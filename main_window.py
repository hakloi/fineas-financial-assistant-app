import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame,
    QGridLayout
)

x = 100

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(950, 700))
        self.setWindowTitle("Fineas - financial assistant")
        # self.setStyleSheet("backgroud: 'white';")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # grid
        grid = QGridLayout()
        central_widget.setLayout(grid)
        grid.setContentsMargins(20, 20, 10, 30) #left, up, right, down
        # central_widget.setStyleSheet("backgroud: white;") 
        
        # greeting
        greet_text = (
            "Здравствуйте! Я Финеас — ваш персональный финансовый ассистент."
            "\nМоя задача — помогать вам контролировать расходы, отслеживать доходы и подсказывать, "
            "\nкак эффективнее управлять средствами."
            + f"\nВаш заработок за день составил: {x}"
            + f"\nВаш заработок в месяц составил: {x}"
            + f"\nНаибольший доход составил по — {x}."
            + f"\nВ сравнении с прошлым месяцем, вы получили на {x} %!"
            + f"\nВы инвестировали в этом месяце: {x} ₽"
            + f"\nДоход от инвестиций составил: {x} ₽"
            "\n\nЯ также могу показывать актуальный курс валют и строить графики ваших финансов."
        )

        greet = QLabel(greet_text)
        greet.setAlignment(Qt.AlignmentFlag.AlignTop)
        greet.setStyleSheet("font-size: 16px; color: black")
        grid.addWidget(greet, 0, 0, 1, 2)
        # (row=0, col=0, rowSpan=1, colSpan=2) — растянуть на 2 колонки
        # background: black; 
        
        # graph
        graph_placeholder = QFrame()
        graph_placeholder.setFixedSize(600, 400)
        graph_placeholder.setStyleSheet("border: 1px solid #ccc;")
        grid.addWidget(graph_placeholder, 1, 0)  # (row=1, col=0)
        
        # currency
        currency_text = (
            "Курс валют на сегодня:"
            f"\nUSD → {x} ₽"
            f"\tEUR → {x} ₽"
            f"\nCNY → {x} ₽"
            f"\tGBP → {x} ₽"
            f"\nЗолото → {x} $/oz"
            f"\nНефть → {x} $/барр."
        )
        currency_label = QLabel(currency_text)
        currency_label.setStyleSheet("font-size: 18px; color: black; margin-bottom: 15px;")
        
        
        # buttons
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout()
        buttons_widget.setLayout(buttons_layout)
        
        buttons_layout.addWidget(currency_label)
        
        buttons = [
            "Создать вклад",
            "Накопительный счёт",
            "Акции",
            "Облигации",
            "Посмотреть все ценные бумаги"
        ]
        
        for text in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(300, 50)
            btn.setStyleSheet("""
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
            buttons_layout.addWidget(btn)
        
        buttons_layout.addStretch()
        grid.addWidget(buttons_widget, 1, 1)