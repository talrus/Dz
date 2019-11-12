# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)


# 5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# # -----------------------------------------------
#                   #3_factorial
# def factorial(n):
#     res = 1
#     if n < 2:
#         return 1
#     else:
#         for i in range(2, n+1):
#             res *= i
#         return res
# n = int(input("Enter number for factorial:\n"))
# print(factorial(n))

# # -----------------------------------------------
#                   # 1__list_of_nummbers
# num = int(input("Enter amount of numbers:\n"))
# list_of_numbers = [int(input("Enter your numbers: \n")) for _ in range(num)]
# print(f"The maximum number is {max(list_of_numbers)}\nThe minimum number is {min(list_of_numbers)}")

# # -----------------------------------------------
#                   #2_Even_and_Odd
# print(f"Multiply two : {[x for x in range(1, 11) if x % 2 == 0]}")
# print(f"Multiply two and three: {[x for x in range(1, 11) if x % 2 == 0 and x % 3 == 0 ]}")
# print(f"The Numbers that are not divisible by two and three: {[x for x in range(1, 11) if not (x % 2 == 0 or x % 3 == 0)]}")

# # -----------------------------------------------
#                   #4__Login_verification_script
# while True:
#     login = input("Enter your account login:\n")
    
#     if  login == "First":
#         print("First, Welcome!")
#         break

#     elif login == 'Idk': break

#     else : print("Try again or write 'Idk' to exit.")

# # -----------------------------------------------
#                   #5_The_first_case

# while True:
#     if int(input("Enter number that more than 0 or you will break me ^_^ :\n")) <= 0:
#          break

# # -----------------------------------------------
#                   #6_The_Second_case
# num = int(input("Enter amount of numbers:\n"))

# for i in range(num):
#     if int(input("Enter a number:\n")) <= 0:
#         break
# else: print("All number has written.")

