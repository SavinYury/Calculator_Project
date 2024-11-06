### МОДУЛЬ с МАТЕМАТИЧЕСКИМИ ФУНКЦИЯМИ
from future.types import newint

### Функция СЛОЖЕНИЯ
def add(a,b):
    return a+b

### Функция ВЫЧИТАНИЯ
def subtract(a,b):
    return a-b

### Функция УМНОЖЕНИЯ
def multiply(a,b):
    return a*b

### Функция ДЕЛЕНИЯ
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя"

