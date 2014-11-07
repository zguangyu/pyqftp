import sys
from ftplib import FTP
from PyQt5.QtWidgets import QApplication, QDialog
from form_ui import Ui_Form

app = QApplication(sys.argv)

class FtpDialog(QDialog, Ui_Form):
    def __init__(self):
        super(FtpDialog, self).__init__()
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

window = FtpDialog()
window.show()
sys.exit(app.exec_())
