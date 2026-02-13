import sys
import humanize
import datetime as dt

from PyQt5 import QtCore
from PyQt5.QtCore import (
    Qt, QTimer, QTime
)
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QInputDialog,
)

light_gray = "#BFC9D1"
dark_gray = "#25343F"
black = "#1B211A"
orange = "#FF9B51"
white = "#EAEFEF"
dark_green = "#628141"
light_green = "#BBC863"
dark_red = "#D02752"
bright_red = "#E4B4C0"
dark_blue = "#1C4D8D"
medium_blue = "#4988C4"
light_blue = "#BDE8F5"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Check-in App")

        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)

        self.time_started = False
        self.selected_task_arr = []
        

        self.timer_obj = QTimer(self)
        self.time = QTime(0,0,0)
        self.timer_obj.timeout.connect(self.timer_event)


        label = QLabel("Welcome to the Check-in App!")
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")

        #checkbox = QCheckBox("I agree to the terms and conditions")

        self.task_dropdown = QComboBox(self)

        add_topic_button = QPushButton("Add Topic", self)
        add_topic_button.clicked.connect(self.handle_add_topic_button_click)


        timer_start_button = QPushButton("Start Timer", self)
        #timer_start_button.setStyleSheet("background-color: {dark_green}; color:  {light_green}; font-size: 30px; border-radius: 10px; padding: 10px;")
        timer_start_button.clicked.connect(self.on_timer_start)

        timer_stop_button = QPushButton("Stop Timer", self)
        #timer_stop_button.setStyleSheet("background-color: {dark_red}; color: {bright_red}; font-size: 30px; border-radius: 10px; padding: 10px;")
        timer_stop_button.clicked.connect(self.timer_stop)

        timer_reset_button = QPushButton("Reset Timer", self)
        #timer_reset_button.setStyleSheet("background-color: {dark_gray}; color: {light_gray}; font-size: 30px; border-radius: 10px; padding: 10px;")
        timer_reset_button.clicked.connect(self.timer_reset)

        self.time_label = QLabel("No Time Clocked")
        #self.time_label.setStyleSheet("background-color: {dark_blue}; color: {light_blue}; font-size: 20px; font-weight: bold; border-radius: 8px;")

        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(add_topic_button, alignment=Qt.AlignCenter)
        #layout.addWidget(checkbox, alignment=Qt.AlignCenter)
        layout.addWidget(self.task_dropdown, alignment=Qt.AlignCenter)
        layout.addWidget(timer_start_button, alignment=Qt.AlignCenter)
        layout.addWidget(timer_stop_button, alignment=Qt.AlignCenter)
        layout.addWidget(timer_reset_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.time_label, alignment=Qt.AlignCenter)
        
        self.setCentralWidget(container)


    def on_timer_start(self):
        if(not self.time_started):
            self.time_started = True
            print("Timer started")
            self.timer_obj.start(1000)
        else :
            print("Timer already started")

    def timer_stop(self):
        if(self.time_started):
            print("Timer stopped")
            self.timer_obj.stop()
            self.time_started = False
        else:
            print("Timer already stopped")
            

    def timer_reset(self):
        self.time = QTime(0,0,0)
        self.time_label.setText("0 seconds")
        print("Timer reset")

    def timer_event(self):
        self.time = self.time.addSecs(1)
        print(self.time.toString("hh:mm:ss"))
        self.formatted_time= humanize.naturaldelta(dt.timedelta(hours=self.time.hour(), minutes=self.time.minute(), seconds=self.time.second()))
        self.time_label.setText(self.formatted_time)

    def handle_add_topic_button_click(self):
        self.text, self.ok = QInputDialog.getText(self, "Topic name", "Enter new topic name")
        if self.ok and self.text.strip():
            self.add_topic(self.text)

    def add_topic(self, topic):
        self.selected_task_arr.append(topic)
        self.task_dropdown.addItem(topic)
        print(f"{topic} added to topics!")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()