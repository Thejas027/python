

# Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.
try:
      for i in ['a', 'b', 'c']:
            print(i**2)
except TypeError:
      print("Its a type error")
finally:
      print("End of program ")


### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

x = 5
y = 0

try:
      result = x/y
      print(f"the result : {result}")
except:
      print("Division by zero in not possible")
finally:
      print("All Done!")
      

### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

def ask_int():
      while True:
            try:
                  n = int(input("Enter a number to find the square of a number : "))
                  square_n = n **2
                  print(f"The square of {n} is : {square_n}")
                  break
            except:
                  print("Its not an integer value what u have entered. Try again!!")
                  continue

ask_int()





