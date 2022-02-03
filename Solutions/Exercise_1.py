#1. Create a **`Coord`** class, where the initialisation method should take an x and y value.
#    1.1. Ensure that the initialised x and y values are stored as **`self.`** variables.
class Coord():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
#2. Create a **`Coord`** object called **`location`** with a numerical **`x`** and a numerical **`y`** value.      
location = Coord(2,3)

#3. Print the value of $x^2 + y^2$.
print(location.x**2 + location.y**2)
# or:
print(pow(location.x,2) + pow(location.y, 2))
