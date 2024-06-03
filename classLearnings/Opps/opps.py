class Dog():
      
      # class attributes
      # same for any instance of class
      
      species = 'mammal'
      
      #attributes
      def __init__(self,breed,name,):
            self.breed = breed
            self.name = name
      
      # method defining 
      def bark(self,number):
            print('WOOF!! My name is {} and the number is {}'.format(self.name,number))
            
            
my_dog = Dog('German shepard','Tommy')
my_dog.bark(20)
print(my_dog.breed,my_dog.name)


###### Another example of a class 

class circle():
      
      pi = 3.14
      
      # def __init__(self,radius):
            # self.radius = radius
            
      ## method 
      def get_circumference(self,radius):
            return radius * self.pi * 2

my_circle = circle()

# my_circle.radius = 100
print(my_circle.get_circumference(100))