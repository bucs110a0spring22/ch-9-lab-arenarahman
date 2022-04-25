class Rectangle:
  def __init__(self, x=0, y=0, h=0, w=0):
    """the constructor for Rectangle class,takes x, y, height, and width as parameters and stores them as instance variables
    self: (str)  represent an instance (object) of the given class
    x: (int) x value inputted into the code
    y: (int) y value inputted into the code
    h: (int) height value inputted into the code
    w: (int) width value inputted into the code
    return: None"""
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    if self.x < 0:
      self.x = 0
    elif self.y < 0:
      self.y = 0
    elif self.height < 0:
      self.height = 0 
    elif self.width < 0:
      self.width  = 0
  
  def __str__(self):
    """represents the class objects as strings
     self: (str)  represent an instance (object) of the given class
    return: (str) returns a string containing the x, y, width, and height of the rectangle."""
    return "(x:" + str(self.x) + ", y:" + str(self.y) + ") width:" + str(self.width) + ", height:" + str(self.height) 
   
