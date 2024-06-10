'''
In python decorators are use to modify the functions, they provide wrapping another function or method in order to extend its behavior without permanently modifying it.
'''

def new_decorator_func(org_func):
      
      def wrap_func():
            print('\nCode before the original function call.\n')
            org_func()
            print('Code after the original function call.\n')
            
      return wrap_func

@ new_decorator_func
def other_decorator_func():
      print('Decorated!!, Original function called form other decorator function to new decorator function.\n')

# calling of function 

other_decorator_func()