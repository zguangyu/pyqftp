#!/usr/bin/env python3

import sys
from ftplib import FTP
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from pyqftp.qftp import FtpWindow

QCoreApplication.setOrganizationName("Guangyu")
QCoreApplication.setOrganizationDomain("guangyu.me")
QCoreApplication.setApplicationName("QFTP")

app = QApplication(sys.argv)

window = FtpWindow()
window.show()
sys.exit(app.exec_())
