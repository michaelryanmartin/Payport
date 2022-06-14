# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_owner.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 533)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.frame_top)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(71, 20))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.labelIDAnggota = QLabel(self.frame_top)
        self.labelIDAnggota.setObjectName(u"labelIDAnggota")
        self.labelIDAnggota.setStyleSheet(u"color: white\n"
"")

        self.horizontalLayout_3.addWidget(self.labelIDAnggota)

        self.label_9 = QLabel(self.frame_top)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(71, 20))
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.labelNamaAnggota = QLabel(self.frame_top)
        self.labelNamaAnggota.setObjectName(u"labelNamaAnggota")
        self.labelNamaAnggota.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_3.addWidget(self.labelNamaAnggota)

        self.label_5 = QLabel(self.frame_top)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(71, 20))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.labelTipeAnggota = QLabel(self.frame_top)
        self.labelTipeAnggota.setObjectName(u"labelTipeAnggota")
        self.labelTipeAnggota.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_3.addWidget(self.labelTipeAnggota)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_laporanHarian = QPushButton(self.frame_top_menus)
        self.btn_laporanHarian.setObjectName(u"btn_laporanHarian")
        self.btn_laporanHarian.setMinimumSize(QSize(0, 40))
        self.btn_laporanHarian.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_laporanHarian)

        self.btn_laporanBulanan = QPushButton(self.frame_top_menus)
        self.btn_laporanBulanan.setObjectName(u"btn_laporanBulanan")
        self.btn_laporanBulanan.setMinimumSize(QSize(0, 40))
        self.btn_laporanBulanan.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_laporanBulanan)

        self.btn_editData = QPushButton(self.frame_top_menus)
        self.btn_editData.setObjectName(u"btn_editData")
        self.btn_editData.setMinimumSize(QSize(0, 40))
        self.btn_editData.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_editData)

        self.btn_editProduk = QPushButton(self.frame_top_menus)
        self.btn_editProduk.setObjectName(u"btn_editProduk")
        self.btn_editProduk.setMinimumSize(QSize(0, 40))
        self.btn_editProduk.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_editProduk)

        self.btn_editPromosi = QPushButton(self.frame_top_menus)
        self.btn_editPromosi.setObjectName(u"btn_editPromosi")
        self.btn_editPromosi.setMinimumSize(QSize(0, 40))
        self.btn_editPromosi.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_editPromosi)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.btn_logOut = QPushButton(self.frame_left_menu)
        self.btn_logOut.setObjectName(u"btn_logOut")
        self.btn_logOut.setMinimumSize(QSize(0, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(35, 35, 35, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.btn_logOut.setPalette(palette)
        self.btn_logOut.setMouseTracking(True)
        self.btn_logOut.setAutoFillBackground(False)
        self.btn_logOut.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_logOut)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.laporanHarian = QWidget()
        self.laporanHarian.setObjectName(u"laporanHarian")
        self.laporanHarian.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_7 = QVBoxLayout(self.laporanHarian)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.laporanHarian)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.laporanHarian)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.dateEditHarian = QDateEdit(self.laporanHarian)
        self.dateEditHarian.setObjectName(u"dateEditHarian")
        self.dateEditHarian.setCurrentSection(QDateTimeEdit.YearSection)

        self.horizontalLayout_10.addWidget(self.dateEditHarian)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.tableWidgetHarian = QTableWidget(self.laporanHarian)
        if (self.tableWidgetHarian.columnCount() < 5):
            self.tableWidgetHarian.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetHarian.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetHarian.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetHarian.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetHarian.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetHarian.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidgetHarian.setObjectName(u"tableWidgetHarian")

        self.verticalLayout_7.addWidget(self.tableWidgetHarian)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.laporanHarian)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.labelGrandTotalHarian = QLabel(self.laporanHarian)
        self.labelGrandTotalHarian.setObjectName(u"labelGrandTotalHarian")

        self.horizontalLayout_11.addWidget(self.labelGrandTotalHarian)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.btn_tampilHarian = QPushButton(self.laporanHarian)
        self.btn_tampilHarian.setObjectName(u"btn_tampilHarian")

        self.verticalLayout_7.addWidget(self.btn_tampilHarian)

        self.btn_unduhHarian = QPushButton(self.laporanHarian)
        self.btn_unduhHarian.setObjectName(u"btn_unduhHarian")

        self.verticalLayout_7.addWidget(self.btn_unduhHarian)

        self.stackedWidget.addWidget(self.laporanHarian)
        self.laporanBulanan = QWidget()
        self.laporanBulanan.setObjectName(u"laporanBulanan")
        self.laporanBulanan.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayout_6 = QVBoxLayout(self.laporanBulanan)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.laporanBulanan)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(25)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.laporanBulanan)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.lineEditBulan = QLineEdit(self.laporanBulanan)
        self.lineEditBulan.setObjectName(u"lineEditBulan")

        self.horizontalLayout_12.addWidget(self.lineEditBulan)

        self.label_23 = QLabel(self.laporanBulanan)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.lineEditTahun = QLineEdit(self.laporanBulanan)
        self.lineEditTahun.setObjectName(u"lineEditTahun")

        self.horizontalLayout_12.addWidget(self.lineEditTahun)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.tableWidgetBulanan = QTableWidget(self.laporanBulanan)
        if (self.tableWidgetBulanan.columnCount() < 3):
            self.tableWidgetBulanan.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetBulanan.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetBulanan.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetBulanan.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.tableWidgetBulanan.setObjectName(u"tableWidgetBulanan")

        self.verticalLayout_6.addWidget(self.tableWidgetBulanan)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.laporanBulanan)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.labelGrandTotalBulanan = QLabel(self.laporanBulanan)
        self.labelGrandTotalBulanan.setObjectName(u"labelGrandTotalBulanan")

        self.horizontalLayout_13.addWidget(self.labelGrandTotalBulanan)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.btn_tampilBulanan = QPushButton(self.laporanBulanan)
        self.btn_tampilBulanan.setObjectName(u"btn_tampilBulanan")

        self.verticalLayout_6.addWidget(self.btn_tampilBulanan)

        self.btn_unduhBulanan = QPushButton(self.laporanBulanan)
        self.btn_unduhBulanan.setObjectName(u"btn_unduhBulanan")

        self.verticalLayout_6.addWidget(self.btn_unduhBulanan)

        self.stackedWidget.addWidget(self.laporanBulanan)
        self.editAnggota = QWidget()
        self.editAnggota.setObjectName(u"editAnggota")
        self.editAnggota.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.verticalLayout_8 = QVBoxLayout(self.editAnggota)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.editAnggota)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidgetAnggota = QTableWidget(self.editAnggota)
        if (self.tableWidgetAnggota.columnCount() < 5):
            self.tableWidgetAnggota.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetAnggota.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetAnggota.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetAnggota.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetAnggota.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidgetAnggota.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        if (self.tableWidgetAnggota.rowCount() < 7):
            self.tableWidgetAnggota.setRowCount(7)
        self.tableWidgetAnggota.setObjectName(u"tableWidgetAnggota")
        self.tableWidgetAnggota.setRowCount(7)
        self.tableWidgetAnggota.setColumnCount(5)

        self.horizontalLayout_4.addWidget(self.tableWidgetAnggota)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.btn_showData = QPushButton(self.editAnggota)
        self.btn_showData.setObjectName(u"btn_showData")
        self.btn_showData.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_showData)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.editAnggota)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEditNamaAnggota = QLineEdit(self.editAnggota)
        self.lineEditNamaAnggota.setObjectName(u"lineEditNamaAnggota")
        self.lineEditNamaAnggota.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_5.addWidget(self.lineEditNamaAnggota)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.editAnggota)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMaximumSize(QSize(90, 16777215))
        self.label_7.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.comboBoxTipeAnggota = QComboBox(self.editAnggota)
        self.comboBoxTipeAnggota.addItem("")
        self.comboBoxTipeAnggota.addItem("")
        self.comboBoxTipeAnggota.setObjectName(u"comboBoxTipeAnggota")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxTipeAnggota.sizePolicy().hasHeightForWidth())
        self.comboBoxTipeAnggota.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setBold(False)
        self.comboBoxTipeAnggota.setFont(font)
        self.comboBoxTipeAnggota.setAutoFillBackground(False)
        self.comboBoxTipeAnggota.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.comboBoxTipeAnggota)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(41)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.editAnggota)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEditUsername = QLineEdit(self.editAnggota)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_7.addWidget(self.lineEditUsername)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(45)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.editAnggota)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEditPassword = QLineEdit(self.editAnggota)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.lineEditPassword)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_add = QPushButton(self.editAnggota)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_add)

        self.btn_update = QPushButton(self.editAnggota)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_update)

        self.btn_delete = QPushButton(self.editAnggota)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_delete)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.editAnggota)
        self.editProduk = QWidget()
        self.editProduk.setObjectName(u"editProduk")
        self.editProduk.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.verticalLayout_9 = QVBoxLayout(self.editProduk)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.editProduk)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.tableWidgetProduk = QTableWidget(self.editProduk)
        if (self.tableWidgetProduk.columnCount() < 5):
            self.tableWidgetProduk.setColumnCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        self.tableWidgetProduk.setObjectName(u"tableWidgetProduk")

        self.verticalLayout_9.addWidget(self.tableWidgetProduk)

        self.btn_showDataProduk = QPushButton(self.editProduk)
        self.btn_showDataProduk.setObjectName(u"btn_showDataProduk")
        self.btn_showDataProduk.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_showDataProduk)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.editProduk)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.lineEditNamaProduk = QLineEdit(self.editProduk)
        self.lineEditNamaProduk.setObjectName(u"lineEditNamaProduk")
        self.lineEditNamaProduk.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_14.addWidget(self.lineEditNamaProduk)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(47)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.editProduk)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMaximumSize(QSize(90, 16777215))
        self.label_17.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.lineEditDeskripsi = QLineEdit(self.editProduk)
        self.lineEditDeskripsi.setObjectName(u"lineEditDeskripsi")

        self.horizontalLayout_15.addWidget(self.lineEditDeskripsi)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(63)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.editProduk)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.label_19)

        self.lineEditHarga = QLineEdit(self.editProduk)
        self.lineEditHarga.setObjectName(u"lineEditHarga")
        self.lineEditHarga.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.lineEditHarga.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_17.addWidget(self.lineEditHarga)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(71)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.editProduk)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_18)

        self.lineEditStok = QLineEdit(self.editProduk)
        self.lineEditStok.setObjectName(u"lineEditStok")
        self.lineEditStok.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_16.addWidget(self.lineEditStok)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_addProduk = QPushButton(self.editProduk)
        self.btn_addProduk.setObjectName(u"btn_addProduk")
        self.btn_addProduk.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_addProduk)

        self.btn_updateProduk = QPushButton(self.editProduk)
        self.btn_updateProduk.setObjectName(u"btn_updateProduk")
        self.btn_updateProduk.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_updateProduk)

        self.btn_deleteProduk = QPushButton(self.editProduk)
        self.btn_deleteProduk.setObjectName(u"btn_deleteProduk")
        self.btn_deleteProduk.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_deleteProduk)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.editProduk)
        self.editPromosi = QWidget()
        self.editPromosi.setObjectName(u"editPromosi")
        self.editPromosi.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.verticalLayout_10 = QVBoxLayout(self.editPromosi)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_20 = QLabel(self.editPromosi)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_10.addWidget(self.label_20)

        self.tableWidgetPromosi = QTableWidget(self.editPromosi)
        if (self.tableWidgetPromosi.columnCount() < 3):
            self.tableWidgetPromosi.setColumnCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidgetPromosi.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidgetPromosi.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidgetPromosi.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        self.tableWidgetPromosi.setObjectName(u"tableWidgetPromosi")

        self.verticalLayout_10.addWidget(self.tableWidgetPromosi)

        self.btn_showDataPromosi = QPushButton(self.editPromosi)
        self.btn_showDataPromosi.setObjectName(u"btn_showDataPromosi")
        self.btn_showDataPromosi.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_showDataPromosi)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(27)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.editPromosi)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.label_21)

        self.lineEditNamaPromosi = QLineEdit(self.editPromosi)
        self.lineEditNamaPromosi.setObjectName(u"lineEditNamaPromosi")
        self.lineEditNamaPromosi.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_19.addWidget(self.lineEditNamaPromosi)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(22)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_22 = QLabel(self.editPromosi)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.label_22)

        self.lineEditJumlahPromosi = QLineEdit(self.editPromosi)
        self.lineEditJumlahPromosi.setObjectName(u"lineEditJumlahPromosi")
        self.lineEditJumlahPromosi.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_20.addWidget(self.lineEditJumlahPromosi)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_addPromosi = QPushButton(self.editPromosi)
        self.btn_addPromosi.setObjectName(u"btn_addPromosi")
        self.btn_addPromosi.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.btn_addPromosi)

        self.btn_updatePromosi = QPushButton(self.editPromosi)
        self.btn_updatePromosi.setObjectName(u"btn_updatePromosi")
        self.btn_updatePromosi.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.btn_updatePromosi)

        self.btn_deletePromosi = QPushButton(self.editPromosi)
        self.btn_deletePromosi.setObjectName(u"btn_deletePromosi")
        self.btn_deletePromosi.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.btn_deletePromosi)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.stackedWidget.addWidget(self.editPromosi)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"PayPort", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID Anggota: ", None))
        self.labelIDAnggota.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nama Anggota:", None))
        self.labelNamaAnggota.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tipe Anggota: ", None))
        self.labelTipeAnggota.setText("")
        self.btn_laporanHarian.setText(QCoreApplication.translate("MainWindow", u"Laporan\n"
"Harian", None))
        self.btn_laporanBulanan.setText(QCoreApplication.translate("MainWindow", u"Laporan\n"
"Bulanan", None))
        self.btn_editData.setText(QCoreApplication.translate("MainWindow", u"Edit\n"
"Anggota", None))
        self.btn_editProduk.setText(QCoreApplication.translate("MainWindow", u"Edit\n"
"Produk", None))
        self.btn_editPromosi.setText(QCoreApplication.translate("MainWindow", u"Edit\n"
"Promosi", None))
        self.btn_logOut.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Laporan Harian", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None))
        self.dateEditHarian.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-M-d", None))
        ___qtablewidgetitem = self.tableWidgetHarian.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IDTransaksi", None));
        ___qtablewidgetitem1 = self.tableWidgetHarian.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem2 = self.tableWidgetHarian.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama Anggota", None));
        ___qtablewidgetitem3 = self.tableWidgetHarian.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nama Promosi", None));
        ___qtablewidgetitem4 = self.tableWidgetHarian.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total Harga", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Grand Total", None))
        self.labelGrandTotalHarian.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.btn_tampilHarian.setText(QCoreApplication.translate("MainWindow", u"Tampilkan Laporan Harian", None))
        self.btn_unduhHarian.setText(QCoreApplication.translate("MainWindow", u"Unduh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Laporan Bulanan", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Bulan", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Tahun", None))
        ___qtablewidgetitem5 = self.tableWidgetBulanan.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem6 = self.tableWidgetBulanan.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Jumlah Transaksi", None));
        ___qtablewidgetitem7 = self.tableWidgetBulanan.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Total Harga", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Grand Total", None))
        self.labelGrandTotalBulanan.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.btn_tampilBulanan.setText(QCoreApplication.translate("MainWindow", u"Tampilkan Laporan Bulanan", None))
        self.btn_unduhBulanan.setText(QCoreApplication.translate("MainWindow", u"Unduh", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Anggota", None))
        ___qtablewidgetitem8 = self.tableWidgetAnggota.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"IDAnggota", None));
        ___qtablewidgetitem9 = self.tableWidgetAnggota.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"NamaAnggota", None));
        ___qtablewidgetitem10 = self.tableWidgetAnggota.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TipeAnggota", None));
        ___qtablewidgetitem11 = self.tableWidgetAnggota.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem12 = self.tableWidgetAnggota.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.btn_showData.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nama Anggota", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipe Anggota", None))
        self.comboBoxTipeAnggota.setItemText(0, QCoreApplication.translate("MainWindow", u"Staff", None))
        self.comboBoxTipeAnggota.setItemText(1, QCoreApplication.translate("MainWindow", u"Owner", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Data Produk", None))
        ___qtablewidgetitem13 = self.tableWidgetProduk.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"IDProduk", None));
        ___qtablewidgetitem14 = self.tableWidgetProduk.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None));
        ___qtablewidgetitem15 = self.tableWidgetProduk.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Deskripsi", None));
        ___qtablewidgetitem16 = self.tableWidgetProduk.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Harga Produk", None));
        ___qtablewidgetitem17 = self.tableWidgetProduk.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Stok", None));
        self.btn_showDataProduk.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Deskripsi", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Harga", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Stok", None))
        self.btn_addProduk.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_updateProduk.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_deleteProduk.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Data Promosi", None))
        ___qtablewidgetitem18 = self.tableWidgetPromosi.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"IDPromosi", None));
        ___qtablewidgetitem19 = self.tableWidgetPromosi.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Nama Promosi", None));
        ___qtablewidgetitem20 = self.tableWidgetPromosi.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Jumlah Promosi", None));
        self.btn_showDataPromosi.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nama Promosi", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Jumlah Promosi", None))
        self.btn_addPromosi.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_updatePromosi.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_deletePromosi.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

