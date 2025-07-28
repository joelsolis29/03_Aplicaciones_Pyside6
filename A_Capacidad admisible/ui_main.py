# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEAxgYT.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 752)
        icon = QIcon()
        icon.addFile(u":/Iconos/luna.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget_2 = QTabWidget(self.frame)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(0, 600))
        self.tabWidget_2.setMaximumSize(QSize(16777208, 16777215))
        self.tabWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_11 = QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_15 = QFrame(self.groupBox_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 30))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_13.addWidget(self.label_21)


        self.verticalLayout_12.addWidget(self.frame_15)

        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_12.addWidget(self.lineEdit)

        self.frame_16 = QFrame(self.groupBox_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_14.addWidget(self.label_22)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_12.addWidget(self.lineEdit_2)

        self.frame_17 = QFrame(self.groupBox_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 30))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_15.addWidget(self.label_23)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.lineEdit_3 = QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_12.addWidget(self.lineEdit_3)

        self.frame_18 = QFrame(self.groupBox_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 30))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_24 = QLabel(self.frame_18)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_16.addWidget(self.label_24)


        self.verticalLayout_12.addWidget(self.frame_18)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_12.addWidget(self.lineEdit_4)

        self.frame_19 = QFrame(self.groupBox_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 30))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_17.addWidget(self.label_25)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_12.addWidget(self.lineEdit_5)

        self.frame_20 = QFrame(self.groupBox_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 30))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_26 = QLabel(self.frame_20)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_18.addWidget(self.label_26)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.lineEdit_6 = QLineEdit(self.groupBox_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_12.addWidget(self.lineEdit_6)

        self.frame_21 = QFrame(self.groupBox_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 30))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_21)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_27 = QLabel(self.frame_21)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_19.addWidget(self.label_27)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.dateEdit = QDateEdit(self.groupBox_5)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2025, 3, 25), QTime(15, 0, 0)))

        self.verticalLayout_12.addWidget(self.dateEdit)

        self.frame_22 = QFrame(self.groupBox_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 35))
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_28 = QLabel(self.frame_22)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_14.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_22)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_14.addWidget(self.label_29)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.pushButton = QPushButton(self.groupBox_5)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 20))

        self.verticalLayout_12.addWidget(self.pushButton)


        self.verticalLayout_11.addWidget(self.groupBox_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_4 = QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.frame_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_5.addWidget(self.comboBox_2)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMaximum(1000.000000000000000)
        self.doubleSpinBox.setValue(1.000000000000000)

        self.verticalLayout_2.addWidget(self.doubleSpinBox)

        self.frame_7 = QFrame(self.groupBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.comboBox_3 = QComboBox(self.frame_7)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_6.addWidget(self.comboBox_3)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMaximum(1000.000000000000000)
        self.doubleSpinBox_6.setValue(1.000000000000000)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_6)

        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.comboBox_4 = QComboBox(self.frame_8)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_7.addWidget(self.comboBox_4)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setValue(1.000000000000000)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_7)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_7 = QGroupBox(self.tab_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_33 = QFrame(self.groupBox_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 40))
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_43 = QLabel(self.frame_33)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_23.addWidget(self.label_43)

        self.comboBox_17 = QComboBox(self.frame_33)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_23.addWidget(self.comboBox_17)


        self.verticalLayout_25.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.groupBox_7)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 40))
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.radioButton_4 = QRadioButton(self.frame_35)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_28.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.frame_35)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_28.addWidget(self.radioButton_5)


        self.verticalLayout_25.addWidget(self.frame_35)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")
        self.doubleSpinBox_14.setEnabled(False)

        self.verticalLayout_25.addWidget(self.doubleSpinBox_14)

        self.frame_31 = QFrame(self.groupBox_7)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 40))
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_41 = QLabel(self.frame_31)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_21.addWidget(self.label_41)

        self.comboBox_16 = QComboBox(self.frame_31)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_21.addWidget(self.comboBox_16)


        self.verticalLayout_25.addWidget(self.frame_31)

        self.frame_34 = QFrame(self.groupBox_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.radioButton_6 = QRadioButton(self.frame_34)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setChecked(True)

        self.horizontalLayout_24.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.frame_34)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_24.addWidget(self.radioButton_7)


        self.verticalLayout_25.addWidget(self.frame_34)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")
        self.doubleSpinBox_13.setValue(10.000000000000000)

        self.verticalLayout_25.addWidget(self.doubleSpinBox_13)


        self.verticalLayout_4.addWidget(self.groupBox_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_24 = QVBoxLayout(self.tab_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_8 = QGroupBox(self.tab_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_36 = QFrame(self.groupBox_8)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 40))
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_45 = QLabel(self.frame_36)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_25.addWidget(self.label_45)

        self.comboBox_19 = QComboBox(self.frame_36)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_25.addWidget(self.comboBox_19)


        self.verticalLayout_26.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.groupBox_8)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 40))
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_46 = QLabel(self.frame_37)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_26.addWidget(self.label_46)

        self.comboBox_20 = QComboBox(self.frame_37)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_26.addWidget(self.comboBox_20)


        self.verticalLayout_26.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.groupBox_8)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 40))
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_5 = QPushButton(self.frame_38)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_27.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_38)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_27.addWidget(self.pushButton_6)


        self.verticalLayout_26.addWidget(self.frame_38)

        self.tableWidget = QTableWidget(self.groupBox_8)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_26.addWidget(self.tableWidget)

        self.pushButton_7 = QPushButton(self.groupBox_8)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_26.addWidget(self.pushButton_7)


        self.verticalLayout_24.addWidget(self.groupBox_8)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_8 = QVBoxLayout(self.tab_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_2 = QGroupBox(self.tab_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(False)

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.frame_13 = QFrame(self.groupBox_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.comboBox_10 = QComboBox(self.frame_13)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_12.addWidget(self.comboBox_10)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setValue(30.000000000000000)

        self.verticalLayout_3.addWidget(self.doubleSpinBox_2)

        self.frame_12 = QFrame(self.groupBox_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.comboBox_9 = QComboBox(self.frame_12)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_11.addWidget(self.comboBox_9)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.verticalLayout_3.addWidget(self.doubleSpinBox_3)

        self.frame_11 = QFrame(self.groupBox_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.comboBox_8 = QComboBox(self.frame_11)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.comboBox_8)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setValue(18.000000000000000)

        self.verticalLayout_3.addWidget(self.doubleSpinBox_4)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_6 = QGroupBox(self.tab_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_23 = QFrame(self.groupBox_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 40))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_30 = QLabel(self.frame_23)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_15.addWidget(self.label_30)

        self.comboBox_11 = QComboBox(self.frame_23)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_15.addWidget(self.comboBox_11)


        self.verticalLayout_20.addWidget(self.frame_23)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setMaximum(99999999.000000000000000)
        self.doubleSpinBox_10.setValue(25.000000000000000)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_10)

        self.frame_24 = QFrame(self.groupBox_6)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 40))
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_24)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_21.addWidget(self.label_31)


        self.verticalLayout_20.addWidget(self.frame_24)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMaximum(1.000000000000000)
        self.doubleSpinBox_11.setValue(0.300000000000000)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_11)


        self.verticalLayout_8.addWidget(self.groupBox_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_9 = QVBoxLayout(self.tab_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.tab_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_9 = QFrame(self.groupBox_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.comboBox_6 = QComboBox(self.frame_9)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_8.addWidget(self.comboBox_6)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.verticalLayout_7.addWidget(self.doubleSpinBox_8)

        self.frame_26 = QFrame(self.groupBox_3)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_34 = QLabel(self.frame_26)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.comboBox_7 = QComboBox(self.frame_26)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_16.addWidget(self.comboBox_7)


        self.verticalLayout_7.addWidget(self.frame_26)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setValue(5.000000000000000)

        self.verticalLayout_7.addWidget(self.doubleSpinBox_5)

        self.frame_27 = QFrame(self.groupBox_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_35 = QLabel(self.frame_27)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_17.addWidget(self.label_35)

        self.comboBox_12 = QComboBox(self.frame_27)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_17.addWidget(self.comboBox_12)


        self.verticalLayout_7.addWidget(self.frame_27)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")
        self.doubleSpinBox_12.setValue(18.000000000000000)

        self.verticalLayout_7.addWidget(self.doubleSpinBox_12)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_14 = QFrame(self.groupBox_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBox_9.setValue(3.000000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_9)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_9.addWidget(self.groupBox_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.tabWidget_2.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_32 = QFrame(self.frame)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_4 = QPushButton(self.frame_32)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_22.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_32)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_22.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_32)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_32)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(480, 480))
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 50))
        self.tableView.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.tableView)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)

        self.tableView_2 = QTableView(self.frame_3)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setMinimumSize(QSize(0, 50))
        self.tableView_2.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.tableView_2)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_6.addWidget(self.label_14)

        self.tableView_3 = QTableView(self.frame_3)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setMinimumSize(QSize(0, 50))
        self.tableView_3.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.tableView_3)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 27, 42);\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 0))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_17)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(50, 0))
        self.comboBox.setMaximumSize(QSize(500, 16777215))
        self.comboBox.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 27, 42);\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_4.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_19)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(50, 0))
        self.comboBox_5.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.comboBox_5)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_22 = QVBoxLayout(self.tab_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_10 = QFrame(self.tab_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_32 = QLabel(self.frame_10)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_9.addWidget(self.label_32)


        self.verticalLayout_22.addWidget(self.frame_10)

        self.frame_25 = QFrame(self.tab_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_25)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_37 = QLabel(self.frame_28)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_18.addWidget(self.label_37)

        self.label_36 = QLabel(self.frame_28)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_36)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)

        self.comboBox_13 = QComboBox(self.frame_28)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setMinimumSize(QSize(50, 0))
        self.comboBox_13.setMaximumSize(QSize(500, 16777215))
        self.comboBox_13.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.comboBox_13)


        self.verticalLayout_23.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_40 = QLabel(self.frame_30)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_20.addWidget(self.label_40)

        self.comboBox_15 = QComboBox(self.frame_30)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.horizontalLayout_20.addWidget(self.comboBox_15)


        self.verticalLayout_23.addWidget(self.frame_30)

        self.label_42 = QLabel(self.frame_25)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_23.addWidget(self.label_42)

        self.tableView_5 = QTableView(self.frame_25)
        self.tableView_5.setObjectName(u"tableView_5")

        self.verticalLayout_23.addWidget(self.tableView_5)

        self.label_33 = QLabel(self.frame_25)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_23.addWidget(self.label_33)

        self.tableView_4 = QTableView(self.frame_25)
        self.tableView_4.setObjectName(u"tableView_4")

        self.verticalLayout_23.addWidget(self.tableView_4)


        self.verticalLayout_22.addWidget(self.frame_25)

        self.frame_29 = QFrame(self.tab_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 27, 42);\n"
"")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_38 = QLabel(self.frame_29)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_19.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_29)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 0))
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_39)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.comboBox_14 = QComboBox(self.frame_29)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_19.addWidget(self.comboBox_14)


        self.verticalLayout_22.addWidget(self.frame_29)

        self.frame_39 = QFrame(self.tab_2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 27, 42);\n"
"")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_47 = QLabel(self.frame_39)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_29.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_39)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(50, 0))
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_48)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_5)

        self.comboBox_21 = QComboBox(self.frame_39)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setMaximumSize(QSize(90, 40))

        self.horizontalLayout_29.addWidget(self.comboBox_21)


        self.verticalLayout_22.addWidget(self.frame_39)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bearing capacity - JS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input parameters", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Project information", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Paquete R-10 Chancay", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Subproject", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"2527677", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Structure", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"DME Cantagallo", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Elaborated by", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"H.A.", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Approved by", None))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"H.A.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Revision", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"0A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Loco company", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Project parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Footing dimensions", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Footing width", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Footing length", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Footing depth", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"General information", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Groundwater level", None))
        self.comboBox_17.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_17.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_17.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Found", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Not found", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Bedrock level", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_16.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Identified", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Not identified", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Geometry parameters", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Statigraphy", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Unit of depth", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_19.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_19.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Unit of density", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"kN/m3", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"kgf/cm3", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("MainWindow", u"tonf/m3", None))

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Delete Row", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Depth", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Clasification", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Dry density", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Saturated density", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Watch profile", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Soil profile", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Shear strength parameters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soil type", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Cohesive soils", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Frictional soils", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Cohesive-Frictional soils", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Friction Angle", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"deg", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"rad", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cohesion [kPa]", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"MPa", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"kgf/cm2", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"tonf/m2", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dry unit weight", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"kN/m3", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"kgf/cm3", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"tonf/m3", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Deformation parameters", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Elastic modulus", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"MPa", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"kgf/cm2", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("MainWindow", u"tonf/m2", None))

        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Poisson ratio", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Geotechnical parameters", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Load parameters", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Load inclination", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"deg", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"rad", None))

        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Average thickness", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"in", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Fill Unit weight", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"kN/m3", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"kgf/cm3", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"tonf/m3", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Reduction factors", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Factor of safety", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Load parameters", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate report", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bearing capacity equation:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"qult = qadm", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Loading factors", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Shape factors", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Load inclination factors", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ultimate bearing capacity", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MPa", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"kgf/cm2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"tonf/m2", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Allowable bearing capacity", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"MPa", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"kgf/cm2", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"tonf/m2", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Bearing capacity", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Elastic settlement equation", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Net Pressure", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"MPa", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"kgf/cm2", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"tonf/m2", None))

        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Point of evaluation", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Center", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"Corner", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Geometric relation (m y n)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Shape factor (Is) and Depht factor (If)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Elastic settlement", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"mm", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"in", None))

        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Allowable settlement", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"m", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("MainWindow", u"mm", None))
        self.comboBox_21.setItemText(3, QCoreApplication.translate("MainWindow", u"ft", None))
        self.comboBox_21.setItemText(4, QCoreApplication.translate("MainWindow", u"in", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settlements", None))
    # retranslateUi

