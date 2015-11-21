import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Client Database")
        self.create_layout()

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.select_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)



    def create_layout(self):
        self.view_button = QPushButton("View Database")
        
        self.search_label = QLabel("Search")
        self.view_job_label = QLabel("View Job")

        self.search_line_edit = QLineEdit()
        self.view_job_line_edit = QLineEdit()

        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.view_button,0,1)
        self.initial_layout.addWidget(self.search_label,2,0)
        self.initial_layout.addWidget(self.view_job_label,3,0)
        self.initial_layout.addWidget(self.search_line_edit,2,1)
        self.initial_layout.addWidget(self.view_job_line_edit,3,1)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

        
def main():
    client_database_view = QApplication(sys.argv)
    client_window = ClientWindow()
    client_window.show()
    client_window.raise_()
    client_database_view.exec_()

if __name__ == "__main__":
    main()
