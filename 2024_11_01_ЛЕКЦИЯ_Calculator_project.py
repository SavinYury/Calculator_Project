# ПРОГРАММА КАЛЬКУЛЯТОР
from tkinter import * # Импортируем из tkinter все функции
from tkinter import ttk # Расширенный вариант tkinter

window = Tk()
window.title("КАЛЬКУЛЯТОР") # Переименовываем окно window
window.iconbitmap(default="calculator-icon.ico") # Перезаписываем иконку вместо перышка

### Создаем главное окно ВЫВОДА информации
line_input = Entry(window, font=("Arial",14)) # Поле для ВЫВОДА визуальной информации
line_input.grid(row=0,column=0, columnspan=4, sticky="ew") # Устанавливаем его в НУЛЕВОЙ ряд НУЛЕВОЙ столбец и растягиваем на ЧЕТЫРЕ колонки


window.mainloop()
