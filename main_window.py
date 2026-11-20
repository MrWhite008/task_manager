from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox

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

        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_task)


    def add_task(self):
        text = self.task_input.text().strip()
        if text:
            self.task_list.addItem(text)
            self.update_counter()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
        self.task_input.clear()


    def delete_task(self):
        row  = self.task_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")
            return
        answer = QMessageBox.question(self, "Удаление", "Вы уверены, что хотите удалить выбранную задачу?")
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()


    def clear_task(self):
        if self.task_list.count() == 0:
            QMessageBox.warning(self, "Ошибка", "Список уже пуст")
            return
        answer = QMessageBox.question(self, "Удаление", "Вы уверены, что хотите удалить все задачи?")
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()


    def update_counter(self):
        count = self.task_list.count()
        self.counter_label.setText(f"Количество задач: {count}")
