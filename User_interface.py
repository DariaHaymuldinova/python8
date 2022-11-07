from os import system
system('cls')

def user_choice():
    while True:
        user_input = input('''
        1 - вывод ID, 2 - вывод ФИО 
        3 - вывод ДР, 4 - вывод успеваемости
        5 - вывод пола, 6 - вывод всех данных
        0 - выход\n
Выберите действие: ''')
    user_input = int(user_input)
