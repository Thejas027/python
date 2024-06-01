#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd

def number(num1,num2):
      if num1 % 2 == 0 and num2 % 2 == 0 :
            return min(num1,num2)
      else:
            return max(num1,num2)
      
# num1 = int(input("enter the num1 value to check : "))
# num2 = int(input("enter the num2 value to check : "))
# result = number(num1,num2)
# print(result)



#####################

#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False

def animal_checker(str):
      word = str.split()
      
      if len(word) == 2 and word[0][0].lower() == word[1][0].lower():
            return True
      else:
            return False

result1 = animal_checker('lio lion')
# print(result1)
      


#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False

#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

def makes_twenty(a,b):
      if a == 20 or b == 20 or (a+b) == 20 :
            return True
      else:
            return False
      
result2 = makes_twenty(2,8)
# print(result2)


###################

#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

#     old_macdonald('macdonald') --> MacDonald
# Note: `'macdonald'.capitalize()` returns `'Macdonald'`

def old_mac(name):
      for i in name:
            if(i == 0 and i == 4):
                  i.upper()
                  pass
      return name
            
result3 = old_mac('macdonalds')
print(result3)