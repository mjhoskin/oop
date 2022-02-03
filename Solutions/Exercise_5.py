# 1. Expand the Coord class from Exercise 4 by adding magic methods for __eq__ and __ne__. 
#     1.1. These should return True if the x, y, and z, values match for __eq__, and the oppposite for __ne__. 
#     1.2. They should also return False if the names of the two objects don't match - use self.__class__.__name__ to compare.  
# 4. Add methods for the following comparison operators to the Coord class: less than, <, less than or equal to, <=, greater than, >, and greater than or equal to >=
#     4.1. These should compare the absolute distance of the points under consideration. 
#     4.2. They should return an error if the names of the two objects don't match as in 1.2 - comparing a Velocity with a Coord is not a reasonable thing to do.
# 3. Test the classes. 
#     3.1. Create two Coord objects with different numerical values. Test out the comparison methods created above.
#     3.2. Create a Velocity object. Test comparing it with the Coord objects.


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

###    
### Question 1 Below
###
        
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
### Question 2 Below
###
    
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

print(Coord_1 > Coord_2) #expect False
print(Coord_1 < Coord_2) #expect True
print(Coord_1 == Coord_2) #expect False
print(Coord_1 != Coord_2) #expect True
print(Coord_1 >= Coord_2) #expect False
print(Coord_1 <= Coord_2) #expect True

vel = Velocity(4,5,6)

print(vel > Coord_2) #expect False
print(vel < Coord_2) #expect False
print(vel == Coord_2) #expect True
print(vel != Coord_2) #expect False
print(vel >= Coord_2) #expect False
print(vel <= Coord_2) #expect False
