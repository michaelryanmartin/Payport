from PySide6 import QtCore, QtWidgets, QtPrintSupport, QtGui
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QApplication, QMainWindow

from src.UI.ui_owner import Ui_MainWindow
from src.UI.ui_popup import Dialog
from src.sql_connector import sql_connection

class Owner(QMainWindow):
    def __init__(self):
        super(Owner, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: Owner.toggle_menu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE Laporan Harian
        self.ui.btn_laporanHarian.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.laporanHarian))
        self.ui.btn_tampilHarian.clicked.connect(self.laporan_harian)
        self.ui.btn_unduhHarian.clicked.connect(self.handlePreviewHarian)
        self.ui.btn_unduhHarian.clicked.connect(self.handlePrintHarian)

        # PAGE Laporan Bulanan
        self.ui.btn_laporanBulanan.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.laporanBulanan))
        self.ui.btn_tampilBulanan.clicked.connect(self.laporan_bulanan)
        self.ui.btn_unduhBulanan.clicked.connect(self.handlePreviewBulanan)
        self.ui.btn_unduhBulanan.clicked.connect(self.handlePrintBulanan)

        # PAGE Edit Anggota
        self.ui.btn_editData.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.editAnggota))
        self.ui.btn_showData.clicked.connect(self.load_anggota)
        self.ui.btn_add.clicked.connect(self.add_anggota)
        self.ui.btn_delete.clicked.connect(self.delete_anggota)
        self.ui.btn_update.clicked.connect(self.update_anggota)
        self.ui.tableWidgetAnggota.cellDoubleClicked.connect(self.selectedCell)
        self.ui.tableWidgetAnggota.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableWidgetAnggota.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # PAGE Edit Produk
        self.ui.btn_editProduk.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.editProduk))
        self.ui.btn_showDataProduk.clicked.connect(self.load_produk)
        self.ui.btn_addProduk.clicked.connect(self.add_produk)
        self.ui.btn_deleteProduk.clicked.connect(self.delete_produk)
        self.ui.btn_updateProduk.clicked.connect(self.update_produk)
        self.ui.tableWidgetProduk.cellDoubleClicked.connect(self.selectedCellProduk)
        self.ui.tableWidgetProduk.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableWidgetProduk.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # PAGE Edit Promosi
        self.ui.btn_editPromosi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.editPromosi))
        self.ui.btn_showDataPromosi.clicked.connect(self.load_promosi)
        self.ui.btn_addPromosi.clicked.connect(self.add_promosi)
        self.ui.btn_deletePromosi.clicked.connect(self.delete_promosi)
        self.ui.btn_updatePromosi.clicked.connect(self.update_promosi)
        self.ui.tableWidgetPromosi.cellDoubleClicked.connect(self.selectedCellPromosi)
        self.ui.tableWidgetPromosi.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableWidgetPromosi.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

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

    def load_anggota(self):
        connection = sql_connection()
        query = "SELECT * FROM anggota"
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.ui.tableWidgetAnggota.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidgetAnggota.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidgetAnggota.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            cur.close()

    def add_anggota(self):
        connection = sql_connection()

        namaAnggota = self.ui.lineEditNamaAnggota.text()
        tipeAnggota = self.ui.comboBoxTipeAnggota.currentText()
        username = self.ui.lineEditUsername.text()
        password = self.ui.lineEditPassword.text()
        cur = connection.cursor()

        query = "INSERT INTO anggota (NamaAnggota, TipeAnggota, Username, Password) VALUES (%s, %s, %s, %s)"
        values = (namaAnggota, tipeAnggota, username, password)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Add Data Anggota Success")
            dialog.show()
            dialog.exec()
            print("Add Data Anggota Success")
            return "Add Data Anggota Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Add Data Anggota Failed")
            dialog.show()
            dialog.exec()
            print("Add Data Anggota Failed")
            return "Add Data Anggota Failed"

    def delete_anggota(self):
        connection = sql_connection()
        cur = connection.cursor()
        namaAnggota = self.ui.lineEditNamaAnggota.text()
        query = "DELETE FROM anggota WHERE namaAnggota = %s"
        values = (namaAnggota,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Delete Data Anggota Success")
            dialog.show()
            dialog.exec()
            print("Delete Data Anggota Success")
            return "Delete Data Anggota Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Delete Data Anggota Failed")
            dialog.show()
            dialog.exec()
            print("Delete Data Anggota Failed")
            return "Delete Data Anggota Failed"

    def update_anggota(self):
        connection = sql_connection()

        cur = connection.cursor()
        namaAnggota = self.ui.lineEditNamaAnggota.text()
        tipeAnggota = self.ui.comboBoxTipeAnggota.currentText()
        username = self.ui.lineEditUsername.text()
        password = self.ui.lineEditPassword.text()
        query = "UPDATE anggota SET TipeAnggota = %s, Username = %s, Password = %s WHERE NamaAnggota = %s"
        values = (tipeAnggota, username, password, namaAnggota)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Update Data Anggota Success")
            dialog.show()
            dialog.exec()
            print("Update Data Anggota Success")
            return "Update Data Anggota Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Update Data Anggota Failed")
            dialog.show()
            dialog.exec()
            print("Update Data Anggota Failed")
            return "Update Data Anggota Failed"

    def selectedCell(self):
        connection = sql_connection()

        cur = connection.cursor()

        self.index = self.ui.tableWidgetAnggota.selectedItems()

        query = "SELECT IDAnggota, NamaAnggota, TipeAnggota, Username, Password FROM anggota WHERE IDAnggota = %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.ui.lineEditNamaAnggota.setText(row[1])
                self.ui.lineEditUsername.setText(row[3])
                self.ui.lineEditPassword.setText(row[4])
        except:
            print("Fill Failed")
    
    def load_produk(self):
        connection = sql_connection()
        query = "SELECT * FROM produk"
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.ui.tableWidgetProduk.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidgetProduk.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidgetProduk.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            cur.close()

    def add_produk(self):
        connection = sql_connection()

        namaProduk = self.ui.lineEditNamaProduk.text()
        deskripsi = self.ui.lineEditDeskripsi.text()
        hargaProduk = self.ui.lineEditHarga.text()
        stok = self.ui.lineEditStok.text()
        cur = connection.cursor()

        query = "INSERT INTO produk (NamaProduk, Deskripsi, HargaProduk, Stok) VALUES (%s, %s, %s, %s)"
        values = (namaProduk, deskripsi, hargaProduk, stok,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Add Data Produk Success")
            dialog.show()
            dialog.exec()
            print("Add Data Produk Success")
            return "Add Data Produk Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Add Data Produk Failed")
            dialog.show()
            dialog.exec()
            print("Add Data Produk Failed")
            return "Add Data Produk Failed"

    def delete_produk(self):
        connection = sql_connection()
        cur = connection.cursor()
        namaProduk = self.ui.lineEditNamaProduk.text()
        query = "DELETE FROM produk WHERE namaProduk = %s"
        values = (namaProduk,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Delete Data Produk Success")
            dialog.show()
            dialog.exec()
            print("Delete Data Produk Success")
            return "Delete Data Produk Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Delete Data Produk Failed")
            dialog.show()
            dialog.exec()
            print("Delete Data Produk Failed")
            return "Delete Data Produk Failed"

    def update_produk(self):
        connection = sql_connection()

        cur = connection.cursor()
        namaProduk = self.ui.lineEditNamaProduk.text()
        deskripsi = self.ui.lineEditDeskripsi.text()
        hargaProduk = self.ui.lineEditHarga.text()
        stok = self.ui.lineEditStok.text()
        query = "UPDATE produk SET Deskripsi = %s, HargaProduk = %s, Stok = %s WHERE NamaProduk = %s"
        values = (deskripsi, hargaProduk, stok, namaProduk,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Update Data Produk Success")
            dialog.show()
            dialog.exec()
            print("Update Data Produk Success")
            return "Update Data Produk Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Update Data Produk Failed")
            dialog.show()
            dialog.exec()
            print("Update Data Produk Failed")
            return "Update Data Produk Failed"

    def selectedCellProduk(self):
        connection = sql_connection()

        cur = connection.cursor()

        self.index = self.ui.tableWidgetProduk.selectedItems()

        query = "SELECT IDProduk, NamaProduk, Deskripsi, HargaProduk, Stok FROM produk WHERE IDProduk= %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.ui.lineEditNamaProduk.setText(row[1])
                self.ui.lineEditDeskripsi.setText(row[2])
                self.ui.lineEditHarga.setText(str(row[3]))
                self.ui.lineEditStok.setText(str(row[4]))
        except:
            print("Fill Failed")

    def load_promosi(self):
        connection = sql_connection()
        query = "SELECT * FROM promosi"
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.ui.tableWidgetPromosi.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidgetPromosi.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidgetPromosi.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            cur.close()

    def add_promosi(self):
        connection = sql_connection()

        namaPromosi = self.ui.lineEditNamaPromosi.text()
        jumlahPromosi = self.ui.lineEditJumlahPromosi.text()
        cur = connection.cursor()

        query = "INSERT INTO promosi (NamaPromosi, JumlahPromosi) VALUES (%s, %s)"
        values = (namaPromosi, jumlahPromosi,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Add Data Promosi Success")
            dialog.show()
            dialog.exec()
            print("Add Data Promosi Success")
            return "Add Data Promosi Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Add Data Promosi Failed")
            dialog.show()
            dialog.exec()
            print("Add Data Promosi Failed")
            return "Add Data Promosi Failed"

    def delete_promosi(self):
        connection = sql_connection()
        cur = connection.cursor()
        namaPromosi = self.ui.lineEditNamaPromosi.text()
        query = "DELETE FROM promosi WHERE namaPromosi = %s"
        values = (namaPromosi,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Delete Data Promosi Success")
            dialog.show()
            dialog.exec()
            print("Delete Data Promosi Success")
            return "Delete Data Promosi Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Delete Data Promosi Failed")
            dialog.show()
            dialog.exec()
            print("Delete Data Promosi Failed")
            return "Delete Data Promosi Failed"

    def update_promosi(self):
        connection = sql_connection()

        cur = connection.cursor()
        namaPromosi = self.ui.lineEditNamaPromosi.text()
        jumlahPromosi = self.ui.lineEditJumlahPromosi.text()
        query = "UPDATE promosi SET jumlahPromosi = %s WHERE NamaPromosi = %s"
        values = (jumlahPromosi, namaPromosi,)

        try:
            cur.execute(query, values)
            connection.commit()
            dialog = Dialog()
            dialog.ui.label.setText("Update Data Promosi Success")
            dialog.show()
            dialog.exec()
            print("Update Data Promosi Success")
            return "Update Data Promosi Success"
        except:
            dialog = Dialog()
            dialog.ui.label.setText("Update Data Promosi Failed")
            dialog.show()
            dialog.exec()
            print("Update Data Promosi Failed")
            return "Update Data Promosi Failed"

    def selectedCellPromosi(self):
        connection = sql_connection()

        cur = connection.cursor()

        self.index = self.ui.tableWidgetPromosi.selectedItems()

        query = "SELECT IDPromosi, NamaPromosi, JumlahPromosi FROM promosi WHERE IDPromosi= %s"
        value = (self.index[0].text(),)

        try:
            cur.execute(query, value)
            row = cur.fetchone()

            if row:
                self.ui.lineEditNamaPromosi.setText(row[1])
                self.ui.lineEditJumlahPromosi.setText(str(row[2]))
        except:
            print("Fill Failed")

    def laporan_bulanan(self):
        connection = sql_connection()

        bulan = self.ui.lineEditBulan.text()
        tahun = self.ui.lineEditTahun.text()
        grandTotal = 0

        query = "SELECT Tanggal, COUNT(IDTransaksi) AS JumlahTransaksi, SUM(TotalHarga) AS TotalHarga FROM Transaksi WHERE MONTH(Tanggal) = %s AND YEAR(Tanggal) = %s GROUP BY Tanggal"
        value = (bulan, tahun,)
        cur = connection.cursor()
        try:
            cur.execute(query, value)
            result = cur.fetchall()
            self.ui.tableWidgetBulanan.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidgetBulanan.insertRow(row_number)
                grandTotal += int(row_data[2])
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidgetBulanan.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                cur.close()
            showGrandTotal = "{:,}".format(grandTotal)
            self.ui.labelGrandTotalBulanan.setText("Rp" + showGrandTotal + ".00")
            return "Laporan Bulanan Success"
        except:
            return "Laporan Bulanan Failed"

    def laporan_harian(self):
        connection = sql_connection()

        tanggal = self.ui.dateEditHarian.text()
        grandTotal = 0

        query = "SELECT IDTransaksi, Tanggal, NamaAnggota, NamaPromosi, TotalHarga FROM transaksi JOIN anggota JOIN promosi WHERE transaksi.IDAnggota=anggota.IDAnggota AND transaksi.IDPromosi=promosi.IDPromosi AND Tanggal = %s"
        value = (tanggal,)
        cur = connection.cursor()
        try:
            cur.execute(query, value)
            result = cur.fetchall()
            self.ui.tableWidgetHarian.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidgetHarian.insertRow(row_number)
                grandTotal += int(row_data[4])
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidgetHarian.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                cur.close()
            showGrandTotal = "{:,}".format(grandTotal)
            self.ui.labelGrandTotalHarian.setText("Rp" + showGrandTotal + ".00")
            return "Laporan Harian Success"
        except:
            return "Laporan Harian Failed"

    def handlePrintHarian(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequestHarian(dialog.printer())

    def handlePreviewHarian(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequestHarian)
        dialog.exec_()

    def handlePaintRequestHarian(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        cursor.beginEditBlock()
        cursor.insertText("PAYPORT\n")
        cursor.insertText("Laporan Harian\n")
        cursor.insertText("Tanggal: " + self.ui.dateEditHarian.text() +"\n")
        cursor.insertText("IDTransaksi | Tanggal | Nama Anggota | Nama Promosi | Total Harga\n")
        cursor.endEditBlock()
        table = cursor.insertTable(
            self.ui.tableWidgetHarian.rowCount(), self.ui.tableWidgetHarian.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.ui.tableWidgetHarian.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        cursor.movePosition(QtGui.QTextCursor.NextBlock)
        cursor.beginEditBlock()
        cursor.insertText("Grand Total: " + self.ui.labelGrandTotalHarian.text() + "\n")
        cursor.endEditBlock()
        document.print_(printer)

    def handlePrintBulanan(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequestBulanan(dialog.printer())

    def handlePreviewBulanan(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequestBulanan)
        dialog.exec_()

    def handlePaintRequestBulanan(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        cursor.beginEditBlock()
        cursor.insertText("PAYPORT\n")
        cursor.insertText("Laporan Bulanan\n")
        cursor.insertText("Bulan: " + self.ui.lineEditBulan.text() +"\n")
        cursor.insertText("Tahun: " + self.ui.lineEditTahun.text() + "\n")
        cursor.insertText("Tanggal | Jumlah Transaksi | Total Harga\n")
        cursor.endEditBlock()
        table = cursor.insertTable(
            self.ui.tableWidgetBulanan.rowCount(), self.ui.tableWidgetBulanan.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.ui.tableWidgetBulanan.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        cursor.movePosition(QtGui.QTextCursor.NextBlock)
        cursor.beginEditBlock()
        cursor.insertText("Grand Total: " + self.ui.labelGrandTotalBulanan.text() + "\n")
        cursor.endEditBlock()
        document.print_(printer)



        
