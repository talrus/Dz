'''
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus.
wait is the number of people waiting to get on to the bus.

'''

def enough(cap, on, wait):
    return 0 if cap >= on + wait else abs(cap - on - wait)