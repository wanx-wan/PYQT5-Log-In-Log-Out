import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, QTime, QDateTime,Qt


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.passcode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.homebutton.clicked.connect(self.gotocheck)
        self.homebutton.clicked.connect(self.gotoshow)
        self.Link.clicked.connect(self.gotoLink)

    def gotoshow(self):
        userid=self.userid.text()
        passcode=self.passcode.text()
        print("ชื่อผู้ใช้: ", userid, "รหัสผ่าน:", passcode)
        datetime = QDateTime.currentDateTime()
        print("เข้าสู่ระบบเมื่อ: ", datetime.toString(Qt.ISODate))
    
    def gotoLink(self):
        print("https://drive.google.com/file/d/1ffnhnYBk3QOhgikZ2VVNMw-wlZpOdIqN")

    def gotocheck(self):
        home = Homepage()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Homepage(QDialog):
    def __init__(self):
        super(Homepage,self).__init__()
        loadUi("pages.ui",self)
        name=self.name.text()
        ids =self.ID.text()
        if self.backupbutton.clicked.connect(self.createaccfunction):
            print("เข้าสู่ระบบสำเร็จ")

    def createaccfunction(self):
        self.close()
        datetime = QDateTime.currentDateTime()
        print("ลงชื่อเข้าทำงานโดย: ", self.name.text()," ลงชื่อเมื่อ:", datetime.toString(Qt.ISODate))
        print("รหัสพนักงาน: ", self.ID.text())
        print("ออกจากระบบสำเร็จ")

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
app.setApplicationName("CC")
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()