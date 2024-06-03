class Animal():
      def __init__(self):
            print("Animal created")
      
      def who_am_i(self):
            print("I am an animal")
      
      def eat(self):
            print("I am eating")
            
# my_animal = Animal()
# my_animal.eat()
# my_animal.who_am_i()


### A Dog class where its get inherited from animal
### The above base class methods can be over ridded

class Dog(Animal):
      def __init__(self):
            Animal.__init__(self)
            print('Hey ! Dog created')
            
my_dog = Dog()
