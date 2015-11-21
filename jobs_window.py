import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class JobsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jobs Database")
        self.create_layout()

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.select_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

    def create_layout(self):
        self.view_button = QPushButton("View Database")
        
        self.search_label = QLabel("Search Database")
        self.view_client_label = QLabel("View Related Client")
        self.edit_label = QLabel("Edit Job")

        self.search_line_edit = QLineEdit()
        self.view_client_line_edit = QLineEdit()
        self.edit_line_edit = QLineEdit()

        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.view_button,0,1)
        self.initial_layout.addWidget(self.search_label,2,0)
        self.initial_layout.addWidget(self.view_client_label,3,0)
        self.initial_layout.addWidget(self.search_line_edit,2,1)
        self.initial_layout.addWidget(self.view_client_line_edit,3,1)
        self.

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

        
def main():
    jobs_database_view = QApplication(sys.argv)
    jobs_window = JobsWindow()
    jobs_window.show()
    jobs_window.raise_()
    jobs_database_view.exec_()

if __name__ == "__main__":
    main()
