'''
      --> used to generate the sequence of values over the time. 
      --> it allow us to send back the value and then later to resume to pick up where it left off.
      -->  Here it shows how to create an OWN generator function 
      
'''

#   here is how the yield key word can be used in python, while returning from the function 

#  Generator function to find the cube of a number till the range is provided 
def create_cube(n):
      for x in range(n):
            yield x**3    # if return key word is used it gives error that int object is not iterable 
            

# for x in create_cube(10):
#       print(x)
      

# Generator function for fib series 

def generate_fib(n):
      first = 0
      second = 1
      
      for i in range(n):
            yield first 
            first,second = second, first+ second
            
# for fib in generate_fib(5):
#       print(fib )


'''
Generators questions 
'''

#  To generate a square number 

def generate_square(n):
      for i in range(n):
            yield i**2


# n = int(input('Enter the n value to generate the squares of a number :'))

# for squares in generate_square(n):
#       print(squares)
      

# To generate a random number between a given range 

# import random

# def generate_random(low,high,n):
#       for i in range(n):
#             yield random.randint(low,high)


# low = int(input("Enter a starting range of low value : "))
# high = int(input("Enter a last value of range :  "))
# n = int(input("Enter the n value(For how many times this should run) : "))
# for i in generate_random(low,high,n):
#       print(i)


