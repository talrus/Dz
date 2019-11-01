from random import randint
# i = 100
# while i > 1:
#     print(i, end=" ")
#     i -= 2
#--------------------------------------------------------------
# for i in range(0, 100, 2):
#    print(i) 
#--------------------------------------------------------------
# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)
#--------------------------------------------------------------
# for i in range(1, 100, 1):
#     print(i)
#--------------------------------------------------------------
#lst = [i for i in range(1, 99, 2)]
# lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# for x in lst:
#     if x % 2 == 0:
#         print("Yes, list the contains odd numbers.")
#         break
# else : print("No, list the contains only even numbers.")
#--------------------------------------------------------------
# for i in range(len(lst)):
#     lst[i] = float(lst[i])
# print(lst)
#--------------------------------------------------------------
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# x = int(input('Enter number:\t'))
# print(list(fib(x)))
#--------------------------------------------------------------
# lst = ['1', '2', '3', '4']
# for x in lst:
#     print(x + "#")

# x = int(input('Enter your number:\t'))
#--------------------------------------------------------------
# for i in range(x):
#     if i > 1 and i < x:
#         if x % i == 0:
#             print("The number not is simple.")
#             break
# else: print("The number is simple.")
#--------------------------------------------------------------
# number = randint(0, 99999)
# lst_of_digits = [int(x) for x in str(number)]
# print(max(lst_of_digits))
#--------------------------------------------------------------
word = input("Enter your word\n")

for i in range(len(word)):
    if word[i] != word[-1-i]:
        print("The word is not palindrom.")
        break
else : print('The word is palindrom')

