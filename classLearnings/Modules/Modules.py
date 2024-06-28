
'''
Collections module 
      --> Counter 
'''
from collections import Counter

my_list = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 'a', 'a', 'a']
counts1 = Counter(my_list)
# print(counts1)

counts2 = Counter('aaaaaabbbbbbbbbssssss')
# print(counts2)


sentence = "How many times does a each word show up in this sentence with a word"

counts3 = Counter(sentence.lower().split())
# print(counts3)

# print(counts2.most_common())  # gives the Tuple 

'''
      --> Default dict
            --> assigns a default values if there is a instances if a key error has occurred 
'''

from collections import defaultdict

d = defaultdict(lambda:0)

d['a'] = 10
d['b'] = 20

# print(d['a'])
# print(d['c']) # here c is not assigned when this is made to print,it does not gives error instead this gives 0, default value assigned



'''
      --> named tuple 
'''

# from collections import namedtuple

# Dog = namedtuple('Dog',['age','breed','name'])
# sammy = Dog( age=5 , breed='Husky' , name='sam' )
# print(sammy)
# print(sammy.age)
# print(sammy.breed)
# print(sammy.name)


'''
Os Module 
'''

import os
# print(os.getcwd())   # gives the path of current directory 
# print(os.listdir())  # lists all the files form current directory 

# import shutil # used to move the folder 
# shutil.move('source path' , 'destination path') # syntax of this move command 

'''
      --> to delete the files 
            1) os.unlink(path) -> which deletes the file at that path 
            2) os.rmdir(path) -> which deletes the folder at that path 
            3) shutil.rmtree(path) --> removes all the files and folders contained at that path (dangerous)       
                  --> Once deleted this cannot be recovered once again 
            
            To avoid this install (send2trash) package and import it.
'''

# import send2trash
# send2trash.send2trash('path')  # to delete it 

# usage of walk 
      # used to look in deeply with any directory 

# for folder,subfolders,files in os.walk(os.getcwd()):
#       print('\ncurrently looking at {}\n'.format(folder))
      
#       print('\nThe sub folders are : ')
#       for sub_fold in subfolders:
#             print(f'\t sub folders : {sub_fold}\n')
#       print('\n')
      
#       print('\nThe fils are : ')
#       for f in files:
#             print(f'\tfiles : {f}\n')
#       print('\n')
      
      
      
#       print(files)



'''
Date and time module 
'''

import datetime

# my_time = datetime.time('hour','min','sec','microsecond') # syntax

my_time = datetime.time(2,20,30,80)
my_time.hour
my_time.minute
my_time.second
my_time.microsecond

# print(my_time)

# date 
today = datetime.date.today()
# print(today)

      # add these below to print statement to get output in terminal 
      
# today.year
# today.month
# today.day

# print(today.ctime())

######
from datetime import datetime

my_datetime = datetime(2024,6,10,22,52)
# print(my_datetime)

# to replace any value 

my_datetime = my_datetime.replace(year=2025)
# print(f"Updated date and time : {my_datetime}")


'''
      Python debugger 
'''

# import pdb

# x = [1,2,3]
# y = 10 
# z = 20

# print(y+z)

# pdb.set_trace()

# print(x+y)

'''
Regular expressions 
'''
import re

address = 'Hey I live in Mysore, and 080-123-4567 its my number'

phone =  re.search( r'(\d{3})-(\d{3})-(\d{4})',address) # Here it shows how re and quantifiers are used 
# print(phone)
# print(phone.group())
# print(phone.group(1)) 

# usage of or operator in Regular expression 

text = 'The cat is here'
result = re.search('cat|dog',text)
# print(result)

result = re.search('.at','The cat in the hat sat there.')


''' 
      Time your python code
            --> Timeit module  
'''

def func_one(n):
      return [str(num) for num in range(n)]

print(func_one(10))

def fun_two(n):
      return list(map(str,range(n)))

print(fun_two(20))

# both the above two functions give the same result to know which is efficient --> USE timeit module 

import time 
#  CURRENT TIME BEFORE 
start_time = time.time()
# RUN CODE 
result = func_one(100000)
# CURRENT TIME AFTER RUNNING CODE 
end_time = time.time()
#ELAPSED TIME 
elapsed_time = end_time - start_time
print(f'The diff between start and end time of a time module -  1 : {elapsed_time}')

################################for function two 
#  CURRENT TIME BEFORE 
start_time = time.time()
# RUN CODE 
result = fun_two(1000)
# CURRENT TIME AFTER RUNNING CODE 
end_time = time.time()
#ELAPSED TIME 
elapsed_time2 = end_time - start_time
print(f'The diff between start and end time of a time module - 1 : {elapsed_time2}')


####### USING TIMEIT 

import timeit

timeit.timeit

stmt = ''' 
func_one(100)
'''

setup = '''
def func_one(n):
      return [str(num) for num in range (n)]
'''

elapsed_timeit = timeit.timeit(stmt,setup,number=1000)
print( "Elapsed time for function - 1 :  {}".format(elapsed_timeit))

# For function 2 

stmt2 = '''
fun_two(100)
'''
setup2 = '''
def fun_two(n):
      return list(map(str,range(n)))
'''

elapsed_timeit2 = timeit.timeit(stmt2,setup2,number=1000)
print( "Elapsed time for function - 2 :  {}".format(elapsed_timeit2))


'''
Zipping and unzipping of files 
'''

