import sys
import os
import json
import tempfile
from PySide6.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt, QDate
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

import pandas as pd

from ui_main import Ui_MainWindow
from data import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Parametros iniciales
        self.test = AGS()

        # Acciones sobre click en botones
        self.ui.pushButton.clicked.connect(self.open_file)

        # Acciones sobre cambios en combobox
        self.ui.comboBox.currentTextChanged.connect(lambda: self.fill_table(self.ui.tableView, self.ui.comboBox.currentText()))
        self.ui.comboBox.currentTextChanged.connect(self.sublist_comb)
        self.ui.comboBox_2.currentTextChanged.connect(self.unique_list)

        self.show()
    
    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self,filter="AGS Files (*.ags)")
        self.test.file_path = self.file[0]

        self.fill_table(self.ui.tableView,"LOCA")
        self.list_comb()

    def fill_table(self, table_view, group):
        df = self.test.read_group(group, df_to_return="data")

        model = QStandardItemModel()
        model.setRowCount(len(df))
        model.setColumnCount(len(df.columns))
        model.setHorizontalHeaderLabels(df.columns.tolist())

        for row in range(len(df)):
            for col in range(len(df.columns)):
                item = QStandardItem(str(df.iat[row, col]))
                model.setItem(row, col, item)

        table_view.setModel(model)

        # Ajustar el tamaño de columnas
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def list_comb(self):
        items = self.test.get_group()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(items)

    def sublist_comb(self):
        df = self.test.read_group(self.ui.comboBox.currentText(), df_to_return="data")
        headings = df.columns.tolist()  # Obtener los encabezados como lista
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(headings)        

    def unique_list(self):
        df = self.test.read_group(self.ui.comboBox.currentText(), df_to_return="data")
        field = self.ui.comboBox_2.currentText()

        if not field:  # Si está vacío, no hacer nada o mostrar advertencia
            return

        if field not in df.columns:
            return

        # Obtener valores únicos con sus cantidades
        counts = df[field].value_counts(dropna=True).reset_index()
        counts.columns = [field, 'COUNT']  # Renombrar columnas

        # Crear un modelo para el QTableView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([field, 'COUNT', 'INCLUDE'])

        for row in counts.itertuples(index=False):
            value_item = QStandardItem(str(row[0]))
            count_item = QStandardItem(str(row[1]))

            checkbox_item = QStandardItem()
            checkbox_item.setCheckable(True)
            checkbox_item.setCheckState(Qt.CheckState.Unchecked)
            checkbox_item.setEditable(False)

            model.appendRow([value_item, count_item, checkbox_item])            

        # Asignar el modelo al QTableView
        self.ui.tableView_2.setModel(model)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

