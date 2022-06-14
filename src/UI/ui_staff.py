# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_staff.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
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
        self.btn_inputPesanan = QPushButton(self.frame_top_menus)
        self.btn_inputPesanan.setObjectName(u"btn_inputPesanan")
        self.btn_inputPesanan.setMinimumSize(QSize(0, 40))
        self.btn_inputPesanan.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_inputPesanan)

        self.btn_cekStok = QPushButton(self.frame_top_menus)
        self.btn_cekStok.setObjectName(u"btn_cekStok")
        self.btn_cekStok.setMinimumSize(QSize(0, 40))
        self.btn_cekStok.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_cekStok)


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
        self.buatPesanan = QWidget()
        self.buatPesanan.setObjectName(u"buatPesanan")
        self.buatPesanan.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.btn_buatPesanan = QPushButton(self.buatPesanan)
        self.btn_buatPesanan.setObjectName(u"btn_buatPesanan")
        self.btn_buatPesanan.setGeometry(QRect(300, 170, 311, 91))
        self.btn_buatPesanan.setStyleSheet(u"QPushButton	 {\n"
"	background-color: rgb(35,35,35);\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.stackedWidget.addWidget(self.buatPesanan)
        self.inputPesanan = QWidget()
        self.inputPesanan.setObjectName(u"inputPesanan")
        self.inputPesanan.setStyleSheet(u"background-color: rgb(255, 255, 255)\n"
"\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.inputPesanan)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.inputPesanan)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.tableWidgetPilihProduk = QTableWidget(self.inputPesanan)
        if (self.tableWidgetPilihProduk.columnCount() < 5):
            self.tableWidgetPilihProduk.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetPilihProduk.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetPilihProduk.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetPilihProduk.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetPilihProduk.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetPilihProduk.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidgetPilihProduk.setObjectName(u"tableWidgetPilihProduk")

        self.verticalLayout_7.addWidget(self.tableWidgetPilihProduk)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.inputPesanan)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.lineEditPilihProduk = QLineEdit(self.inputPesanan)
        self.lineEditPilihProduk.setObjectName(u"lineEditPilihProduk")
        sizePolicy1.setHeightForWidth(self.lineEditPilihProduk.sizePolicy().hasHeightForWidth())
        self.lineEditPilihProduk.setSizePolicy(sizePolicy1)
        self.lineEditPilihProduk.setMaximumSize(QSize(442, 21))

        self.horizontalLayout_9.addWidget(self.lineEditPilihProduk)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.inputPesanan)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.spinBoxKuantitas = QSpinBox(self.inputPesanan)
        self.spinBoxKuantitas.setObjectName(u"spinBoxKuantitas")

        self.horizontalLayout_7.addWidget(self.spinBoxKuantitas)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.btn_inputProduk = QPushButton(self.inputPesanan)
        self.btn_inputProduk.setObjectName(u"btn_inputProduk")
        self.btn_inputProduk.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_inputProduk)

        self.tableWidgetInputPesanan = QTableWidget(self.inputPesanan)
        if (self.tableWidgetInputPesanan.columnCount() < 5):
            self.tableWidgetInputPesanan.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetInputPesanan.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetInputPesanan.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetInputPesanan.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetInputPesanan.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetInputPesanan.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidgetInputPesanan.setObjectName(u"tableWidgetInputPesanan")

        self.verticalLayout_7.addWidget(self.tableWidgetInputPesanan)

        self.btn_lakukanTransaksi = QPushButton(self.inputPesanan)
        self.btn_lakukanTransaksi.setObjectName(u"btn_lakukanTransaksi")
        self.btn_lakukanTransaksi.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_lakukanTransaksi)

        self.stackedWidget.addWidget(self.inputPesanan)
        self.transaksi = QWidget()
        self.transaksi.setObjectName(u"transaksi")
        self.transaksi.setStyleSheet(u"background-color: white\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.transaksi)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.transaksi)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.tableWidgetTransaksi = QTableWidget(self.transaksi)
        if (self.tableWidgetTransaksi.columnCount() < 3):
            self.tableWidgetTransaksi.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetTransaksi.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetTransaksi.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidgetTransaksi.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.tableWidgetTransaksi.setObjectName(u"tableWidgetTransaksi")

        self.verticalLayout_6.addWidget(self.tableWidgetTransaksi)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.transaksi)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.labelTotalHargaPesanan = QLabel(self.transaksi)
        self.labelTotalHargaPesanan.setObjectName(u"labelTotalHargaPesanan")

        self.horizontalLayout_10.addWidget(self.labelTotalHargaPesanan)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.transaksi)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.comboBox = QComboBox(self.transaksi)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.transaksi)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.labelDiscount = QLabel(self.transaksi)
        self.labelDiscount.setObjectName(u"labelDiscount")

        self.horizontalLayout_11.addWidget(self.labelDiscount)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.transaksi)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_16.addWidget(self.label_17)

        self.labelPPN = QLabel(self.transaksi)
        self.labelPPN.setObjectName(u"labelPPN")

        self.horizontalLayout_16.addWidget(self.labelPPN)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.btn_totalHarga = QPushButton(self.transaksi)
        self.btn_totalHarga.setObjectName(u"btn_totalHarga")
        self.btn_totalHarga.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_totalHarga)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.transaksi)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.labelTotalHarga = QLabel(self.transaksi)
        self.labelTotalHarga.setObjectName(u"labelTotalHarga")

        self.horizontalLayout_13.addWidget(self.labelTotalHarga)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.transaksi)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(441, 16))

        self.horizontalLayout_12.addWidget(self.label_15)

        self.lineEditBayar = QLineEdit(self.transaksi)
        self.lineEditBayar.setObjectName(u"lineEditBayar")

        self.horizontalLayout_12.addWidget(self.lineEditBayar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.btn_bayar = QPushButton(self.transaksi)
        self.btn_bayar.setObjectName(u"btn_bayar")
        self.btn_bayar.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_bayar)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.transaksi)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.labelKembalian = QLabel(self.transaksi)
        self.labelKembalian.setObjectName(u"labelKembalian")

        self.horizontalLayout_15.addWidget(self.labelKembalian)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.btn_cetak = QPushButton(self.transaksi)
        self.btn_cetak.setObjectName(u"btn_cetak")
        self.btn_cetak.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_cetak)

        self.btn_selesai = QPushButton(self.transaksi)
        self.btn_selesai.setObjectName(u"btn_selesai")
        self.btn_selesai.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_selesai)

        self.stackedWidget.addWidget(self.transaksi)
        self.cekStok = QWidget()
        self.cekStok.setObjectName(u"cekStok")
        self.cekStok.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.verticalLayout_8 = QVBoxLayout(self.cekStok)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.cekStok)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidgetProduk = QTableWidget(self.cekStok)
        if (self.tableWidgetProduk.columnCount() < 3):
            self.tableWidgetProduk.setColumnCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidgetProduk.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        if (self.tableWidgetProduk.rowCount() < 7):
            self.tableWidgetProduk.setRowCount(7)
        self.tableWidgetProduk.setObjectName(u"tableWidgetProduk")
        self.tableWidgetProduk.setRowCount(7)
        self.tableWidgetProduk.setColumnCount(3)

        self.horizontalLayout_4.addWidget(self.tableWidgetProduk)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.btn_showData = QPushButton(self.cekStok)
        self.btn_showData.setObjectName(u"btn_showData")
        self.btn_showData.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_showData)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.cekStok)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEditNamaProduk = QLineEdit(self.cekStok)
        self.lineEditNamaProduk.setObjectName(u"lineEditNamaProduk")
        self.lineEditNamaProduk.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.horizontalLayout_5.addWidget(self.lineEditNamaProduk)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(63)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.cekStok)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEditStok = QLineEdit(self.cekStok)
        self.lineEditStok.setObjectName(u"lineEditStok")
        self.lineEditStok.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.lineEditStok.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_6.addWidget(self.lineEditStok)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_update = QPushButton(self.cekStok)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_update)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.cekStok)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.btn_inputPesanan.setText(QCoreApplication.translate("MainWindow", u"Input\n"
"Pesanan", None))
        self.btn_cekStok.setText(QCoreApplication.translate("MainWindow", u"Cek Stok", None))
        self.btn_logOut.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.btn_buatPesanan.setText(QCoreApplication.translate("MainWindow", u"Buat Pesanan", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input Pesanan", None))
        ___qtablewidgetitem = self.tableWidgetPilihProduk.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IDProduk", None));
        ___qtablewidgetitem1 = self.tableWidgetPilihProduk.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None));
        ___qtablewidgetitem2 = self.tableWidgetPilihProduk.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Deskripsi", None));
        ___qtablewidgetitem3 = self.tableWidgetPilihProduk.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Harga Produk", None));
        ___qtablewidgetitem4 = self.tableWidgetPilihProduk.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stok", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"NamaProduk", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kuantitas", None))
        self.btn_inputProduk.setText(QCoreApplication.translate("MainWindow", u"Input Produk", None))
        ___qtablewidgetitem5 = self.tableWidgetInputPesanan.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"IDTransaksi", None));
        ___qtablewidgetitem6 = self.tableWidgetInputPesanan.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NomorPesanan", None));
        ___qtablewidgetitem7 = self.tableWidgetInputPesanan.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NamaProduk", None));
        ___qtablewidgetitem8 = self.tableWidgetInputPesanan.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Kuantitas", None));
        ___qtablewidgetitem9 = self.tableWidgetInputPesanan.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Harga", None));
        self.btn_lakukanTransaksi.setText(QCoreApplication.translate("MainWindow", u"Lakukan Transaksi", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Transaksi", None))
        ___qtablewidgetitem10 = self.tableWidgetTransaksi.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NamaProduk", None));
        ___qtablewidgetitem11 = self.tableWidgetTransaksi.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Kuantitas", None));
        ___qtablewidgetitem12 = self.tableWidgetTransaksi.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Harga", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Total Harga Pesanan", None))
        self.labelTotalHargaPesanan.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pilih Discount", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.labelDiscount.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"PPn 10%", None))
        self.labelPPN.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.btn_totalHarga.setText(QCoreApplication.translate("MainWindow", u"Hitung Total Harga", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Total Harga", None))
        self.labelTotalHarga.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Bayar", None))
        self.btn_bayar.setText(QCoreApplication.translate("MainWindow", u"Bayar", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Kembalian", None))
        self.labelKembalian.setText(QCoreApplication.translate("MainWindow", u"Rp0.00", None))
        self.btn_cetak.setText(QCoreApplication.translate("MainWindow", u"Cetak", None))
        self.btn_selesai.setText(QCoreApplication.translate("MainWindow", u"Selesai", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Produk", None))
        ___qtablewidgetitem13 = self.tableWidgetProduk.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"IDProduk", None));
        ___qtablewidgetitem14 = self.tableWidgetProduk.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None));
        ___qtablewidgetitem15 = self.tableWidgetProduk.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Stok", None));
        self.btn_showData.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nama Produk", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stok", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

