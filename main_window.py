import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super class constructor
        self.setWindowTitle("Stock Control System")
        self.create_layout()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
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
        self.back_button = QPushButton("Back")

        self.search_line_edit = QLineEdit()
        self.edit_line_edit = QLineEdit()

        self.initial_client_layout = QGridLayout()
        self.main_client_layout = QGridLayout()
        
        self.initial_client_layout.addWidget(self.search_button,1,0)
        self.initial_client_layout.addWidget(self.edit_button,2,0)
        self.initial_client_layout.addWidget(self.search_line_edit,1,1)
        self.initial_client_layout.addWidget(self.edit_line_edit,2,1)

        self.main_client_layout.addLayout(self.initial_client_layout,1,0)
        self.main_client_layout.addWidget(self.back_button,2,0)
        self.main_client_layout.addWidget(self.view_button,0,0)
                                             
        self.view_client_widget = QWidget()
        self.view_client_widget.setLayout(self.main_client_layout)

        #connections
        self.back_button.clicked.connect(self.back)
                                      
    def create_jobs_layout(self):
        self.view_button = QPushButton("View Full Database")
        self.search_button = QPushButton("Search")
        self.edit_button = QPushButton("Edit An Entry")
        self.back_button = QPushButton("Back")

        self.search_line_edit = QLineEdit()
        self.edit_line_edit = QLineEdit()

        self.initial_jobs_layout = QGridLayout()
        self.main_jobs_layout = QGridLayout()
        
        self.initial_jobs_layout.addWidget(self.search_button,1,0)
        self.initial_jobs_layout.addWidget(self.edit_button,2,0)
        self.initial_jobs_layout.addWidget(self.search_line_edit,1,1)
        self.initial_jobs_layout.addWidget(self.edit_line_edit,2,1)

        self.main_jobs_layout.addLayout(self.initial_jobs_layout,1,0)
        self.main_jobs_layout.addWidget(self.back_button,2,0)
        self.main_jobs_layout.addWidget(self.view_button,0,0)
                                             
        self.view_jobs_widget = QWidget()
        self.view_jobs_widget.setLayout(self.main_jobs_layout)

        #connections
        self.back_button.clicked.connect(self.back)

    def create_add_layout(self):
        self.back_button = QPushButton("Back")
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.back_button)

        self.view_add_widget = QWidget()
        self.view_add_widget.setLayout(self.grid)

        #connections
        self.back_button.clicked.connect(self.back)

    def create_delete_layout(self):
        self.delete_button = QPushButton("Delete Entry")
        self.back_button = QPushButton("Back")
        self.code_label = QLabel("Customer Code")

        self.delete_line_edit = QLineEdit()

        self.grid1 = QGridLayout()
        self.grid2 = QGridLayout()

        self.grid1.addWidget(self.code_label,1,0)
        self.grid1.addWidget(self.delete_line_edit,1,1)

        self.grid2.addLayout(self.grid1,1,0)
        self.grid2.addWidget(self.delete_button,0,0)
        self.grid2.addWidget(self.back_button,2,0)

        self.view_delete_widget = QWidget()
        self.view_delete_widget.setLayout(self.grid2)

        #connections
        self.back_button.clicked.connect(self.back)

    def create_password_layout(self):
        self.setWindowTitle("Change Password")
        
        self.current_password_label = QLabel("Current Password")
        self.new_password_label = QLabel("New Password")
        self.repeat_new_password_label = QLabel("Repeat New Password")

        self.current_password_line_edit = QLineEdit()
        self.new_password_line_edit = QLineEdit()
        self.repeat_new_password_line_edit = QLineEdit()

        self.change_password_button = QPushButton("Change Password")
        self.back_button = QPushButton("Back")

        self.grid1 = QGridLayout()
        self.grid2 = QGridLayout()

        self.grid1.addWidget(self.current_password_label,0,0)
        self.grid1.addWidget(self.new_password_label,1,0)
        self.grid1.addWidget(self.repeat_new_password_label,2,0)
        self.grid1.addWidget(self.current_password_line_edit,0,1)
        self.grid1.addWidget(self.new_password_line_edit,1,1)
        self.grid1.addWidget(self.repeat_new_password_line_edit,2,1)

        self.grid2.addLayout(self.grid1,0,0)
        self.grid2.addWidget(self.change_password_button,1,0)
        self.grid2.addWidget(self.back_button,2,0)

        self.view_password_widget = QWidget()
        self.view_password_widget.setLayout(self.grid2)

        #connections
        self.back_button.clicked.connect(self.back)

    def client(self):
        self.create_client_layout()
        self.stacked_layout.addWidget(self.view_client_widget)
        self.stacked_layout.setCurrentIndex(1)   
 
    def jobs_layout(self):
        self.create_jobs_layout()
        self.stacked_layout.addWidget(self.view_jobs_widget)
        self.stacked_layout.setCurrentIndex(1)

    def add_entry(self):
        pass
        #self.create_add_layout()
        #self.stacked_layout.addWidget(self.view_add_widget)
        #self.stacked_layout.setCurrentIndex(1)

    def delete_entry(self):
        self.create_delete_layout()
        self.stacked_layout.addWidget(self.view_delete_widget)
        self.stacked_layout.setCurrentIndex(1)

    def change_password(self):
        self.create_password_layout()
        self.stacked_layout.addWidget(self.view_password_widget)
        self.stacked_layout.setCurrentIndex(1)

    def back(self):
        self.create_layout()
        self.stacked_layout.addWidget(self.select_widget)
        self.stacked_layout.setCurrentIndex(2)

       
def main():
    system = QApplication(sys.argv) #create application
    system_window = MainWindow() #new instance of main window
    system_window.show() #show window
    system_window.raise_() #raise to front
    system.exec_() #monitor

if __name__ == "__main__":
    main()
