# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(197, 220, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calculate.setFont(font)
        self.calculate.setStyleSheet("background-color: rgb(160, 179, 207);")
        self.calculate.setObjectName("calculate")
        self.gridLayout_2.addWidget(self.calculate, 0, 2, 1, 1)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(160, 179, 207);")
        self.back.setObjectName("back")
        self.gridLayout_2.addWidget(self.back, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.main)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 4, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 0, 1, 1)
        self.wre = QtWidgets.QRadioButton(self.main)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wre.setFont(font)
        self.wre.setStyleSheet("")
        self.wre.setAutoExclusive(True)
        self.wre.setObjectName("wre")
        self.shape_group = QtWidgets.QButtonGroup(MainWindow)
        self.shape_group.setObjectName("shape_group")
        self.shape_group.addButton(self.wre)
        self.gridLayout_3.addWidget(self.wre, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 1, 2, 1, 1)
        self.kvadrati = QtWidgets.QRadioButton(self.main)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kvadrati.setFont(font)
        self.kvadrati.setObjectName("kvadrati")
        self.shape_group.addButton(self.kvadrati)
        self.gridLayout_3.addWidget(self.kvadrati, 6, 2, 1, 1)
        self.trapecia = QtWidgets.QRadioButton(self.main)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trapecia.setFont(font)
        self.trapecia.setObjectName("trapecia")
        self.shape_group.addButton(self.trapecia)
        self.gridLayout_3.addWidget(self.trapecia, 5, 2, 1, 1)
        self.samkutxedi = QtWidgets.QRadioButton(self.main)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.samkutxedi.setFont(font)
        self.samkutxedi.setStyleSheet("")
        self.samkutxedi.setObjectName("samkutxedi")
        self.shape_group.addButton(self.samkutxedi)
        self.gridLayout_3.addWidget(self.samkutxedi, 4, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 7, 2, 1, 1)
        self.select = QtWidgets.QPushButton(self.main)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select.setFont(font)
        self.select.setStyleSheet("background-color: rgb(160, 179, 207);")
        self.select.setObjectName("select")
        self.gridLayout_3.addWidget(self.select, 8, 2, 1, 1)
        self.stackedWidget.addWidget(self.main)
        self.samkutxedi_page = QtWidgets.QWidget()
        self.samkutxedi_page.setObjectName("samkutxedi_page")
        self.label_4 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_4.setGeometry(QtCore.QRect(380, 56, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.s1 = QtWidgets.QDoubleSpinBox(self.samkutxedi_page)
        self.s1.setGeometry(QtCore.QRect(510, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s1.setFont(font)
        self.s1.setAlignment(QtCore.Qt.AlignCenter)
        self.s1.setObjectName("s1")
        self.label_5 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_5.setGeometry(QtCore.QRect(380, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.s2 = QtWidgets.QDoubleSpinBox(self.samkutxedi_page)
        self.s2.setGeometry(QtCore.QRect(510, 100, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s2.setFont(font)
        self.s2.setAlignment(QtCore.Qt.AlignCenter)
        self.s2.setObjectName("s2")
        self.label_6 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_6.setGeometry(QtCore.QRect(380, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.s3 = QtWidgets.QDoubleSpinBox(self.samkutxedi_page)
        self.s3.setGeometry(QtCore.QRect(510, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s3.setFont(font)
        self.s3.setAlignment(QtCore.Qt.AlignCenter)
        self.s3.setObjectName("s3")
        self.label_7 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lcd_s_area = QtWidgets.QLCDNumber(self.samkutxedi_page)
        self.lcd_s_area.setGeometry(QtCore.QRect(400, 360, 64, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_s_area.setFont(font)
        self.lcd_s_area.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_s_area.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_s_area.setObjectName("lcd_s_area")
        self.lcd_s_perimeter = QtWidgets.QLCDNumber(self.samkutxedi_page)
        self.lcd_s_perimeter.setGeometry(QtCore.QRect(400, 420, 64, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_s_perimeter.setFont(font)
        self.lcd_s_perimeter.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_s_perimeter.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_s_perimeter.setObjectName("lcd_s_perimeter")
        self.label_11 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_11.setGeometry(QtCore.QRect(70, 30, 281, 241))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("media/triangle.jpg"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_12.setGeometry(QtCore.QRect(380, 220, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.samkutxedi_page)
        self.label_13.setGeometry(QtCore.QRect(380, 260, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.samkutxedi_page)
        self.wre_page = QtWidgets.QWidget()
        self.wre_page.setObjectName("wre_page")
        self.r1 = QtWidgets.QDoubleSpinBox(self.wre_page)
        self.r1.setGeometry(QtCore.QRect(560, 100, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r1.setFont(font)
        self.r1.setObjectName("r1")
        self.label = QtWidgets.QLabel(self.wre_page)
        self.label.setGeometry(QtCore.QRect(416, 106, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.wre_page)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.wre_page)
        self.label_3.setGeometry(QtCore.QRect(16, 380, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lcd_r_area = QtWidgets.QLCDNumber(self.wre_page)
        self.lcd_r_area.setGeometry(QtCore.QRect(400, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_r_area.setFont(font)
        self.lcd_r_area.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_r_area.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_r_area.setObjectName("lcd_r_area")
        self.lcd_r_perimeter = QtWidgets.QLCDNumber(self.wre_page)
        self.lcd_r_perimeter.setGeometry(QtCore.QRect(400, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_r_perimeter.setFont(font)
        self.lcd_r_perimeter.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_r_perimeter.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_r_perimeter.setObjectName("lcd_r_perimeter")
        self.label_14 = QtWidgets.QLabel(self.wre_page)
        self.label_14.setGeometry(QtCore.QRect(50, 23, 341, 261))
        self.label_14.setMinimumSize(QtCore.QSize(341, 261))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("media/circle.png"))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.wre_page)
        self.label_15.setGeometry(QtCore.QRect(420, 170, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.wre_page)
        self.label_16.setGeometry(QtCore.QRect(420, 220, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.wre_page)
        self.trapecia_page = QtWidgets.QWidget()
        self.trapecia_page.setObjectName("trapecia_page")
        self.label_17 = QtWidgets.QLabel(self.trapecia_page)
        self.label_17.setGeometry(QtCore.QRect(340, 40, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.t2 = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.t2.setGeometry(QtCore.QRect(560, 84, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t2.setFont(font)
        self.t2.setAlignment(QtCore.Qt.AlignCenter)
        self.t2.setObjectName("t2")
        self.label_19 = QtWidgets.QLabel(self.trapecia_page)
        self.label_19.setGeometry(QtCore.QRect(340, 94, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.th = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.th.setGeometry(QtCore.QRect(560, 244, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.th.setFont(font)
        self.th.setAlignment(QtCore.Qt.AlignCenter)
        self.th.setObjectName("th")
        self.t1 = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.t1.setGeometry(QtCore.QRect(560, 34, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t1.setFont(font)
        self.t1.setAlignment(QtCore.Qt.AlignCenter)
        self.t1.setObjectName("t1")
        self.label_20 = QtWidgets.QLabel(self.trapecia_page)
        self.label_20.setGeometry(QtCore.QRect(10, 0, 321, 291))
        font = QtGui.QFont()
        font.setPointSize(3)
        self.label_20.setFont(font)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("media/arbitrary-trapezoid.webp"))
        self.label_20.setObjectName("label_20")
        self.lcd_t_area = QtWidgets.QLCDNumber(self.trapecia_page)
        self.lcd_t_area.setGeometry(QtCore.QRect(400, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_t_area.setFont(font)
        self.lcd_t_area.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lcd_t_area.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcd_t_area.setStyleSheet("font-color: rgb(218, 0, 0)\n"
"")
        self.lcd_t_area.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_t_area.setSmallDecimalPoint(False)
        self.lcd_t_area.setProperty("value", 0.0)
        self.lcd_t_area.setObjectName("lcd_t_area")
        self.label_21 = QtWidgets.QLabel(self.trapecia_page)
        self.label_21.setGeometry(QtCore.QRect(20, 430, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lcd_t_perimeter = QtWidgets.QLCDNumber(self.trapecia_page)
        self.lcd_t_perimeter.setGeometry(QtCore.QRect(400, 440, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_t_perimeter.setFont(font)
        self.lcd_t_perimeter.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_t_perimeter.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_t_perimeter.setObjectName("lcd_t_perimeter")
        self.label_22 = QtWidgets.QLabel(self.trapecia_page)
        self.label_22.setGeometry(QtCore.QRect(20, 390, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.trapecia_page)
        self.label_23.setGeometry(QtCore.QRect(21, 330, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.trapecia_page)
        self.label_24.setGeometry(QtCore.QRect(390, 320, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_31 = QtWidgets.QLabel(self.trapecia_page)
        self.label_31.setGeometry(QtCore.QRect(340, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.trapecia_page)
        self.label_32.setGeometry(QtCore.QRect(340, 194, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.t3 = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.t3.setGeometry(QtCore.QRect(560, 134, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t3.setFont(font)
        self.t3.setAlignment(QtCore.Qt.AlignCenter)
        self.t3.setObjectName("t3")
        self.t4 = QtWidgets.QDoubleSpinBox(self.trapecia_page)
        self.t4.setGeometry(QtCore.QRect(560, 184, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t4.setFont(font)
        self.t4.setAlignment(QtCore.Qt.AlignCenter)
        self.t4.setObjectName("t4")
        self.label_34 = QtWidgets.QLabel(self.trapecia_page)
        self.label_34.setGeometry(QtCore.QRect(340, 254, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_17.raise_()
        self.t2.raise_()
        self.label_19.raise_()
        self.th.raise_()
        self.t1.raise_()
        self.lcd_t_area.raise_()
        self.label_21.raise_()
        self.lcd_t_perimeter.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_20.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.t3.raise_()
        self.t4.raise_()
        self.label_34.raise_()
        self.stackedWidget.addWidget(self.trapecia_page)
        self.kvadrati_page = QtWidgets.QWidget()
        self.kvadrati_page.setObjectName("kvadrati_page")
        self.label_25 = QtWidgets.QLabel(self.kvadrati_page)
        self.label_25.setGeometry(QtCore.QRect(70, 40, 271, 261))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("media/square.jpg"))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.kvadrati_page)
        self.label_26.setGeometry(QtCore.QRect(350, 126, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.k1 = QtWidgets.QDoubleSpinBox(self.kvadrati_page)
        self.k1.setGeometry(QtCore.QRect(530, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.k1.setFont(font)
        self.k1.setAlignment(QtCore.Qt.AlignCenter)
        self.k1.setObjectName("k1")
        self.lcd_k_area = QtWidgets.QLCDNumber(self.kvadrati_page)
        self.lcd_k_area.setGeometry(QtCore.QRect(400, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_k_area.setFont(font)
        self.lcd_k_area.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_k_area.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_k_area.setObjectName("lcd_k_area")
        self.lcd_k_perimeter = QtWidgets.QLCDNumber(self.kvadrati_page)
        self.lcd_k_perimeter.setGeometry(QtCore.QRect(400, 420, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_k_perimeter.setFont(font)
        self.lcd_k_perimeter.setStyleSheet("font-color: rgb(218, 0, 0)")
        self.lcd_k_perimeter.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcd_k_perimeter.setObjectName("lcd_k_perimeter")
        self.label_27 = QtWidgets.QLabel(self.kvadrati_page)
        self.label_27.setGeometry(QtCore.QRect(20, 360, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.kvadrati_page)
        self.label_28.setGeometry(QtCore.QRect(20, 420, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.kvadrati_page)
        self.label_29.setGeometry(QtCore.QRect(400, 200, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.kvadrati_page)
        self.label_30.setGeometry(QtCore.QRect(400, 240, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.stackedWidget.addWidget(self.kvadrati_page)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculate.setText(_translate("MainWindow", "გამოთვლა"))
        self.back.setText(_translate("MainWindow", "უკან დაბრუნება"))
        self.wre.setText(_translate("MainWindow", "წრე"))
        self.label_10.setText(_translate("MainWindow", "ფიგურათა პარამეტრების კალკულატორი"))
        self.label_9.setText(_translate("MainWindow", "მონიშნეთ ფიგურა:"))
        self.kvadrati.setText(_translate("MainWindow", "კვადრატი"))
        self.trapecia.setText(_translate("MainWindow", "ტრაპეცია"))
        self.samkutxedi.setText(_translate("MainWindow", "სამკუთხედი"))
        self.select.setText(_translate("MainWindow", "არჩევა"))
        self.label_4.setText(_translate("MainWindow", "I გვერდი"))
        self.label_5.setText(_translate("MainWindow", "II გვერდი"))
        self.label_6.setText(_translate("MainWindow", "III გვერდი"))
        self.label_7.setText(_translate("MainWindow", "ფართობი"))
        self.label_8.setText(_translate("MainWindow", "პერიმეტრი"))
        self.label_12.setText(_translate("MainWindow", "პარამეტრი = a + b + c"))
        self.label_13.setText(_translate("MainWindow", "ფართობი (ჰერონი) = √p(p-a)(p-b)(p-c), სადაც p პერიმეტრის ნახევარია"))
        self.label.setText(_translate("MainWindow", "რადიუსი"))
        self.label_2.setText(_translate("MainWindow", "ფართობი"))
        self.label_3.setText(_translate("MainWindow", "სიგრძე"))
        self.label_15.setText(_translate("MainWindow", "პერიმეტრი(წრის სიგრძე) = 2πr"))
        self.label_16.setText(_translate("MainWindow", "ფართობი = πr^2"))
        self.label_17.setText(_translate("MainWindow", "a გვერდი"))
        self.label_19.setText(_translate("MainWindow", "b გვერდი"))
        self.label_21.setText(_translate("MainWindow", "პერიმეტრი"))
        self.label_22.setText(_translate("MainWindow", "ფართობი"))
        self.label_23.setText(_translate("MainWindow", "პერიმეტრი = a + b + c + d"))
        self.label_24.setText(_translate("MainWindow", "ფართობი = ((a+b) / n) * h"))
        self.label_31.setText(_translate("MainWindow", "III გვერდი"))
        self.label_32.setText(_translate("MainWindow", "IV გვერდი"))
        self.label_34.setText(_translate("MainWindow", "სიმაღლე"))
        self.label_26.setText(_translate("MainWindow", "გვერდი"))
        self.label_27.setText(_translate("MainWindow", "ფართობი"))
        self.label_28.setText(_translate("MainWindow", "პერიმეტრი"))
        self.label_29.setText(_translate("MainWindow", "პარამეტრი = 4a"))
        self.label_30.setText(_translate("MainWindow", "ფართობი = a^2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
