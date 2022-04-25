from Rectangle import Rectangle

class Surface:
  def __init__(self, filename= "", x=0, y=0, h=0, w=0):
    """the constructor for Surface class,takes filename, x, y, height, and width as parameters and stores them as instance variables
    self: (str)  represent an instance (object) of the given class
    filename: (str) represents the name of the file
   x: (int) x value inputted into the code
    y: (int) y value inputted into the code
    h: (int) height value inputted into the code
    w: (int) width value inputted into the code
    return: None"""
    self.rect = Rectangle(x, y, h, w)
    self.image = filename

  def getRect(self):
    """represents the rectangle object being returned 
      self: (str)  represent an instance (object) of the given class
    return: (str) returns the rectangle object"""
    return self.rect

