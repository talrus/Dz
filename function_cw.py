# '''
# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
# 2.  Написати функцію, яка повертає абсолютне значення числа
# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
# '''
def opt_arith_means(*args):
    return sum(args)/len(args)

# lst_of_num = input("Enter your list of numbers:\n")
 
# lst = lst_of_num.split(',')
# y = [int(x) for x in lst]

# n = int(input("Enter amount of numbers:\n"))
# y = [int(input("Enter a number:\n")) for _ in range(n)]
# print(opt_arith_means(*y))
#------------------------------------------------------------------
def absolute_value(number):
    return number if number > 0 else -number

#print(absolute_value(-55))
#------------------------------------------------------------------
def my_max_number(first, second):
    '''
    finding the maximum number
    '''    
    return first if first > second else second
#print(my_max_number(8, 99))

def square_circle(num, *args):
    PI = 3.14 
    radius = int(input("Enter radius of circle:\n"))
