#!/usr/bin/env python3

import sys
from ftplib import FTP
from PyQt5.QtWidgets import QApplication
from pyqftp.qftp import FtpWindow

app = QApplication(sys.argv)

window = FtpWindow()
window.show()
sys.exit(app.exec_())
