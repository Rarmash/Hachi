import sys #Импортируем библиотеку sys
import os #Импортируем библиотеку os

dir = os.path.abspath(os.curdir) #Узнаём откуда запущен компилятор
p = str(dir) + '\\' + str(sys.argv[1]) #sys.argv[1] - определяем 1 аргумент
modules = ['if', 'else', 'while', 'for', '=', '==', '{', '}', '[', ']', '(', ')', '//'] #Создаём все зарезервированные слова 
var = [] #Создаём список для лексера
vars_ = {} #Создаём список для переменных
try:
    with open(p, 'r', encoding="UTF-8") as f: #Отрываем файл из аргумента
        for ex in f.read().split(): #Распределяем все слова
            var.append(ex) #Записываем все слова в список var
    a = -1 #Устанавливаем значение на каком сейчас var
    for i in var: #Перебираем все значения
        a = a + 1 #Добавляем что это значение просмотренно
        if i == '=': #Если находим совпадение с "="
            vars_[var[a-1]] = var[a+1] #в список vars_ добавляем занчение до и после "="
        if i == 'rprint':
            let = var[a+1]
            for key, value in vars_.items():
                if key == let:
                    print(value)
except FileNotFoundError:
    print('Error! Файл не найден!')