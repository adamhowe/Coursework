import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.create_layout()

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.select_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

    def create_layout(self):
        self.login_button = QPushButton("Login")

        self.username_label = QLabel("Username")
        self.password_label = QLabel("Password")

        self.username_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()

        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.username_label,1,0)
        self.initial_layout.addWidget(self.password_label,2,0)
        self.initial_layout.addWidget(self.username_line_edit,1,1)
        self.initial_layout.addWidget(self.password_line_edit,2,1)
        self.initial_layout.addWidget(self.login_button,1,2)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)


def main():
    login_screen = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    login_window.raise_()
    login_screen.exec_()

if __name__ == "__main__":
    main()
