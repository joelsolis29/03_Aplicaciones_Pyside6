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

#Convertir en ejecutable standalone
#python -m PyInstaller main.py --onefile --windowed --icon=luna.ico

from ui_main import Ui_MainWindow
from data import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #==========================================
        #Crear elemento a partir de una clase
        self.report = Datos()

        #==========================================
        #Estados iniciales
        #Logo por defecto
        self.logo_path = self.report.logo

        #Ecuacion por defecto
        self.ui.label_11.setText("q<sub>d</sub> = i<sub>q</sub> · y<sub>1</sub> · D<sub>f</sub> x N<sub>q</sub> + 0.5 s<sub>y</sub> · i<sub>y</sub> · y<sub>2</sub> · B' · N<sub>y</sub>")
        self.ui.label_32.setText("S<sub>e</sub> = q<sub>o</sub>(&#945;B') · (1 - u<sup>2</sup>)/E<sub>s</sub> · I<sub>s</sub> · I<sub>f</sub>")

        #Control sobre el tipo de suelo cohesivo/friccionante
        self.ui.doubleSpinBox_3.setEnabled(False)
        self.ui.doubleSpinBox_2.setEnabled(True)

        #Crear los layouts en cada pestaña
        self.layout_raw = QVBoxLayout()
        self.ui.tab.setLayout(self.layout_raw)

        self.layout_fit = QVBoxLayout()
        self.ui.tab_2.setLayout(self.layout_fit)

        #Crear las tablas de factores    
        datos = [
            load_factor(self.ui.doubleSpinBox_2.value()),
            shape_factor(self.ui.doubleSpinBox.value(),self.ui.doubleSpinBox_6.value()),
            inclination_factor(self.ui.doubleSpinBox_8.value(),self.ui.doubleSpinBox_2.value())
        ]

        factor = point_factor(self.ui.comboBox_15.currentText(), 
                            self.ui.doubleSpinBox.value(), 
                            self.ui.doubleSpinBox_6.value(), 
                            self.ui.doubleSpinBox_7.value(), 
                            self.ui.doubleSpinBox_13.value())
        
        datos2 = set_factor(self.ui.doubleSpinBox_11.value(), factor[1], factor[2],
                            self.ui.doubleSpinBox.value(), 
                            self.ui.doubleSpinBox_6.value(), 
                            self.ui.doubleSpinBox_7.value())

        self.columnas = [["Nc", "Nq", "Ny"],["Sc", "Sq", "Sy"],["ic", "iq", "iy"]]
        self.columnas2 = [["Is","If"],["m","n"]]

        self.fill_table(datos[0],self.columnas[0],self.ui.tableView)
        self.fill_table(datos[1],self.columnas[1],self.ui.tableView_2)
        self.fill_table(datos[2],self.columnas[2],self.ui.tableView_3)
        self.fill_table(datos2,self.columnas2[0],self.ui.tableView_4)
        self.fill_table(factor[1:3],self.columnas2[1],self.ui.tableView_5)
        
        self.res_pres()
        self.net_pres()
        self.set_pres()
        self.set_adm()
        #==========================================
        #Acciones

        # Acciones sobre click en botones
        self.ui.pushButton_5.clicked.connect(self.add_row)
        self.ui.pushButton_6.clicked.connect(self.del_row)
        self.ui.pushButton_7.clicked.connect(self.show_prof)
        self.ui.pushButton_2.clicked.connect(self.gen_report)
        self.ui.pushButton.clicked.connect(self.open_logo)
        self.ui.pushButton_3.clicked.connect(self.save_file)
        self.ui.pushButton_4.clicked.connect(self.open_file)

        #Acciones sobre el cambio en el ancho de cimentación
        self.ui.doubleSpinBox.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox.valueChanged.connect(self.res_pres)
        self.ui.doubleSpinBox.valueChanged.connect(self.update_table2)
        self.ui.doubleSpinBox.valueChanged.connect(self.set_pres)

        #Acciones sobre el cambio en el largo de cimentación
        self.ui.doubleSpinBox_6.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_6.valueChanged.connect(self.res_pres)
        self.ui.doubleSpinBox_6.valueChanged.connect(self.update_table2)
        self.ui.doubleSpinBox_6.valueChanged.connect(self.set_pres)

        #Acciones sobre el cambio en la profundidad de cimentación
        self.ui.doubleSpinBox_7.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_7.valueChanged.connect(self.res_pres)
        self.ui.doubleSpinBox_7.valueChanged.connect(self.update_table2)
        self.ui.doubleSpinBox_7.valueChanged.connect(self.set_pres)

        #Acciones sobre el cambio en el espesor del suelo
        self.ui.doubleSpinBox_13.valueChanged.connect(self.update_table2)
        self.ui.doubleSpinBox_13.valueChanged.connect(self.set_pres)

        # Acciones sobre el cambio en el ángulo de fricción
        self.ui.doubleSpinBox_2.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_2.valueChanged.connect(self.res_pres)

        # Acciones sobre el cambio en la cohesión
        self.ui.doubleSpinBox_3.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.res_pres)

        # Acciones sobre el cambio en el coeficiente de elasticidad
        self.ui.doubleSpinBox_10.valueChanged.connect(self.set_pres)

        # Acciones sobre el cambio en el coeficiente de Poisson
        self.ui.doubleSpinBox_13.valueChanged.connect(self.update_table2)
        self.ui.doubleSpinBox_11.valueChanged.connect(self.set_pres)

        # Acciones sobre el cambio en el ángulo de inclinación de la carga
        self.ui.doubleSpinBox_8.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_8.valueChanged.connect(self.res_pres)

        # Acciones sobre el cambio en el peso especifico seco
        self.ui.doubleSpinBox_4.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_4.valueChanged.connect(self.res_pres)

        # Acciones sobre el cambio del factor de seguridad
        self.ui.doubleSpinBox_9.valueChanged.connect(self.update_table)
        self.ui.doubleSpinBox_9.valueChanged.connect(self.res_pres)

        # Acciones sobre el cambio del espesor del relleno
        self.ui.doubleSpinBox_5.valueChanged.connect(self.net_pres)
        self.ui.doubleSpinBox_12.valueChanged.connect(self.net_pres)
        self.ui.doubleSpinBox_5.valueChanged.connect(self.set_pres)
        self.ui.doubleSpinBox_12.valueChanged.connect(self.set_pres)
        self.ui.doubleSpinBox_5.valueChanged.connect(self.set_adm)

        # Actualizar texto
        self.ui.radioButton.toggled.connect(self.update_equation)
        self.ui.radioButton_2.toggled.connect(self.update_equation)
        self.ui.radioButton_3.toggled.connect(self.update_equation)

        self.ui.radioButton_4.toggled.connect(self.gw_input)
        self.ui.radioButton_5.toggled.connect(self.gw_input)       

        # Cambio de ubicacion del punto de evaluacion
        self.ui.comboBox_15.currentTextChanged.connect(self.update_table2)

        # Cambio de unidades
        self.ui.comboBox.currentTextChanged.connect(lambda: self.unit_changed(self.ui.comboBox, self.ult_pres(), self.ui.label_17,"pressure"))
        self.ui.comboBox_5.currentTextChanged.connect(lambda: self.unit_changed(self.ui.comboBox_5, self.ult_pres()/3, self.ui.label_19,"pressure"))
        self.ui.comboBox_21.currentTextChanged.connect(self.set_adm)
        self.ui.comboBox_14.currentTextChanged.connect(self.set_pres)
        self.ui.comboBox_13.currentTextChanged.connect(lambda: self.unit_changed(self.ui.comboBox_13, self.net_pres(), self.ui.label_36,"pressure"))


        #==========================================
        self.show()

    #==========================================
    #Agregar y eliminar fila
    def add_row(self):
        self.opciones = ["Rock", "Fract. Rock","Gravel", "Sand", "Clay", "Lime"]
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        # Crear y añadir el combo box en la columna 0
        combo = QComboBox()
        combo.addItems(self.opciones)
        self.ui.tableWidget.setCellWidget(row_position, 1, combo)

        # Crear QDoubleSpinBox para la columna 5 (índice 5)
        for col in [0, 2, 3]:
            spin = QDoubleSpinBox()
            spin.setDecimals(2)
            spin.setMinimum(0.00)
            spin.setMaximum(999999.99)
            spin.setSingleStep(0.10)
            spin.setValue(0.00)
            spin.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.ui.tableWidget.setCellWidget(row_position, col, spin)

    def del_row(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            self.ui.tableWidget.removeRow(current_row)

    #==========================================
    #Convertir tabla a dataframe
    def table_to_dataframe(self, tableWidget):
        rows = tableWidget.rowCount()
        cols = tableWidget.columnCount()
        data = []

        for row in range(rows):
            row_data = []
            for col in range(cols):
                # Try to get widget first (QComboBox, QDoubleSpinBox, etc.)
                widget = tableWidget.cellWidget(row, col)
                if isinstance(widget, QComboBox):
                    value = widget.currentText()
                elif isinstance(widget, QDoubleSpinBox):
                    value = widget.value()
                else:
                    item = tableWidget.item(row, col)
                    value = item.text() if item is not None else ""
                row_data.append(value)
            data.append(row_data)

        # Optional: Get headers if you set them
        headers = [
            tableWidget.horizontalHeaderItem(i).text()
            if tableWidget.horizontalHeaderItem(i) is not None else f"Column {i}"
            for i in range(cols)
        ]

        df = pd.DataFrame(data, columns=headers)
        return df

    #==========================================
    #Cargar logo
    def open_logo(self):
        self.update = False

        file = QFileDialog.getOpenFileName(self, filter="Image files (*.png *.jpg *.jpeg *.bmp)")
        file_path = file[0]

        if file_path:
            # Mostrar el nombre del archivo en label_29
            namefile = file_path.split("/")[-1]
            self.ui.label_29.setText(namefile)

            # Guardar la ruta si la necesitas más adelante
            self.logo_path = file_path

        self.update = True 

    #==========================================
    #Cambio de unidades
    def unit_changed(self, combo, valor, label, measure):
        unit = combo.currentText()
        if measure == "pressure":
            if unit == "MPa":
                valor_c = valor / 1000
            elif unit == "kPa":
                valor_c = valor
            elif unit == "tonf/m2":
                valor_c = valor * 0.10197
            elif unit == "kgf/cm2":
                valor_c = valor * 0.0101972  
            else:
                valor_c = valor
        elif measure == "length":
            if unit == "m":
                valor_c = valor
            elif unit == "cm":
                valor_c = valor*100
            elif unit == "mm":
                valor_c = valor*1000
            else:
                valor_c = valor

        label.setText(f"{valor_c:.2f}")
        return valor_c

    #==========================================
    # Actualizar ecuación
    def update_equation(self):
        if self.ui.radioButton.isChecked():
            self.ui.label_11.setText("q<sub>d</sub> = i<sub>q</sub> · y<sub>1</sub> · D<sub>f</sub> x N<sub>q</sub> + 0.5 s<sub>y</sub> · i<sub>y</sub> · y<sub>2</sub> · B' · N<sub>y</sub>")
            self.ui.doubleSpinBox_3.setEnabled(False)
            self.ui.doubleSpinBox_2.setEnabled(True)
            self.ui.doubleSpinBox_3.setValue(0)
        elif self.ui.radioButton_2.isChecked():
            self.ui.label_11.setText("q<sub>d</sub> = s<sub>c</sub> · i<sub>c</sub> · c · N<sub>c</sub>")
            self.ui.doubleSpinBox_2.setEnabled(False)
            self.ui.doubleSpinBox_3.setEnabled(True)
            self.ui.doubleSpinBox_2.setValue(0)
        elif self.ui.radioButton_3.isChecked():
            self.ui.label_11.setText("q<sub>d</sub> = s<sub>c</sub> · i<sub>c</sub> · c · N<sub>c</sub> + i<sub>q</sub> · y<sub>1</sub> · D<sub>f</sub> x N<sub>q</sub> + 0.5 s<sub>y</sub> · i<sub>y</sub> · y<sub>2</sub> · B' · N<sub>y</sub>")
            self.ui.doubleSpinBox_3.setEnabled(True)
            self.ui.doubleSpinBox_2.setEnabled(True)  

    # Actualizar input dl nivel freatico
    def gw_input(self):
        if self.ui.radioButton_4.isChecked():
            self.ui.doubleSpinBox_14.setEnabled(True)
            return True

        elif self.ui.radioButton_5.isChecked():
            self.ui.doubleSpinBox_14.setValue(0)
            self.ui.doubleSpinBox_14.setEnabled(False)
            return False
    
    #==========================================
    # Boton de generar reporte
    def gen_report(self):
        # Generamos el perfil y obtengo la ruta de la imagen
        per_path = self.per_est()
        self.report.perf_image = per_path  # o cualquier otro nombre que uses
        
        # Obtener información de tablas        
        model_n = self.ui.tableView.model()
        model_s = self.ui.tableView_2.model()
        model_i = self.ui.tableView_3.model()

        model_g = self.ui.tableView_5.model()
        model_is = self.ui.tableView_4.model()

        # Actualizar datos del reporte
        self.report.pro = self.ui.lineEdit.text()
        self.report.sub = self.ui.lineEdit_2.text()
        self.report.est = self.ui.lineEdit_3.text()
        self.report.elab = self.ui.lineEdit_4.text()
        self.report.aprob = self.ui.lineEdit_5.text()
        self.report.rev = self.ui.lineEdit_6.text()
        self.report.fec = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        self.report.logo = self.logo_path

        # Actualizar parametros
        self.report.coh = self.ui.doubleSpinBox_3.value()
        self.report.phi = self.ui.doubleSpinBox_2.value()
        self.report.ydr = self.ui.doubleSpinBox_4.value()
        self.report.ymo = self.ui.doubleSpinBox_4.value()
        self.report.mu = self.ui.doubleSpinBox_11.value()
        self.report.Es = self.ui.doubleSpinBox_10.value()

        self.report.B = self.ui.doubleSpinBox.value()
        self.report.L = self.ui.doubleSpinBox_6.value()
        self.report.Df = self.ui.doubleSpinBox_7.value()
        self.report.Ht = self.ui.doubleSpinBox_13.value()

        self.report.tma = self.ui.doubleSpinBox_5.value()
        self.report.yf = self.ui.doubleSpinBox_12.value()
        self.report.alp = self.ui.doubleSpinBox_8.value()

        self.report.Nc, self.report.Nq, self.report.Ny = float(model_n.item(0, 0).text()), float(model_n.item(0, 1).text()), float(model_n.item(0, 2).text())        
        self.report.sc, self.report.sq, self.report.sy = float(model_s.item(0, 0).text()), float(model_s.item(0, 1).text()), float(model_s.item(0, 2).text())        
        self.report.ic, self.report.iq, self.report.iy = float(model_i.item(0, 0).text()), float(model_i.item(0, 1).text()), float(model_i.item(0, 2).text())        

        self.report.m, self.report.n = float(model_g.item(0, 0).text()), float(model_g.item(0, 1).text())       
        self.report.Is, self.report.If = float(model_is.item(0, 0).text()), float(model_is.item(0, 1).text())

        self.report.pmax = self.ui.label_36.text()
        self.report.qult = self.ui.label_17.text()   
        self.report.qadm = self.ui.label_19.text()

        self.report.s_e = self.ui.label_39.text() 
        self.report.s_a = self.ui.label_48.text()

        self.report.u_pm, self.report.u_qu,self.report.u_qa = self.ui.comboBox_13.currentText(), self.ui.comboBox.currentText(), self.ui.comboBox_5.currentText()
        self.report.u_se, self.report.u_sa = self.ui.comboBox_14.currentText(), self.ui.comboBox_21.currentText()

        # Abrir un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo PDF
        options = QFileDialog.Options()
        self.file = QFileDialog.getSaveFileName(self, "Guardar Reporte PDF", "", "PDF Files (*.pdf)", options=options)
        
        file_path = self.file[0]


        
        if file_path:
            # Definir la ruta en la clase reporte
            self.report.file = file_path
            # Si el usuario seleccionó una ubicación, genera el PDF en esa ruta
            self.report.gen_pdf()
    
    #==========================================
    # Funcion para llenar tabla
    def fill_table(self, fila_datos, columnas, tableview):
        model = QStandardItemModel()
        model.setColumnCount(len(columnas))
        model.setHorizontalHeaderLabels(columnas)

        items = []
        for celda in fila_datos:
            item = QStandardItem(f"{celda:.2f}")
            item.setTextAlignment(Qt.AlignCenter)
            item.setBackground(QColor("#2E3A59"))  # Fondo celda
            item.setForeground(QColor("white"))    # Texto
            items.append(item)

        model.appendRow(items)
        tableview.setModel(model)

        # Ajustar el ancho de columnas
        tableview.horizontalHeader().setStretchLastSection(True)
        tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    #==========================================
    # Funcion para actualizar tabla
    def update_table(self):
        self.fill_table(load_factor(self.ui.doubleSpinBox_2.value()),self.columnas[0],self.ui.tableView)
        self.fill_table(shape_factor(self.ui.doubleSpinBox.value(),self.ui.doubleSpinBox_6.value()),self.columnas[1],self.ui.tableView_2)
        self.fill_table(inclination_factor(self.ui.doubleSpinBox_8.value(), self.ui.doubleSpinBox_2.value()),self.columnas[2],self.ui.tableView_3)
  
    #==========================================
    # Funcion para actualizar la capacidad ultima cuando cambie algun valor en la tabla    
    def ult_pres(self):
        model_n = self.ui.tableView.model()
        model_s = self.ui.tableView_2.model()
        model_i = self.ui.tableView_3.model()

        datos = [
            [float(model_n.item(0, 0).text()), float(model_n.item(0, 1).text()), float(model_n.item(0, 2).text())],
            [float(model_s.item(0, 0).text()), float(model_s.item(0, 1).text()), float(model_s.item(0, 2).text())],
            [float(model_i.item(0, 0).text()), float(model_i.item(0, 1).text()), float(model_i.item(0, 2).text())]
        ]

        valor = ult_bearing(
            self.ui.doubleSpinBox_3.value(),
            1.00,
            self.ui.doubleSpinBox_7.value(),
            datos[0],
            datos[1],
            datos[2],
            self.ui.doubleSpinBox_4.value(),
            self.ui.doubleSpinBox_4.value()
        )

        return valor
    
    #==========================================
    # Funcion para mostrar el resultado
    def res_pres(self):
        valor = self.ult_pres()  # Obtener el valor base de la función ult_pres

        # Actualizar los labels dependiendo de la unidad seleccionada
        self.unit_changed(self.ui.comboBox, valor, self.ui.label_17,"pressure")
        self.unit_changed(self.ui.comboBox_5, valor/self.ui.doubleSpinBox_9.value(), self.ui.label_19,"pressure")

    #==========================================
    # Funcion para estimar la presion neta sobre el terreno
    def net_pres(self):
        valor = self.ui.doubleSpinBox_5.value()*self.ui.doubleSpinBox_12.value()
        self.unit_changed(self.ui.comboBox_13, valor, self.ui.label_36,"pressure")
        return valor

    #==========================================
    #Funcion para actualizar tabla 2
    def update_table2(self):
        factor = point_factor(self.ui.comboBox_15.currentText(), 
                            self.ui.doubleSpinBox.value(), 
                            self.ui.doubleSpinBox_6.value(), 
                            self.ui.doubleSpinBox_7.value(), 
                            self.ui.doubleSpinBox_13.value())
        
        datos2 = set_factor(self.ui.doubleSpinBox_11.value(), factor[1], factor[2],
                            self.ui.doubleSpinBox.value(), 
                            self.ui.doubleSpinBox_6.value(), 
                            self.ui.doubleSpinBox_7.value())
        self.fill_table(datos2,self.columnas2[0],self.ui.tableView_4)
        self.fill_table(factor[1:3],self.columnas2[1],self.ui.tableView_5)

    #==========================================
    #Funcion para calcular el asentamiento elastico
    def set_pres(self):
        if self.ui.comboBox_15.currentText() == "Center":
            alpha = 4
            b = 0.5*self.ui.doubleSpinBox.value()
        else:
            alpha = 1
            b = self.ui.doubleSpinBox.value()
        
        model_n = self.ui.tableView_4.model()
        datos = [float(model_n.item(0, 0).text()), float(model_n.item(0, 1).text())]

        valor = self.net_pres() * alpha * b * ((1 - self.ui.doubleSpinBox_11.value()**2) / self.ui.doubleSpinBox_10.value()) * datos[0] * datos[1]
        
        self.unit_changed(self.ui.comboBox_14, valor, self.ui.label_39,"length")

        return valor
    
    def set_adm(self):

        valor = 0.01*self.ui.doubleSpinBox_5.value()
        
        self.unit_changed(self.ui.comboBox_21, valor, self.ui.label_48,"length")        
    
    #==========================================
    #Funcion para generar el perfil estratigrafico
    def per_est(self):
        # Crear ruta temporal para guardar la imagen
        temp_dir = tempfile.gettempdir()
        image_path = os.path.join(temp_dir, "grafico_prueba.png")

        # Obtener los datos del QTableWidget
        df = self.table_to_dataframe(self.ui.tableWidget)

        # Crear gráfica
        fig = create_profile(df, self.ui.doubleSpinBox_14.value(), self.gw_input())

        # Guardar imagen desde la figura creada
        fig.savefig(image_path, dpi=300)
        plt.close(fig)  # Cerrar solo esa figura
        return image_path        
    
    #==========================================
    #Funcion para mostrar el perfil estratigrafico
    def show_prof(self):
        df = self.table_to_dataframe(self.ui.tableWidget)
        
        if df.empty:
            QMessageBox.warning(self, "Advertencia", "La tabla está vacía.")
            return

        fig = create_profile(df, self.ui.doubleSpinBox_14.value(),self.gw_input())

        # Crear diálogo directamente
        dialog = QDialog(self)
        dialog.setWindowTitle("Perfil Estratigráfico")

        layout = QVBoxLayout(dialog)

        # Crear canvas y toolbar
        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, dialog)

        # Agregar al layout
        layout.addWidget(toolbar)
        layout.addWidget(canvas)

        dialog.setLayout(layout)
        dialog.exec()
    
    #==========================================
    #Funcion para guardar y abrir informacion
    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)")
        if path:
            # Extraer informacion de estratigrafia
            rows = self.ui.tableWidget.rowCount()
            columns = self.ui.tableWidget.columnCount()
            data_table = []

            for row in range(rows):
                row_data = []
                for col in range(columns):
                    widget = self.ui.tableWidget.cellWidget(row, col)

                    if isinstance(widget, QComboBox):
                        row_data.append(widget.currentText())
                    elif isinstance(widget, QDoubleSpinBox):
                        row_data.append(str(widget.value()))
                    else:
                        item = self.ui.tableWidget.item(row, col)
                        row_data.append(item.text() if item else "")
                
                data_table.append(row_data)

            # Extraer informacion de los textos
            data = {
                "project": self.ui.lineEdit.text(),
                "subproject": self.ui.lineEdit_2.text(),
                "structure": self.ui.lineEdit_3.text(),
                "elab": self.ui.lineEdit_4.text(),
                "aprov": self.ui.lineEdit_5.text(),
                "revis": self.ui.lineEdit_6.text(),
                "date": self.ui.dateEdit.date().toString("dd/MM/yyyy"),
                "width": self.ui.doubleSpinBox.value(),
                "length": self.ui.doubleSpinBox_6.value(),
                "depth": self.ui.doubleSpinBox_7.value(),
                "load_i": self.ui.doubleSpinBox_8.value(),
                "thick": self.ui.doubleSpinBox_5.value(),
                "u_wei": self.ui.doubleSpinBox_12.value(),
                "fos": self.ui.doubleSpinBox_9.value(),
                "Es": self.ui.doubleSpinBox_10.value(),
                "us": self.ui.doubleSpinBox_11.value(),
                "coh": self.ui.doubleSpinBox_3.value(),
                "phi": self.ui.doubleSpinBox_2.value(),
                "u_dry": self.ui.doubleSpinBox_4.value(),
                "st1": self.ui.radioButton.isChecked(),
                "st2": self.ui.radioButton_2.isChecked(),
                "st3": self.ui.radioButton_3.isChecked(),
                "gw1": self.ui.radioButton_4.isChecked(),
                "gw2": self.ui.radioButton_5.isChecked(),
                "gw_level": self.ui.doubleSpinBox_14.value(),
                "br_level": self.ui.doubleSpinBox_13.value(),
                "table_data": data_table,
                "logo_path" : self.logo_path,
                "unit_pmax" : self.ui.comboBox_13.currentText(),
                "unit_qult" : self.ui.comboBox.currentText(),
                "unit_qadm" : self.ui.comboBox_5.currentText(),
                "unit_se" : self.ui.comboBox_14.currentText(),
                "unit_sa" : self.ui.comboBox_21.currentText()
            }
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)")
        if path:
            with open(path, 'r') as f:
                data = json.load(f)
                self.ui.comboBox_13.setCurrentText(data.get("unit_pmax", ""))                
                self.ui.comboBox.setCurrentText(data.get("unit_qult", ""))
                self.ui.comboBox_5.setCurrentText(data.get("unit_qadm", ""))
                self.ui.comboBox_14.setCurrentText(data.get("unit_se", ""))
                self.ui.comboBox_21.setCurrentText(data.get("unit_sa", ""))
                self.ui.lineEdit.setText(data.get("project", ""))
                self.ui.lineEdit_2.setText(data.get("subproject", ""))
                self.ui.lineEdit_3.setText(data.get("structure", ""))
                self.ui.lineEdit_4.setText(data.get("elab", ""))
                self.ui.lineEdit_5.setText(data.get("aprov", ""))
                self.ui.lineEdit_6.setText(data.get("revis", ""))
                self.ui.dateEdit.setDate(QDate.fromString(data.get("date", ""), "dd/MM/yyyy"))
                self.ui.doubleSpinBox.setValue(data.get("width", ""))
                self.ui.doubleSpinBox_6.setValue(data.get("length", ""))
                self.ui.doubleSpinBox_7.setValue(data.get("depth", ""))
                self.ui.doubleSpinBox_8.setValue(data.get("load_i", ""))
                self.ui.doubleSpinBox_5.setValue(data.get("thick", ""))
                self.ui.doubleSpinBox_12.setValue(data.get("u_wei", ""))
                self.ui.doubleSpinBox_9.setValue(data.get("fos", ""))
                self.ui.doubleSpinBox_10.setValue(data.get("Es", ""))
                self.ui.doubleSpinBox_11.setValue(data.get("us", ""))
                self.ui.radioButton.setChecked(data.get("st1", False))
                self.ui.radioButton_2.setChecked(data.get("st2", False))
                self.ui.radioButton_3.setChecked(data.get("st3", False))
                self.ui.radioButton_4.setChecked(data.get("gw1", False))
                self.ui.radioButton_5.setChecked(data.get("gw2", False))
                self.ui.doubleSpinBox_3.setValue(data.get("coh", ""))
                self.ui.doubleSpinBox_2.setValue(data.get("phi", ""))
                self.ui.doubleSpinBox_4.setValue(data.get("u_dry", ""))
                self.ui.doubleSpinBox_14.setValue(data.get("gw_level", ""))
                self.ui.doubleSpinBox_13.setValue(data.get("br_level", ""))
                self.logo_path = data.get("logo_path","")


                # Cargar datos de la tabla
                table_data = data.get("table_data", [])
                self.ui.tableWidget.setRowCount(0)  # Limpiar tabla antes de cargar

                for row_data in table_data:
                    self.add_row()  # Crea una nueva fila con widgets
                    row = self.ui.tableWidget.rowCount() - 1
                    for col, value in enumerate(row_data):
                        widget = self.ui.tableWidget.cellWidget(row, col)
                        if isinstance(widget, QComboBox):
                            index = widget.findText(value)
                            if index >= 0:
                                widget.setCurrentIndex(index)
                        elif isinstance(widget, QDoubleSpinBox):
                            try:
                                widget.setValue(float(value))
                            except ValueError:
                                widget.setValue(0.0)
                        else:
                            self.ui.tableWidget.setItem(row, col, QTableWidgetItem(value))


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

