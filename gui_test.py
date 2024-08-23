import sys

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QDateEdit,
    QSizePolicy,
    QGraphicsDropShadowEffect,
)
from PyQt6.QtGui import QColor, QPalette, QFont
from datetime import datetime

class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid #e0e0e0;
                border-radius: 3px;
                padding: 5px;
            }
        """)

class CustomComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("""
            QComboBox {
                border: 1px solid #e0e0e0;
                border-radius: 3px;
                padding: 5px;
            } 
            QComboBox::drop-down 
            {
                border: 0px;
            }

            QComboBox::down-arrow {
                image: url(assets/chevron_down.png);
                width: 15px;
                height: 15px;
            }
        """)

class CustomQDateEdit(QDateEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("""
            QDateEdit {
                border: 1px solid #e0e0e0;
                border-radius: 3px;
                padding: 5px;
            } 
            QDateEdit::drop-down 
            {
                border: 0px;
            }

            QDateEdit::down-arrow {
                image: url(assets/chevron_down.png);
                width: 15px;
                height: 15px;
            }
        """)

class CustomQPushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet("""
            QPushButton {
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                padding: 10px;
                color: white;
                background-color: black;
                margin-top: 20px;
            } 
            QPushButton:hover {
                background-color: grey;
            }
            QPushButton:pressed {
                background-color: black;
            }
        """)

        # Create and apply the shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(5)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 50))  # 50 is the alpha value for 20% opacity
        self.setGraphicsEffect(shadow)

        font = QFont('Helvetica', 10)  # Choose your desired font and size
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 2)  # Set letter spacing (2 pixels)
        self.setFont(font)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize (400, 400)

        self.setWindowTitle("Access Request Form")
        self.setStyleSheet(
            """
            background-color: #ffffff;
            """
            )

        # Main layout
        main_layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Card Access Request")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font: Helvetica; font-size: 24px; font-weight: bold; padding-bottom: 20px;")
        main_layout.addWidget(title_label)

        # Grid layout for form elements
        grid_layout = QGridLayout()

        # First Row: First and Last Name
        FName_label = QLabel(f"First Name")
        FName_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        grid_layout.addWidget(FName_label, 0, 0)
        grid_layout.addWidget(CustomLineEdit(), 1, 0)

        LName_label = QLabel(f"Last Name")
        LName_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        grid_layout.addWidget(LName_label, 0, 1)
        grid_layout.addWidget(CustomLineEdit(), 1, 1)

        # Second row:
        second_row_layout = QHBoxLayout()
        
        # ID Number
        ID_vbox = QVBoxLayout()
        ID_label = QLabel(f"ID")
        ID_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        ID_vbox.addWidget(ID_label)
        ID_vbox.addWidget(CustomLineEdit())
        second_row_layout.addLayout(ID_vbox)

        # UPI
        UPI_vbox = QVBoxLayout()
        UPI_label = QLabel(f"UPI")
        UPI_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        UPI_vbox.addWidget(UPI_label)
        UPI_vbox.addWidget(CustomLineEdit())
        second_row_layout.addLayout(UPI_vbox)

        # Card Access Number
        card_vbox = QVBoxLayout()
        card_label = QLabel(f"Card No.")
        card_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        card_vbox.addWidget(card_label)
        card_vbox.addWidget(CustomLineEdit())
        second_row_layout.addLayout(card_vbox)

        grid_layout.addLayout(second_row_layout, 2, 0, 1, 2)

        # Third row:
        third_row_layout = QHBoxLayout()
        
        #Programme
        programme_vbox = QVBoxLayout()
        programme_label = QLabel("Programme")
        programme_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        programme_vbox.addWidget(programme_label)
        programme_combo = CustomComboBox()
        programme_combo.addItems(["Architecture", "Urban Planning", "Urban Design"])
        programme_combo.setCurrentIndex(0)  # Set default to Architecture
        programme_vbox.addWidget(programme_combo)
        third_row_layout.addLayout(programme_vbox)

        # Level of Appointment
        appointment_vbox = QVBoxLayout()
        appointment_label = QLabel("Level of Appointment")
        appointment_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        appointment_vbox.addWidget(appointment_label)
        appointment_combo = CustomComboBox()
        appointment_combo.addItems(["Staff", "Student", "Visitor", "ARCHPLAN Summer"])
        appointment_combo.setCurrentIndex(0)  # Set default to Staff
        appointment_vbox.addWidget(appointment_combo)
        third_row_layout.addLayout(appointment_vbox)

        # Access Group
        access_vbox = QVBoxLayout()
        access_label = QLabel("Access Group")
        access_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        access_vbox.addWidget(access_label)
        access_combo = CustomComboBox()
        access_combo.addItems(["CAI Staff", "CAI Arch & Plan PhD", "ARCHPLAN Summer"])
        access_combo.setCurrentIndex(0)  # Set default to CAI Staff
        access_vbox.addWidget(access_combo)
        third_row_layout.addLayout(access_vbox)

        grid_layout.addLayout(third_row_layout, 3, 0, 1, 2)

        # Fourth row: Date pickers
        fourth_row_layout = QHBoxLayout()
        today = QDate.currentDate()

        # Request Sent Date
        request_date_vbox = QVBoxLayout()
        request_date_label = QLabel(f"Request Sent")
        request_date_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        request_date_vbox.addWidget(request_date_label)
        
        request_date_edit = CustomQDateEdit()
        request_date_edit.setCalendarPopup(True)  # Enable the pop-up calendar
        request_date_edit.setDisplayFormat("dd/MM/yyyy")
        request_date_edit.setDate(today)
        request_date_edit.setMinimumDate(today)
        request_date_vbox.addWidget(request_date_edit)

        fourth_row_layout.addLayout(request_date_vbox)

        # Contract End Date
        contract_end_date_vbox = QVBoxLayout()
        contract_end_date_label = QLabel(f"Contract End Date")
        contract_end_date_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        contract_end_date_vbox.addWidget(contract_end_date_label)
        
        contract_end_date_edit = CustomQDateEdit()
        contract_end_date_edit.setCalendarPopup(True)  # Enable the pop-up calendar
        contract_end_date_edit.setDisplayFormat("dd/MM/yyyy")
        contract_end_date_edit.setDate(today)
        contract_end_date_edit.setMinimumDate(today)
        contract_end_date_vbox.addWidget(contract_end_date_edit)
        
        fourth_row_layout.addLayout(contract_end_date_vbox)

        grid_layout.addLayout(fourth_row_layout, 5, 0, 1, 2)

        # Center justify all rows
        for i in range(7):
            grid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add grid layout to main layout
        main_layout.addLayout(grid_layout)

        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button = CustomQPushButton("SUBMIT")
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        button_layout.addWidget(button)

        # Add the button container to the grid layout, spanning all columns
        grid_layout.addWidget(button_container, grid_layout.rowCount(), 0, 1, grid_layout.columnCount())

        # Set up the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()