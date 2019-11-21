'''
Create a class Ball.

Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
'''

class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type