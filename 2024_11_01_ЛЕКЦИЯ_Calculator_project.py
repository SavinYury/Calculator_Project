# ПРОГРАММА КАЛЬКУЛЯТОР
from tkinter import * # Импортируем из tkinter все функции
from tkinter import ttk # Расширенный вариант tkinter

window = Tk()
window.title("КАЛЬКУЛЯТОР") # Переименовываем окно window
window.iconbitmap(default="calculator-icon.ico") # Перезаписываем иконку вместо перышка

### Создаем главное окно ВЫВОДА информации
line_input = Entry(window, font=("Arial",14)) # Поле для ВЫВОДА визуальной информации
line_input.grid(row=0,column=0, columnspan=4, sticky="ew") # Устанавливаем его в НУЛЕВОЙ ряд НУЛЕВОЙ столбец и растягиваем на ЧЕТЫРЕ колонки

### Создаем КНОПКИ ЦИФРЫ калькулятора
b1 = ttk.Button(window, text="1")
b1.grid(row=3,column=0)
b2 = ttk.Button(window, text="2")
b2.grid(row=3,column=1)
b3 = ttk.Button(window, text="3")
b3.grid(row=3,column=2)
b4 = ttk.Button(window, text="4")
b4.grid(row=2,column=0)
b5 = ttk.Button(window, text="5")
b5.grid(row=2,column=1)
b6 = ttk.Button(window, text="6")
b6.grid(row=2,column=2)
b7 = ttk.Button(window, text="7")
b7.grid(row=1,column=0)
b8 = ttk.Button(window, text="8")
b8.grid(row=1,column=1)
b9 = ttk.Button(window, text="9")
b9.grid(row=1,column=2)
b0 = ttk.Button(window, text="0")
b0.grid(row=4,column=0)

### Создаем КНОПКИ Математических ДЕЙСТВИЙ калькулятора
# (с укороченным вариантом записи кода для примера)
ttk.Button(window, text="+").grid(row=1, column=3)
ttk.Button(window, text="-").grid(row=2, column=3)
ttk.Button(window, text="*").grid(row=3, column=3)
ttk.Button(window, text="/").grid(row=4, column=3)

### Создаем КНОПКИ РЕЗУЛЬТАТИВНЫХ действий калькулятора
# (с укороченным вариантом записи кода для примера)
ttk.Button(window, text="C").grid(row=4, column=1)
ttk.Button(window, text="=").grid(row=4, column=2)

window.mainloop()
