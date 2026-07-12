from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QPushButton
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.originary = "12345"
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Проверка пароля")
        self.resize(200, 100)

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите ваш пароль...")

        self.info = QLabel()
        self.btn = QPushButton("Войти")

        self.btn.clicked.connect(self.check_password)

        layout.addWidget(self.info)
        layout.addWidget(self.password_input)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def check_password(self):
        user_text = self.password_input.text()

        if not user_text:
            self.info.setText("<font color = 'red'> Введите пароль! </font>")
        elif user_text == self.originary:
            self.info.setText("<font color = 'green'> Доступ разрешён! </font>")
        else:
            self.info.setText("<font color = 'red'> Неверный пароль! </font>")
            self.password_input.clear()

