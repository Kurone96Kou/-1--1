"""Формулировка задачи"""

z2 = \
    "Задание 2. С клавиатуры вводится текст, содержащий слова с повторяющимися буквами. \n"\
    "Удалить все повторения, оставив по одной букве\n\n"\
    "Для проверки Вы можете использовать данную строку: \n"\
    "Pythooon iiisss tttheee BBeesttt Softwaree \n"

def delete_duplicates(str): ## функция удаляет дубликаты. Отправляем ей нашу строку
    news = '' ##новая пустая строка, которая будет принимать символ
    for i in range(len(s) - 1): # посимвольно пробегаем по нашей строке
                                # len(s) возвращает нам длину строки int, а потом range() нам это число раскладывает
        if s[i] != s[i + 1]: # если проверяемый символ не равен следующему,
            news += s[i] # то отдаем его в новую строку
    if s[-1] != news[-1]: ## s[-1]  - последний символ в строке. Если в исходной строке последний символ не равен
                        ## последнему символу в новой,
        news += s[-1]    ##то в новой записываем последний этот символ
    return news # возвращаем новую строку

print(z2)
s = input("Введите строку символов, буквы в которой должны поторяться:")

print("Исходная строка: " +s)
s = delete_duplicates(s) ##вызываем функцию
print ("Преобразованная строка: "+s)
input("Введите ENTER, чтобы завершить работу")



