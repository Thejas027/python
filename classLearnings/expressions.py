# #   LAMBDA EXPRESSIONS , MAPS AND FILTERS

# # the below code is used to obtain the square of number and map function is used 
# def square(nums):
#       return nums ** 2

# nums = [1,2,3,4]

# squared_num = map(square,nums)
# square_list = list(map(square,nums))

# print(square_list)

# for item in squared_num:
#       print(item)


# #############

# #the below code is used to check weather the giving string has a even number or not and map function is used 
# def splicer(names):
#       if len(names) % 2 == 0:
#             return 'EVEN'
#       else:
#             return names[0]
      
# names = ['Andy','eve']
# splicers = list(map(splicer,names))
# print(splicers)

# ######

# # FILTER METHOD

# def check_even(num):
#       return num % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,10]

# # it has been transformed to list 
# filter_list = list(filter(check_even,nums))
# # print(filter_list)

# # filter can be even iterated 
# for item in filter_list:
#       print(item)
      
# #############
# # Lambda expressions 
# # the above square method is written in lambda function 

# # square = lambda num : num **2 
# # result = square(8)
# # print(f"The square of given number is : {result}")


# square = list(map(lambda num : num **2 ,nums))
# print(square)

#above check even number function to lambda function

# even_number = lambda num : num %2 ==0
# res = even_number(2)
# print(res)

# even_num = list(filter(lambda num : num % 2 ==0 ,nums))
# print(even_num)


########
# code to take a first element from a list of string 

# names = ['Andy','Bob','Champ']
# res = list(map(lambda name : name[0],names))
# print(res)

##### 
# to reverse a names list name 

names = ['Andy','Bob','Champ']
res = list(map(lambda name : name[::-1],names))
print(res)