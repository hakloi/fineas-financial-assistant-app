from PyQt6.QtWidgets import QPushButton, QMessageBox

buttons_info = {
    "Создать вклад": "Открытие вклада пока в разработке.",
    "Накопительный счёт": "Здесь будет информация о накопительных счетах.",
    "Акции": "Просмотр акций пока не подключен.",
    "Облигации": "Облигации появятся позже.",
    "Посмотреть все ценные бумаги": "Здесь будет список всех ценных бумаг."
}

class ActionButton(QPushButton):
    def __init__(self, text, parent=None, action_msg="Функция в разработке"):
        super().__init__(text, parent)
        self.action_msg = action_msg
        self.setFixedSize(300, 45)
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.clicked.connect(self.do_action)

    def do_action(self):
        QMessageBox.information(self, self.text(), self.action_msg)
        