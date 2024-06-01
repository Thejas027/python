

# # using of if , elif and else statements 
# num1 = 1000
# num2 = 200
# num3 = 30
# if num1 > num2 and num1 > num3 :
#       print(f"largest element : {num1}")
# elif num2 > num3 : 
#       print(f"largest element : {num2}")
# else :
#             print(f"largest element : {num3}")
            
# for loops usage

# my_list = [5,2,7 ]
# my_list.sort()
# for i in my_list :
#       # check for even number 
#       if(i % 2 == 0):
#             print(f"{i} is a even number")
#       else:
#             print(f"{i} is a odd number")
   
            
## while loop usage
# x = 0
# while x < 5:
#       print(f"the value of x :{x}")
#       x+=1

# def keyword usage 

# def add_fun(num1,num2) :
#       return num1 + num2

# result = add_fun(30,90)
# print(result)

# # it checks weather the number is even or not 
# def even_number(num) :
#       return num %2 ==0
      
      
# num1 =int(input("enter the num value to find weather its an even number or not :"))
      
# result = even_number(num1)
# if(result) :
#       print(f"{num1} is a even number")
# else:
#       print(f"{num1} is a odd number")
      
# # the below code checks for even number in a list 
# def even_check(my_list) :
#       for number in my_list :
#             if(number % 2 == 0):
#                   return True
#             else :
#                   pass
#             return False
# result = even_check([1,3,5,9])
# print(result)

# #  to returns the even number list form  given list 
# def check_even_number (my_list):
#       even_num = []
#       for number in my_list:
#             if(number % 2 == 0):
#                   even_num.append(number)
#             else:
#                   pass
#       return even_num

# res = check_even_number([1,2,3,4,5,6,7,8,9])
# print(res)

######
# # functions on tuples 

# stock_prices = [('apple',200),('orange',90),('grape',1200),('mango',150)]

# def fruits_rate (stock_prices):
#       current_max = 0
#       fruit_name = ''
      
#       for fname,hours in stock_prices:
#             if(hours > current_max):
#                   current_max = hours
#                   fruit_name = fname
#       return (fruit_name,current_max)

# result = fruits_rate(stock_prices)
# print(result)


#####
#shuffle list 

from random import shuffle

my_list = [' ', 'O', ' ']

def shuffle_list(my_list):
      shuffle(my_list)
      return my_list

def player_guess():
      guess =''
      while guess not in ['0','1','2']:
            guess =  input("Pick a number : 0 , 1 or 2 : ")
      return int(guess)

def check_guess(my_list,guess):
      if(my_list[guess] == 'O'):
            print("correct !")
      else:
            print("invalid ! Try again")
            print(my_list)

# shuffle list 
mixed_list = shuffle_list(my_list)

guess = player_guess()

check_guess(mixed_list,guess)
