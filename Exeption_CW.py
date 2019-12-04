'''
Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
'''
'''
Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
 Головний код має викликати функцію, яка обробляє введену інформацію.
'''
"""
3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому,
 передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
 Використати блоки else та finaly.

4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
кий відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.
"""
def Weekday():
    try:
        list_of_week = ['Monday', 'Thuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        number = int(input("Enter number of week 1-7:\n"))
        if number not in range(1,8): 
            raise ValueError("Only 1-7 number not more or less")
    except TypeError as t:
         print(t)
    except ValueError as v:
         print(v)
    except: 
        print("Someting went wrong")
    else: 
        print(list_of_week[number-1])
    

def DivExeption():
    try:
        a, b = input("Enter two numbers separated by commas\n").split(',')
        print(f"a : {a}, b: {b}")
    except ZeroDivisionError as e:
        print(e)
    except SyntaxError as s:
        print(s)
    except Exception:
        print('Something went wrong.')
    else: print('No exception')
    finally : print('I am always execute ^_^')

def MyExeption():
    try:
        age = int(input("Please enter your age: \n"))
        if age <= 0 : raise Exception("Please enter positive integer")
        elif age % 2 ==0 : print(f'{age} is even number.')
        else : print(f"{age} is odd number")
    except ValueError as e:
        print(e)
    return age
# try:
#     number = int(input("Enter integer number\n"))
#     if number % 2 ==0 : print(f'{number} is even number.')
#     else : print(f"{number} is odd number")
# except ValueError as e:
#     print(e)

#age = MyExeption()
#MyExeption()
#DivExeption()
Weekday()
