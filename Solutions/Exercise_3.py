# 1. Expand the Coord class from Exercise 2 by adding a method called values.
#     1.1. This should just return the values of x, y, and z.

import math

class Coord():
    
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def hypotenuse(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def values(self):
        return(self.x, self.y, self.z)
    
    
# 2. Create a new class called Velocity.
#     2.1. This should inherit from the Coord class, and it's initialisation should call that of the parent class. 
class Velocity(Coord):
    
    def __init__(self, x, y, z):
        Coord.__init__(self, x, y, z)

        
# 3. Create a Velocity object called vel with values of 2, 4, and 6 for x, y, and z respectively.
#     3.1. Call the values method of vel to check the numbers have been assigned correctly. 
vel = Velocity(2, 4, 6)      
vel.values()