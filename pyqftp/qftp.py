#!/usr/bin/env python3

import sys
from ftplib import FTP
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqftp.form_ui import Ui_MainWindow
from pyqftp.utils import url_check

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
