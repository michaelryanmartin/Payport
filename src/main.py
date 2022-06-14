import sys

from PySide6.QtWidgets import QApplication, QWidget
from src.UI.ui_login import Ui_Form
from src.owner import Owner
from src.staff import Staff
from src.sql_connector import sql_connection


class Anggota(QWidget):
    idAnggota = ""
    namaAnggota = ""
    tipeAnggota = ""

    def __init__(self):
        super(Anggota, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonLogin.clicked.connect(self.login)
        self.show()

    def login(self):
        username = self.ui.lineEditUsername.text()
        password = self.ui.lineEditPassword.text()

        connection = sql_connection()
        cursor = connection.cursor()
        query = "SELECT IDAnggota, NamaAnggota, TipeAnggota, Username, Password FROM anggota WHERE Username LIKE '" + username + "'and Password LIKE '" + password + "'"
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except:
            print("failed")

        if result is None:
            self.ui.label_status.setText("Incorrect Username or Password")

        else:
            self.ui.label_status.setText("You are logged in")
            self.idAnggota = str(result[0])
            self.namaAnggota = result[1]
            self.tipeAnggota = result[2]
            try:
                if self.tipeAnggota == "Owner":
                    ownerwindow = Owner()
                    ownerwindow.ui.labelNamaAnggota.setText(self.namaAnggota)
                    ownerwindow.ui.labelTipeAnggota.setText(self.tipeAnggota)
                    ownerwindow.ui.labelIDAnggota.setText(self.idAnggota)
                    ownerwindow.show()
                    windowLogin.close()
                    self.ui.label_status.setText("")
                    ownerwindow.ui.btn_logOut.clicked.connect(self.show)
                    ownerwindow.ui.btn_logOut.clicked.connect(self.clearData)
                    ownerwindow.ui.btn_logOut.clicked.connect(ownerwindow.close)
                else:
                    staffwindow = Staff()
                    staffwindow.ui.labelNamaAnggota.setText(self.namaAnggota)
                    staffwindow.ui.labelTipeAnggota.setText(self.tipeAnggota)
                    staffwindow.ui.labelIDAnggota.setText(self.idAnggota)
                    staffwindow.show()
                    windowLogin.close()
                    self.ui.label_status.setText("")
                    staffwindow.ui.btn_logOut.clicked.connect(self.show)
                    staffwindow.ui.btn_logOut.clicked.connect(self.clearData)
                    staffwindow.ui.btn_logOut.clicked.connect(staffwindow.close)
            except:
                return 0
            
    def clearData(self):
        connection = sql_connection()

        cur = connection.cursor()

        query1 = "DELETE FROM pesanan WHERE IDTransaksi IN (SELECT IDTransaksi FROM transaksi WHERE TotalHarga IS NULL)"

        query2 = "DELETE FROM transaksi WHERE TotalHarga IS NULL"
        
        try:
            cur.execute(query1)
            connection.commit()
        except:
            print("failed")  
        
        try:
            cur.execute(query2)
            connection.commit()
            return "Clear Data Success"
        except:
            print("failed")
            return "Clear Data Failed"   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowLogin = Anggota()
    windowLogin.show()
    sys.exit(app.exec())
