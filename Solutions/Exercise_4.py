# 1. Expand the Coord class from Exercise 3 by adding docstrings where methods either take inputs which are not self, or return an output. Do this for Velocity, and all future methods going forwards.
# 2. Further expand Coord by adding a __repr__ method.
#     2.1. This should just return the code required to recreate the object.


import math

class Coord():
    
    def __init__(self, x, y, z=0):
        """
        Initialises the object and sets some object wide attributes
        
        Parameters
        ----------
        x: float
            value along x axis
        y: float
            value along y axis
        z: float, optional
            value along z axis. Defaults to 0
        """
        
        self.x = x
        self.y = y
        self.z = z
        
    def hypotenuse(self):
        """
        Returns the hypotenuse calculated from the Coordinate points
        
        Returns
        -------
        float: sqrt(x^2 + y^2 + z^2) 
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def values(self):        
        """
        Returns the values of the Coordinate
        
        Returns
        -------
        tuple(float, float, float): (x,y,z) 
        """
        return(self.x, self.y, self.z)
    
    def __repr__(self):
        """
        Specialised technical string to allow the recreation of the object. 
        
        Returns
        -------
        str: call needed to recreate object
        """
        
        return("{0}({1},{2},{3})".format(self.__class__.__name__, 
                                         self.x, 
                                         self.y, 
                                         self.z))   
    
class Velocity(Coord):
    
    def __init__(self, x, y, z):
        """
        Initialises the object and sets some object wide attributes
        
        Parameters
        ----------
        x: float
            speed in x direction
        y: float
            speed in y direction
        z: float
            speed in z direction
            
        Notes
        -----
        Calls parent Coord class init method.
        
        """
        Coord.__init__(self, x, y, z)

        
# 3. Create both a Coord and a Velocity object. Test running str() and print on them both.  
#     3.1. Does the Velocity object return the correct values? If not, try using self.__class__.__name__ in the __repr__ method.   
pos = Coord(2,3,4)
vel = Velocity(5,1,2)

print(str(pos))
print(pos)
print(str(vel))
print(vel)


### By using self.__class__.__name__ in the __repr__method, python handles inheritance very well. 
### While __class__.__name__ gives the value of Coord while used in the Coord class, when inherited, 
### the name of the child class takes precedence and is used instead. This allows the single repr method
### to handle both the parent Coord, and the child Velocity, classes. 
