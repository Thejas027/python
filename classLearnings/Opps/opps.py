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



class Book():
      
      def __init__(self,title,author,page):
            
            self.title = title
            self.author = author
            self.page = page
            
      def __str__(self):
            return f"{self.title} by {self.author}"

      def __len__(self):
            return self.page

      def __del__(self):
            print("The book object has been deleted")
      
b = Book('Python rocks','Jose',200)

# print(b)
result = str(b)
# print(result)

page_res = len(b)
print(page_res)

del b   # used to delete the created object 
# print(b)  # it gives op as 'not defined'
