import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super class constructor
        self.setWindowTitle("Stock Control System")
        self.create_layout()

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.select_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

    def create_layout(self):
        self.client_button = QPushButton("Client Database")
        self.jobs_button = QPushButton("Jobs Database")
        self.add_button = QPushButton("Add entry to system")
        self.delete_button = QPushButton("Delete entry from system")
        self.password_button = QPushButton("Change Password")

    #create layout
        self.initial_layout = QGridLayout()
        self.initial_layout.addWidget(self.client_button)
        self.initial_layout.addWidget(self.jobs_button)
        self.initial_layout.addWidget(self.add_button)
        self.initial_layout.addWidget(self.delete_button)
        self.initial_layout.addWidget(self.password_button)

        self.select_widget = QWidget()
        self.select_widget.setLayout(self.initial_layout)

    #connections
        self.client_button.clicked.connect(self.client)
        self.jobs_button.clicked.connect(self.jobs_layout)
        self.add_button.clicked.connect(self.add_entry)
        self.delete_button.clicked.connect(self.delete_entry)
        self.password_button.clicked.connect(self.change_password)

    def create_client_layout(self):
        self.view_button = QPushButton("View Full Database")
        self.search_button = QPushButton("Search")
        self.edit_button = QPushButton("Edit An Entry")

        #self.

        self.view_client_widget = QWidget()
        #self.view_client_widget.setLayout()


    def client(self):
        print("yay")
        self.create_client_layout()
        self.grid_layout.addWidget(self.view_client_widget)
        self.grid_layout.setCurrentIndex(1)
        
 
    def jobs_layout(self):
        pass

    def add_entry(self):
        pass

    def delete_entry(self):
        pass

    def change_password(self):
        pass
       
def main():
    system = QApplication(sys.argv) #create application
    system_window = MainWindow() #new instance of main window
    system_window.show() #show window
    system_window.raise_() #raise to front
    system.exec_() #monitor

if __name__ == "__main__":
    main()
