from src.main import *

QApplication(sys.argv)

def test_login_success():
    login = Anggota()
    login.ui.lineEditUsername.setText("admin")
    login.ui.lineEditPassword.setText("admin")
    login.login()
    assert login.ui.label_status.text() == "You are logged in"

def test_login_failed():
    login = Anggota()
    login.ui.lineEditUsername.setText("admin")
    login.ui.lineEditPassword.setText("")
    login.login()
    assert login.ui.label_status.text() == "Incorrect Username or Password"
