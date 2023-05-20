#print(5,8,6)

#n = 5
#n = None #пустое значение
#n = 1.89
#print(n)

#n = 'fdd'
#print(n)

#n = "fddd"
#print(n)

"""
n = 5
print(type(n))       3 апострофа сверху + 3 снизу - для многострочного комментария

n = 'kjkjfh'         или Ctrl+K затем Ctrl+C
print(type(n))
"""

# n = 'kj\'kj'  #\ для вывода символа
# print(n)

# n = 'kj"fhhgg"kj'  # для вывода записи в кавычках
# print(n)

#ИНТЕРПОЛЯЦИЯ - получение сложной строки из нескольких простых с пом-ю шаблонов
# a = 5
# b = 5.89
# c = 'hello'

# #print(a, '-', b, '-', c)
# #print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))


#ВВОД ДАННЫХ
# #input()  #пользователь пишет в консоли
# print('Введите первое число: ')
# a = int(input())  #чтобы введенные данные сохранились, напр в знач а
# #print(a)
# b = int(input ('Введите второе число: '))

# # #сумма чисел

# print(a, '+', b, '=', a + b)  #сложились строки, сумма не получилась, но после введения int на строках 41 и 43 получилась сумма


#ПРИВЕДЕНИЕ ТИПОВ
# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# #c = int(c)
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# #c = int(c)
# print(c)
# print(type(c))

# v = 'fgfjg'
# v = int(v)  #ошибка, т.к. нельзя 'fgfjg' вывести в int

# #ОКРУГЛЕНИЕ
# a = 5.7698
# b = 6.098948
# print(round(a*b, 2))

# #СОКРАЩЕНИЯ
# iter = 2
# iter += 3 #iter = iter + 3
# iter -= 4 #iter = iter - 4
# iter *= 5 #iter = iter * 5
# iter /= 5 #iter = iter / 5
# iter //= 5 #iter = iter // 5
# iter %= 5 #iter = iter % 5
# iter **= 5 #iter = iter ** 5

#ЛОГИЧЕСКИЕ
# a = 1 > 4
# print(a)     #выводится false
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 4
# print(a)
# a = 1 != 4
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10  #true
# print(a)
# a = 1 < 3 < 3 < 10  #false
# print(a)

# # IF  IF-ELSE
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, Маша!')
# elif username == 'Марина':
#     print('Я так ждала тебя, Марина')
# elif username == 'Ильнар':
#     print('Ильнар топ')
# else:
#     print('Привет, ', username)

# # Цикл While
# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)

# Конструкция While-else
# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит')
# print(i)

# # вместо break использовать ФЛАЖОК
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# FOR для строки
# a = 'qwerty'
# #print(a[0])
# for i in a:
#     print(i)

#Вложенные циклы
# line = ""
# for i in range(5):  #последовательность из 5 чисел, значит цикл выполнится 5 раз
#     line = ""
#     for j in range(5):
#         line += "*"  # к пустой строке 5 раз прибавим *
#     print(line)

# text = 'Съешь еще этих мягких французских булок'
#print(len(text))  #узнать размер строки
#print('еще' in text)  #есть ли 'еще' в text   true/false
#print(text.lower())   # перевод всех букв в нижний регистр
#print(text.upper())  # перевод всех букв в ВЕРХНИЙ регистр
#print(text.replace('еще','ЕЩЁ'))  # замена символов в text

# СРЕЗЫ - для более удобной работы со строкой
text = 'Съешь еще этих мягких французских булок'
# print(text[0])                                    #с
# print(text[1])                                    #ъ
# print(text[len(text) - 1])                        #к
# print(text[-1])
# print(text[-5])                                   # 5-й элемент с конца б
# print(text[:])                                    #выводится всё - Съешь еще этих мягких французских булок
# print(text[:2])                                   # элемент с 0-2 (2 не вкл)
# print(text[len(text) - 2:])                       # весь текст, с конца 2 = ок
# print(text[2:9])                                  # со 2 по 9 (ешь еще)
# print(text[6:-18])                                #начинаем на 6 элементе и заканчиваем на 18 с конца (еще этих мягких)
# print(text[0:len(text):6])                        #идем от 0 до конца строки с шагом 6 (вывод каждого 6-го элемента)
# print(text[::6])                                  #то же, если не указываем начальный и конечный элемент, то с начала и до конца с шагом 6
text = text[2:9] + text[-5] + text[:2]            #сначала эл 2-9, затем с конца 5-й, затем первые 2 буквы
print(text)