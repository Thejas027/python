class Animal():
      
      def __init__(self,name):
            self.name = name
      
      def speak(self):
            raise NotImplementedError("sub class need to implement this abstract method")

class Dog(Animal):
      def speak(self):
            return self.name + " says WOOF!"

class Cat(Animal):
      def speak(self):
            return self.name + " says MEOW!"
      

my_dog = Dog('fido')
print(my_dog.speak())
my_cat = Cat('Isis')
print(my_cat.speak())