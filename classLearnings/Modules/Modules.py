
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

import pdb

x = [1,2,3]
y = 10 
z = 20

print(y+z)

pdb.set_trace()

print(x+y)