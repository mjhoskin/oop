#1. Expand the Coord class created in Exercise 1 by adding a method called hypotenuse.
#    1.1. This should return the value of $\sqrt{x^2 + y^2}$  - the distance from the origin.
#    1.2. NOTE: The default math library includes a sqrt() function.  

import math

class Coord():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
              
    def hypotenuse(self):
        return math.sqrt(self.x**2 + self.y**2)

#    1.3. Create an object with an x of 5, a y of 13, and display the hypotenuse.  

location = Coord(5, 12)
print(location.hypotenuse())
    
#2. Add a z attribute with a default value of 0
class Coord():
    
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
              
    def hypotenuse(self):
        return math.sqrt(self.x**2 + self.y**2)
    
#3. Include this value in the hypotenuse calculation - $\sqrt{x^2 + y^2 + z^2}$
class Coord():
    
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
              
    def hypotenuse(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    
#    3.1. Create an object with x and y values of 4, and a z of 7, and display the hypotenuse.  
location = Coord(4, 4, 7)
print(location.hypotenuse())