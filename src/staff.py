from PySide6 import QtCore, QtWidgets, QtPrintSupport, QtGui
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QApplication, QMainWindow

from src.UI.ui_staff import Ui_MainWindow
from src.UI.ui_popup import Dialog
from src.sql_connector import sql_connection


class Staff(QMainWindow):

    idTransaksi = 0
    idPromosi = 0
    totalHargaPesanan = 0
    discount = 0
    ppn = 0
    totalHarga = 0

    def __init__(self):
        super(Staff, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: Staff.toggle_menu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE Buat Pesanan
        self.ui.btn_inputPesanan.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.buatPesanan))
        self.ui.btn_buatPesanan.clicked.connect(self.buat_pesanan)

        # PAGE Input Pesanan
        self.ui.btn_buatPesanan.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.inputPesanan))
        self.ui.btn_buatPesanan.clicked.connect(self.load_pilih_produk)
        self.ui.tableWidgetPilihProduk.cellDoubleClicked.connect(self.selectedCellProduk)
        self.ui.tableWidgetPilihProduk.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableWidgetPilihProduk.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.btn_inputProduk.clicked.connect(self.input_produk)
        self.ui.btn_inputProduk.clicked.connect(self.load_pesanan)

        # PAGE Transaksi
        self.ui.btn_lakukanTransaksi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.transaksi))
        self.ui.btn_lakukanTransaksi.clicked.connect(self.load_transaksi)
        self.ui.comboBox.activated.connect(self.hitung_promosi)
        self.ui.comboBox.activated.connect(self.hitung_ppn)
        self.ui.btn_totalHarga.clicked.connect(self.hitung_totalHarga)
        self.ui.btn_bayar.clicked.connect(self.bayar_transaksi)
        self.ui.btn_bayar.clicked.connect(self.hitung_kembalian)

        # PAGE Cetak Transaksi
        self.ui.btn_cetak.clicked.connect(self.handlePreview)
        self.ui.btn_cetak.clicked.connect(self.handlePrint)
        self.ui.btn_selesai.clicked.connect(self.clear_transaksi)
        self.ui.btn_selesai.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.buatPesanan))

        # PAGE Cek Stok
        self.ui.btn_cekStok.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cekStok))
        self.ui.btn_showData.clicked.connect(self.load_produk)
        self.ui.btn_update.clicked.connect(self.update_produk)
        self.ui.tableWidgetProduk.cellDoubleClicked.connect(self.selectedCell)
        self.ui.tableWidgetProduk.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableWidgetProduk.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def toggle_menu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def load_produk(self):
        query = "SELECT IDProduk, NamaProduk, Stok FROM produk"
        connection = sql_connection()
        cur = connection.cursor()
        try:
            cur.execute(query)
            result = cur.fetchall()
            self.ui.tableWidgetProduk.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidgetProduk.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidgetProduk.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                cur.close()
            return "Load Stok Success"
        except:
            return "Load Stok Failed"

    def update_produk(self):
        connection = sql_connection()
        cur = connection.cursor()
        namaProduk = self.ui.lineEditNamaProduk.text()
        stok = self.ui.lineEditStok.text()
        query = "UPDATE produk SET Stok= %s WHERE NamaProduk = %s"
        values = (stok, namaProduk)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Update Stok Success")
            dialog.show()
            dialog.exec()
            print("Update Stok Success")
            return "Update Stok Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Update Stok Failed")
            dialog.show()
            dialog.exec()
            print("Update Stok Failed")
            return "Update Stok Failed"

    def selectedCell(self):
        connection = sql_connection()
        cur = connection.cursor()

        self.index = self.ui.tableWidgetProduk.selectedItems()

        query = "SELECT IDProduk, NamaProduk, Stok FROM produk WHERE IDProduk = %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.ui.lineEditNamaProduk.setText(row[1])
                self.ui.lineEditStok.setText(str(row[2]))
        except:
            print("Fill Failed")

    def load_pilih_produk(self):
        query = "SELECT * FROM produk"
        connection = sql_connection()
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.ui.tableWidgetPilihProduk.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidgetPilihProduk.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidgetPilihProduk.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()

    def selectedCellProduk(self):
        connection = sql_connection()
        cur = connection.cursor()

        self.index = self.ui.tableWidgetPilihProduk.selectedItems()

        query = "SELECT NamaProduk FROM produk WHERE IDProduk = %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.ui.lineEditPilihProduk.setText(row[0])
        except:
            print("Fill Failed")

    def buat_pesanan(self):
        connection = sql_connection()
        cur = connection.cursor()

        idAnggota = self.ui.labelIDAnggota.text()

        query1 = "INSERT INTO transaksi (IDAnggota) VALUES (%s)"
        value1 = (idAnggota,)

        try:
            cur.execute(query1, value1)
            connection.commit()
            print("Success")
        except:
            print("failed")

        query2 = "SELECT MAX(IDTransaksi) FROM transaksi"

        try:
            cur.execute(query2)
            result = cur.fetchone()
            self.idTransaksi = result[0]
            print("Buat Pesanan Success")
            return "Buat Pesanan Success"
        except:
            print("Buat Pesanan Failed")
            return "Buat Pesanan Failed"


    def input_produk(self):
        connection = sql_connection()
        cur = connection.cursor()

        pilihProduk = self.ui.lineEditPilihProduk.text()
        kuantitas = self.ui.spinBoxKuantitas.value()
        idTransaksi = self.idTransaksi
        idProduk = ""
        hargaProduk = ""
        stok = 0

        query1 = "SELECT IDProduk, HargaProduk, Stok FROM produk where NamaProduk = %s"
        value1 = (pilihProduk,)

        if (pilihProduk == "" or kuantitas == 0):
            dialog = Dialog()
            dialog.ui.label.setText("Isi Nama Produk dan Kuantitas")
            dialog.show()
            dialog.exec()
        else:
            try:
                cur.execute(query1, value1)
                result = cur.fetchone()
                idProduk = result[0]
                hargaProduk = result[1]
                stok = result[2]
                print("Success")
            except:
                print("Failed")

            if (stok >= kuantitas):
                harga = hargaProduk * kuantitas
                stok = stok - kuantitas

                query2 = "INSERT INTO pesanan (IDTransaksi, IDProduk, Kuantitas, Harga) VALUES (%s, %s, %s, %s)"
                value2 = (idTransaksi,idProduk,kuantitas,harga)
                query3 = "UPDATE produk SET Stok= %s WHERE IDProduk = %s"
                value3 = (stok, idProduk,)

                try:
                    cur.execute(query2, value2)
                    connection.commit()
                    cur.execute(query3, value3)
                    connection.commit()
                    print("Input Pesanan Success")
                    return "Input Pesanan Success"
                except:
                    print("Input Pesanan Failed")
                    return "Input Pesanan Failed"
            else:
                dialog = Dialog()
                dialog.ui.label.setText("Stok Tidak Cukup, Silahkan Isi Stok!")
                dialog.show()
                dialog.exec()
                print("Input Pesanan Failed")
                return "Input Pesanan Failed"

    def load_pesanan(self):
        query = "SELECT IDTransaksi, NomorPesanan, NamaProduk, Kuantitas, Harga FROM pesanan JOIN produk WHERE pesanan.IDProduk = produk.IDProduk AND pesanan.IDTransaksi = %s"
        value = (self.idTransaksi,)
        connection = sql_connection()
        cur = connection.cursor()
        cur.execute(query, value)
        result = cur.fetchall()
        self.ui.tableWidgetInputPesanan.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidgetInputPesanan.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidgetInputPesanan.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            cur.close()

    def load_transaksi(self):
        query = "SELECT NamaProduk, Kuantitas, Harga FROM pesanan JOIN produk WHERE pesanan.IDProduk = produk.IDProduk AND pesanan.IDTransaksi = %s"
        query2 = "SELECT NamaPromosi FROM promosi"
        value = (self.idTransaksi,)
        connection = sql_connection()
        cur = connection.cursor()
        self.ui.comboBox.clear()
        try:
            cur.execute(query2)
            result2 = cur.fetchall()
            for row_number, row_data in enumerate(result2):
                for column_number, data in enumerate(row_data):
                    self.ui.comboBox.addItem(str(data))
        except:
            print("failed")
        try:
            cur.execute(query, value)
            result = cur.fetchall()
            self.ui.tableWidgetTransaksi.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidgetTransaksi.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidgetTransaksi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    if column_number == 2:
                        self.totalHargaPesanan += int(data)
                cur.close()
            showTotalHargaPesanan = "{:,}".format(self.totalHargaPesanan)
            self.ui.labelTotalHargaPesanan.setText("Rp"+showTotalHargaPesanan+".00")
            self.hitung_promosi()
            self.hitung_ppn()
            return "Load Transaksi Success"
        except:
            return "Load Transaksi Failed"

    def hitung_promosi(self):
        namaPromosi = self.ui.comboBox.currentText()
        query1 = "SELECT idPromosi, JumlahPromosi FROM promosi WHERE NamaPromosi = %s"
        value1 = (namaPromosi,)
        connection = sql_connection()
        cur = connection.cursor()
        try:
            cur.execute(query1,value1)
            result = cur.fetchone()
            self.idPromosi = int(result[0])
            self.discount = int(self.totalHargaPesanan * result[1])
            showDiscount = "{:,}".format(self.discount)
            self.ui.labelDiscount.setText("Rp" + showDiscount + ".00")
        except:
            print("failed")

    def hitung_ppn(self):
        self.ppn = int((self.totalHargaPesanan - self.discount) * 0.1)
        showPPn = "{:,}".format(self.ppn)
        self.ui.labelPPN.setText("Rp" + showPPn + ".00")

    def hitung_totalHarga(self):
        self.hitung_promosi()
        self.hitung_ppn()
        self.totalHarga = self.totalHargaPesanan - self.discount + self.ppn
        showTotalHarga = "{:,}".format(self.totalHarga)
        self.ui.labelTotalHarga.setText("Rp" + showTotalHarga + ".00")

    def hitung_kembalian(self):
        bayar = int(self.ui.lineEditBayar.text())
        if self.totalHarga <= bayar:
            kembalian = bayar - self.totalHarga
            showKembalian = "{:,}".format(kembalian)
            self.ui.labelKembalian.setText("Rp" + showKembalian + ".00")
        else:
            dialog = Dialog()
            dialog.ui.label.setText("Uang Pembayaran Tidak Cukup")
            dialog.show()
            dialog.exec()

    def bayar_transaksi(self):
        connection = sql_connection()
        cur = connection.cursor()
        query = "UPDATE transaksi SET IDPromosi = %s, TotalHarga = %s WHERE IDTransaksi = %s"
        values = (self.idPromosi, self.totalHarga, self.idTransaksi)

        try:
            cur.execute(query, values)
            connection.commit()
            print("Pembayaran Success")
            return "Pembayaran Success"
        except:
            print("Pembayaran Failed")
            return "Pembayaran Failed"

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        query = "SELECT Tanggal FROM transaksi WHERE IDTransaksi = %s"
        value = (self.idTransaksi,)
        connection = sql_connection()
        cur = connection.cursor()
        cur.execute(query, value)
        result = cur.fetchone()
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        cursor.beginEditBlock()
        cursor.insertText("Transaksi\n")
        cursor.insertText("ID Transaksi: " + str(self.idTransaksi) +"\n")
        cursor.insertText("Nama Anggota: " + self.ui.labelNamaAnggota.text() +"\n")
        cursor.insertText("Tanggal: " + str(result[0]) +"\n")
        cursor.insertText("Nama Produk | Kuantitas | Harga\n")
        cursor.endEditBlock()
        table = cursor.insertTable(
            self.ui.tableWidgetTransaksi.rowCount(), self.ui.tableWidgetTransaksi.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.ui.tableWidgetTransaksi.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        cursor.movePosition(QtGui.QTextCursor.NextBlock)
        cursor.beginEditBlock()
        cursor.insertText("Total Harga Pesanan: " + self.ui.labelTotalHargaPesanan.text()+"\n")
        cursor.insertText("Discount: " + self.ui.labelDiscount.text()+"\n")
        cursor.insertText("PPn: " + self.ui.labelPPN.text()+"\n")
        cursor.insertText("Total Harga: " + self.ui.labelTotalHarga.text()+"\n")
        cursor.insertText("Bayar: " + self.ui.lineEditBayar.text()+"\n")
        cursor.insertText("Kembalian: " + self.ui.labelKembalian.text()+"\n")
        cursor.endEditBlock()
        document.print_(printer)

    def clear_transaksi(self):
        self.totalHarga = 0
        self.idTransaksi = 0
        self.idPromosi = 0
        self.discount = 0
        self.ppn = 0
        self.totalHargaPesanan = 0
        self.ui.lineEditNamaProduk.clear()
        self.ui.lineEditPilihProduk.clear()
        self.ui.spinBoxKuantitas.clear()
        self.ui.tableWidgetInputPesanan.clearContents()
        self.ui.labelTotalHarga.setText("Rp0.00")
        self.ui.labelTotalHargaPesanan.setText("Rp0.00")
        self.ui.labelDiscount.setText("Rp0.00")
        self.ui.labelPPN.setText("Rp0.00")
        self.ui.labelKembalian.setText("Rp0.00")
        self.ui.lineEditBayar.clear()

