'''
If the tail is right return true, else return false.

The arguments will always be strings, and normal letters.

For Haskell, body has the type of String and tail has the type of Char. For Go, body has type string and tail has type rune.
'''
def correct_tail(body, tail):
     return True if tail == body[-1] else False