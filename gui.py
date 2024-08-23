import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from spreadsheet import update_spreadsheet

class SpreadsheetGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.dateedit, QtCore.Qt.TopLeftCorner)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())

    def initUI(self):
        self.setWindowTitle('Spreadsheet GUI')
        self.setGeometry(100, 100, 900, 900)

        layout = QVBoxLayout()

        # First Name
        self.first_name_label = QLabel('First Name')
        self.first_name_entry = QLineEdit()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_entry)

        # Last Name
        self.last_name_label = QLabel('Last Name')
        self.last_name_entry = QLineEdit()
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_entry)

        # ID
        self.id_label = QLabel('ID')
        self.id_entry = QLineEdit()
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_entry)

        # UPI
        self.upi_label = QLabel('UPI')
        self.upi_entry = QLineEdit()
        layout.addWidget(self.upi_label)
        layout.addWidget(self.upi_entry)

        # Card Number
        self.card_label = QLabel('Card Number')
        self.card_entry = QLineEdit()
        layout.addWidget(self.card_label)
        layout.addWidget(self.card_entry)

        # Programme
        self.programme_label = QLabel('Programme')
        self.programme_combobox = QComboBox()
        # Add programme options here
        layout.addWidget(self.programme_label)
        layout.addWidget(self.programme_combobox)

        # Level of Appointment
        self.appointment_level_label = QLabel('Level of Appointment')
        self.appointment_level_combobox = QComboBox()
        self.appointment_level_combobox.addItems(["ARCHPLAN Summer", "Staff", "Student", "Visitor"])
        layout.addWidget(self.appointment_level_label)
        layout.addWidget(self.appointment_level_combobox)

        # Access Group
        self.access_group_label = QLabel('Access Group')
        self.access_group_combobox = QComboBox()
        # Add access group options here
        layout.addWidget(self.access_group_label)
        layout.addWidget(self.access_group_combobox)

        # # Request Sent
        self.request_date_label = QLabel('Request Sent')
        self.request_date = QWidget.QDateEdit(self.frame)
        layout.addWidget(self.request_date_label)
        layout.addWidget(self.request_date)

        # Contract Expiry
        # self.contract_end_date_label = QLabel('Contract Expiry')
        # self.contract_end_date = QDateEdit()  # You might want to use QDateEdit instead
        # layout.addWidget(self.contract_end_date_label)
        # layout.addWidget(self.contract_end_date)

        # Update Button
        self.update_button = QPushButton('Update Spreadsheet')
        self.update_button.clicked.connect(self.update_value)
        layout.addWidget(self.update_button)

        self.setLayout(layout)

    def update_value(self):
        path = 'test_record.xlsx'
        new_row_data = {
            "First Name": self.first_name_entry.text(),
            "Last Name": self.last_name_entry.text(),
            "ID": self.id_entry.text(),
            "UPI": self.upi_entry.text(),
            "Card Number": self.card_entry.text(),
            "Programme": self.programme_combobox.currentText(),
            "Level of Appointment": self.appointment_level_combobox.currentText(),
            "Access Group": self.access_group_combobox.currentText(),
            #"Request Sent": self.request_date.text(),
            #"Contract Expiry": self.contract_end_date.text()
        }
        try:
            result = update_spreadsheet(new_row_data, path)
            QMessageBox.information(self, "Success", result)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpreadsheetGUI()
    ex.show()
    sys.exit(app.exec_())