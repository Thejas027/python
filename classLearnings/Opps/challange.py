
#### Problem 1

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
import math
class Line():
      def __init__(self,coor1,coor2):
            self.coor1 = coor1
            self.coor2 = coor2
      
      def distance(self):
            x = (self.coor1[0] - self.coor2[0]) 
            y = (self.coor1[1] - self.coor2[1]) 

            
            d = math.sqrt(x**2 + y**2)
            return d
      
      def slope(self):
            m1 = self.coor2[1] - self.coor1[1]
            m2 = self.coor2[0] - self.coor1[0]
            
            return m1/m2
            
      
co1 = (3,2)
co2 = (8,10)
# print(co1[0])
li = Line(co1,co2)
print( "the distance between the points : ",  li.distance())
print( "the slope of a given coords : " ,  li.slope())