from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class LoginDialog(QDialog):
    def __init__(self, parent=None, username=None):
        super(LoginDialog, self).__init__(parent)

        self.nameEdit = QLineEdit()
        self.nameEdit.setText(username)
        self.passEdit = QLineEdit()
        self.passEdit.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton(QCoreApplication.translate("LoginDialog", "&Submit"))
        self.submitButton.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.nameEdit)
        layout.addWidget(self.passEdit)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)
        self.setWindowTitle(QCoreApplication.translate("LoginDialog", "Login"))

        if self.nameEdit.text() != None and len(self.nameEdit.text()) != 0:
            self.passEdit.setFocus()
