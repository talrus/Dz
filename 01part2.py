x = 3715
lst_of_int = [int(i) for i in str(x)]
print(lst_of_int)

res = 1
for i in lst_of_int:
    res *= i

print(res)
#----------------------------------------------------------------------------------
x2 = str(x)[::-1] # convert to string and reverse with slice feature
print(x2)
#----------------------------------------------------------------------------------
print(sorted(lst_of_int))
#----------------------------------------------------------------------------------
#part03
x = 23
y = "45"
x, y = y, x
print(f"x -- {x} \t y -- {y}")