import sys
from ftplib import FTP
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqftp.form_ui import Ui_MainWindow
from pyqftp.utils import url_check
from urllib.parse import urlparse

class FtpWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FtpWindow, self).__init__()
        self.setupUi(self)
        self.btnOpen.clicked.connect(self.connectFTP)

    def connectFTP(self):
        host = self.txtFtpUrl.text()
        user = None
        passwd = None
        port = 21
        if url_check(self.txtFtpUrl.text()):
            res = urlparse(self.txtFtpUrl.text())
            host = res.hostname
            user = res.username
            passwd = res.password
            port = res.port if res.port else 21

        if user is not None and passwd is None:
            # TODO: pop up a box to receive password
            pass

        self.lstFileList.clear()
        self.lstFileList.addItem("Loading...")

        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(user, passwd)
        flist = list(ftp.nlst())
        self.lstFileList.clear()
        for f in flist:
            self.lstFileList.addItem(f)
