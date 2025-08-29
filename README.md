# finmate

        # Левая часть: приветствие и график
        left_layout = QVBoxLayout()

        # Приветствие
        greeting = QLabel("Добро пожаловать в Fineas — вашего финансового помощника")
        greeting.setAlignment(Qt.AlignmentFlag.AlignCenter)
        greeting.setStyleSheet("font-size: 20px; font-weight: bold; margin: 10px;")

        # Заглушка для графика
        graph_placeholder = QFrame()
        graph_placeholder.setFrameShape(QFrame.Shape.Box)
        graph_placeholder.setStyleSheet("background-color: #f5f5f5; border: 1px solid #ccc;")
        graph_placeholder.setFixedSize(800, 500)

        left_layout.addWidget(greeting)
        left_layout.addWidget(graph_placeholder, alignment=Qt.AlignmentFlag.AlignCenter)

        # Правая часть: кнопки
        right_layout = QVBoxLayout()

        buttons = [
            "Создать вклад",
            "Накопительный счёт",
            "Акции",
            "Облигации",
            "Посмотреть все ценные бумаги"
        ]

        for text in buttons:
            btn = QPushButton(text)
            btn.setFixedWidth(250)
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
            right_layout.addWidget(btn)

        right_layout.addStretch()

        # Объединяем левую и правую часть
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)