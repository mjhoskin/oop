# 1. Expand the Coord class from Exercise 5 by adding a magic method for __add__.
#     1.1. This should accept one other argument, another object of the same class, and return a new object - the original values added to those of the other object
#     1.2. Ensure that the method will only be able to add Coords to Coords, and velocities to velocities, by adding in assert statements as above.
#     1.3. Add __radd__ and __iadd__ methods which call the main __add__ method. While __radd__ at current isn't very useful by itself as only the Coord family of classes can be added, if the original __add__ method was expanded to allow numerical collections of length 3 as an input, reflecting the original method will allow addition in either direction. 
# 2. Expand the Velocity class to be able to multiple it with a singular numerical time value using __mul__.
#     2.1. This should return a Coordinate with values equal to those of the original Velocity object multiplied by the time.
# 3. Test the classes. 
#     3.1. Create two Coord objects with different numerical values. Test out adding them together. 
#     3.2. Create a Velocity object. Test adding it to the Coord objects.
#     3.3. Test the addition of a Coord object, with the results of multiplying the Velocity object by a time value.  

import math

class Coord():
    
    def __init__(self, x, y, z):
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
        
        #return("Coord({0},{1},{2})".format(self.x, self.y, self.z))
        return("{0}({1},{2},{3})".format(self.__class__.__name__, 
                                         self.x, 
                                         self.y, 
                                         self.z)) 
        
    def __eq__(self, other):
        """
        Method to handle == comparisons. Returns True if attributes are the same AND if the class name is the same
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to compare to. 
            
        Returns
        -------
        bool: Whether two objects are identical
        
        Notes
        -----
        comparing a Coord with a child of Coord will return False, regardless of the numbers involved.
        """
        
        equivalence = (self.__dict__ == other.__dict__) and \
                      (self.__class__.__name__ == other.__class__.__name__)
        
        return equivalence
    
    def __ne__(self, other):
        """
        Method to handle != comparisons. Returns True if attributes are not the same OR if the class name is not the same
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to compare to. 
            
        Returns
        -------
        bool: Whether two objects are not identical 
        
        Notes
        -----
        comparing a Coord with a child of Coord will return True, regardless of the numbers involved.
        """        
        equivalence = (self.__dict__ != other.__dict__) or \
                      (self.__class__.__name__ != other.__class__.__name__)
        
        return equivalence
    
###    
### Question 1 Below
###
        
    def __add__(self, other):
        """
        Method to add a second set of Coordinates 
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to add on
            
        Returns
        -------
        Coord: sum of self and other
        
        Notes
        -----
        Will thrown an assertion error if two objects are not both Coords, or identical children of Coord
        
        """
        
        assert isinstance(other, self.__class__), \
            "objects to be added must be {0}, rather than {1}".format(self.__class__.__name__, type(other))
        assert isinstance(self, other.__class__), \
            "objects to be added must not be children of {0}, they must be {0}".format(self.__class__.__name__)
                
        delta_x, delta_y, delta_z = other.values()

        return(Coord(self.x + delta_x, 
                     self.y + delta_y, 
                     self.z + delta_z))

    def __radd__(self, other):
        """
        Reflective addition - calls Coord.__add__
        """
        
        return self.__add__(other)
    
    def __iadd__(self, other):
        """
        Assignment addition - calls Coord.__add__
        """        
        return self.__add__(other)
    
    def __lt__(self, other):
        """
        Handles comparisons between self and other for less than
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to compare to
            
        Returns
        -------
        bool: True if abs(self) is less than abs(other)
        
        Notes
        -----
        Evaluates to False if names of classes are different
        """
        comparison_result = self.hypotenuse() < other.hypotenuse()
        
        if self.__class__.__name__ != other.__class__.__name__:
            comparison_result = False
        
        return comparison_result
        
    def __le__(self, other):
        """
        Handles comparisons between self and other for less than or equal to
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to compare to
            
        Returns
        -------
        bool: True if abs(self) is less than or equal to abs(other)
        
        Notes
        -----
        Evaluates to False if names of classes are different
        """        
        comparison_result = self.hypotenuse() <= other.hypotenuse()
        
        if self.__class__.__name__ != other.__class__.__name__:
            comparison_result = False
        
        return comparison_result
    
    def __gt__(self, other):
        """
        Handles comparisons between self and other for greater than
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to compare to
            
        Returns
        -------
        bool: True if abs(self) is greater than abs(other)
        
        Notes
        -----
        Evaluates to False if names of classes are different
        """          
        comparison_result = self.hypotenuse() > other.hypotenuse()
        
        if self.__class__.__name__ != other.__class__.__name__:
            comparison_result = False
        
        return comparison_result    
    
    
    def __ge__(self, other):
        """
        Handles comparisons between self and other for greater than or equal to
        
        Parameters
        ----------
        other: Coord
            Secondary Coordinate to compare to
            
        Returns
        -------
        bool: True if abs(self) is greater than or equal to abs(other)
        
        Notes
        -----
        Evaluates to False if names of classes are different
        """        
        comparison_result = self.hypotenuse() >= other.hypotenuse()
        
        if self.__class__.__name__ != other.__class__.__name__:
            comparison_result = False
        
        return comparison_result
    
###    
### Question 2 Below
###
    
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
        
    def __mul__(self, t):
        """
        Method for handling multiplication of object
        
        Parameters
        ----------
        t: float/int
            time value to multiple Velocity by to get a position
            
        Returns
        -------
        Coord: Coordinate = Velocity * time
        """        
        return(Coord(self.x * t, 
                     self.y * t, 
                     self.z * t))
    
    
###    
### Question 3 Below
### 
Coord_1 = Coord(1,2,3)
Coord_2 = Coord(3,4,5)

print((Coord_1 + Coord_2).values())

vel = Velocity(4,5,6)

print((vel * 5 + Coord_2).values()) 
print((vel + Coord_2).values()) #expect an AssertionError

