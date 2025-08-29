# Fineas - financial assistent
Программа для анализа расходов и доходов с ценных бумаг, вкладов и накопительных счетов.

## Структура:

main.py — запускает приложение, импортирует MainWindow из main_window.py.

main_window.py — весь GUI: приветствие, график, кнопки, панель валют.

buttons.py — отдельный модуль для кнопок с готовыми слотами, чтобы не засорять MainWindow.

/data — хранение всех пользовательских данных, JSON и CSV удобно для теста и будущей аналитики.

/graphs — отдельный модуль для построения графиков по данным (Matplotlib, PyQtGraph и т.п.).

/resources — все визуальные материалы для интерфейса.

/utils — вспомогательные скрипты для загрузки данных и API.

## Дерево: 

fineas/

├── main.py

├── main_window.py

├── buttons.py

├── __data/__ investments.json / income.csv / expenses.csv


├── __graphs/__ income_graph.py

├── __resources/__ icons/ images/

└── __utils/__ data_loader.py /currency_api.py
