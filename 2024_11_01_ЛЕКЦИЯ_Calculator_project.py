# ПРОГРАММА КАЛЬКУЛЯТОР
from tkinter import * # Импортируем из tkinter все функции
from tkinter import ttk # Расширенный вариант tkinter
import Mathematical_operators as ma # Подключаем свой собственный модуль с математическими операциями


### Создаем функцию знака РАВНО как результата математических действий
def result_calc(): #
    res = None  # До первого ввода цифры резервируем значение None
    second_num = int(line_input.get()) # Переменная ввода второго числа
    print(f"second_num = {second_num}")
    line_input.delete(0, END) # После нажатия мат знака очищаем поле от 0 значения и до конца
    if operator == "+": # В переменной operator храниться знак сложения то из модуля вызываем функцию ma.add
        res = ma.add(first_num, second_num) #
    elif operator == "-":
        res = ma.subtract(first_num, second_num)
    elif operator == "*":
        res = ma.multiply(first_num, second_num)
    elif operator == "/":
        res = ma.division(first_num, second_num)
    print(f"res = {res}")
    line_input.insert(0, res) # Выводим результат на экран


### Создаем функцию ВЫБОРА числа
def choice_number(num): # С параметром выбранного числа num
    line_input.insert(END, num) # Вносим цифры num в конце метки вывода числе на экран


### Создаем функцию очистки экрана после ВВОДА математической операции
def choice_operator(oper):
    global operator # Назначаем глобальной переменной
    global first_num # Назначаем глобальной переменной
    first_num = int(line_input.get()) # До первого ввода цифры резервируем значение None
    print(f"first_num = {first_num}")
    operator = oper # Создаем переменную в которую запоминаем какое математическое действие мы записали через функцию
    print(f"operator = {operator}")
    line_input.delete(0, END) # После нажатия мат знака очищаем поле от 0 значения и до конца

### Создаем функцию очистки экрана ВВОДА
def clear_line():
    line_input.delete(0, END)


### Установка нулевых значений переменным
first_num = None # До первого ввода цифры резервируем значение None
operator = None

window = Tk()
window.title("КАЛЬКУЛЯТОР") # Переименовываем окно window
window.iconbitmap(default="calculator-icon.ico") # Перезаписываем иконку вместо перышка

### Создаем главное окно ВЫВОДА информации
line_input = Entry(window, font=("Arial",14)) # Поле для ВЫВОДА визуальной информации
line_input.grid(row=0,column=0, columnspan=4, sticky="ew") # Устанавливаем его в НУЛЕВОЙ ряд НУЛЕВОЙ столбец и растягиваем на ЧЕТЫРЕ колонки

### Создаем КНОПКИ ЦИФРЫ калькулятора
b1 = ttk.Button(window, text="1", command=lambda: choice_number("1"))
b1.grid(row=3,column=0)
b2 = ttk.Button(window, text="2", command=lambda: choice_number("2"))
b2.grid(row=3,column=1)
b3 = ttk.Button(window, text="3", command=lambda: choice_number("3"))
b3.grid(row=3,column=2)
b4 = ttk.Button(window, text="4", command=lambda: choice_number("4"))
b4.grid(row=2,column=0)
b5 = ttk.Button(window, text="5", command=lambda: choice_number("5"))
b5.grid(row=2,column=1)
b6 = ttk.Button(window, text="6", command=lambda: choice_number("6"))
b6.grid(row=2,column=2)
b7 = ttk.Button(window, text="7", command=lambda: choice_number("7"))
b7.grid(row=1,column=0)
b8 = ttk.Button(window, text="8", command=lambda: choice_number("8"))
b8.grid(row=1,column=1)
b9 = ttk.Button(window, text="9", command=lambda: choice_number("9"))
b9.grid(row=1,column=2)
b0 = ttk.Button(window, text="0", command=lambda: choice_number("0"))
b0.grid(row=4,column=0)

### Создаем КНОПКИ Математических ДЕЙСТВИЙ калькулятора
# (с укороченным вариантом записи кода для примера)
ttk.Button(window, text="+", command=lambda: choice_operator("+")).grid(row=1, column=3)
ttk.Button(window, text="-", command=lambda: choice_operator("-")).grid(row=2, column=3)
ttk.Button(window, text="*", command=lambda: choice_operator("*")).grid(row=3, column=3)
ttk.Button(window, text="/", command=lambda: choice_operator("/")).grid(row=4, column=3)

### Создаем КНОПКИ РЕЗУЛЬТАТИВНЫХ действий калькулятора
# (с укороченным вариантом записи кода для примера)
ttk.Button(window, text="C", command=clear_line).grid(row=4, column=1)
ttk.Button(window, text="=", command=result_calc).grid(row=4, column=2)

window.mainloop()
