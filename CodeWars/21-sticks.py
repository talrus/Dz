'''
In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. The last person to take a stick wins. Like this:
'''
def make_move(sticks):
    return sticks % 4 or 1