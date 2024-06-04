
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
# print( "the distance between the points : ",  li.distance())
# print( "the slope of a given coords : " ,  li.slope())




###

# cylinder class to find the volume and  surface area

class cylinder():
      
      pi = 3.14
      
      def __init__(self,height =1 , radius = 1):
            self.height = height
            self.radius = radius
      
      def volume(self):
            return self.pi * self.radius**2 * self.height
                  
      def surface_area(self):
            return 2 * self.pi * self.radius * (self.height + self.radius)
      
# ci = cylinder(2,3)
# print("the volume of a sphere : ",ci.volume())
# print("the surface area of sphere : ",ci.surface_area())




class Bank():
      def __init__(self, owner, balance=0):  # Added default balance of 0
            self.owner = owner
            self.balance = balance
      
      def deposit(self):      
            dep = int(input("Enter the amount to be deposited: "))
            self.balance += dep
            print("Amount deposited.")
            return self.balance

      def withdraw(self):  # Renamed to withdraw for consistency
            amt = int(input("Enter the amount to withdraw: "))

            if amt > self.balance:
                  print("Insufficient funds!!")
                  return
            else:
                  self.balance -= amt
                  print(f"Available balance: {self.balance}")

acc1 = Bank('Abc', 100)
# acc1.deposit()  # Now correctly calls the deposit method
# print(acc1.balance)  # To see the updated balance after deposit

acc1.withdraw()  # Uncomment this line to test the withdraw functionality
