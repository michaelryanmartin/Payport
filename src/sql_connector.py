from src.UI.ui_popup import Dialog
import mysql.connector


def sql_connection():
    connection = mysql.connector
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="payport"
        )
    except mysql.connector.Error as e:
        dialog = Dialog()
        dialog.ui.label.setText("Error:" + e)
        dialog.show()
        dialog.exec()
        print("failed")
    return connection
