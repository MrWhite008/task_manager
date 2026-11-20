from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)

        self.label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        self.task_list = QListWidget()
        self.delete_button = QPushButton("Удалить")
        self.clear_button = QPushButton("Очистить всё")
        self.counter_label = QLabel("Количество задач: 0")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.task_input)
        self.top_layout.addWidget(self.add_button)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(self.delete_button)
        self.bottom_layout.addWidget(self.clear_button)

        self.main_layout.addWidget(self.label)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.task_list)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addWidget(self.counter_label)
