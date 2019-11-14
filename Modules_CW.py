from random import randint
import math
'''
  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
'''
def script_game():
	'''
	start game 'Try guess my number'
	'''
	x = randint(1, 101)
	while True:
		number = int(input("Try to guess my number:\n"))
		if number == x:
			print("Congratuation! You win!!!")
			break
		elif number < x: print("My number is greater!")
		elif number > x: print("My number is smaller!")

script_game()

#-----------------------------------------------------------
def area_of_triangle():
	''' 
	Calculate area of triangle
	'''
	height = float(input("Enter height of triangle:\n"))
	a = float(input("Enter the size of triangle base:\n"))
	
	return 0.5 * height * a

def area_circle():
    '''
    Calculate the area of circle
    '''
    radius = float(input("Enter radius of circle:\n"))

    return  math.pi * math.pow(radius ,2)

def area_rectangle():
    """
    Calculate the area of rectangle
    """
    side_a = float(input("Enter the first side:\n"))
    side_b = float(input("Enter the second side\n"))
    return side_a * side_b