#!/usr/bin/env python3

import sys
from ftplib import FTP
from PyQt5.QtWidgets import QApplication, QMainWindow
from form_ui import Ui_MainWindow

app = QApplication(sys.argv)

class FtpWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FtpWindow, self).__init__()
        self.setupUi(self)
        self.btnOpen.clicked.connect(self.connectFTP)

    def connectFTP(self):
        self.lstFileList.clear()
        self.lstFileList.addItem("Loading...")
        with FTP(self.txtFtpUrl.text()) as ftp:
            ftp.login(user="ftp", passwd="ftp")
            flist = list(ftp.nlst())
            self.lstFileList.clear()
            for f in flist:
                self.lstFileList.addItem(f)

window = FtpWindow()
window.show()
sys.exit(app.exec_())
