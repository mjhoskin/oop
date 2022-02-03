#1. Adapt the Coord class to use the dataclass decorator. 

from dataclasses import dataclass
import math

@dataclass
class Coord():
    
#     x : float #for question 1 this is perfectly fine
#     y : float
#     z : float


#2. Convert x, y, and z to be properties with suitable get and set methods.
#    2.1. The set method should check to make sure the value being set is not a string. 

    _x : float #for question 2 onwards, having these as hidden works better for the properties
    _y : float
    _z : float

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @x.setter
    def x(self, value):
        if isinstance(value, str):
            raise ValueError('x cannot be a string!')
        else:
            self._x = value
    
    @y.setter
    def y(self, value):
        if isinstance(value, str):
            raise ValueError('y cannot be a string!')
        else:
            self._y = value
    
    @z.setter
    def z(self, value):
        if isinstance(value, str):
            raise ValueError('z cannot be a string!')
        else:
            self._z = value  

#3. Adapt the Coord class to allow the values to change when called by implementing a __call__ method. 
            
    def __call__(self, x, y, z):
        """
        Used to reassign the values of the object, method allows object(x,y,z) to overwrite existing values
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
        comparison_result = self.hypotenuse() >= other.hypotenuse()
        
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
 
c = Coord(1,2,3)

c(2,3,4)
print(c.values())

c(21,31,41)
print(c.values())

c('21','31','41') #expect ValueError