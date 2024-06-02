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

def old_macdonald(name):
      first_letter = name[0]
      in_between = name[1:3]
      fourth_letter = name[3]
      rest = name[4:]
      
      return first_letter.upper() + in_between + fourth_letter.upper() + rest

# res = old_macdonald('macdonalds')
# res = old_macdonald('thejas')
# print(res)


# ----another method

def old_macdonald2(name):
      first_half = name[:3]
      second_half = name[3:]
      
      return first_half.capitalize() + second_half.capitalize()


# res = old_macdonald('macdonalds')
# print(res)


#### MASTER YODA: Given a sentence, return a sentence with the words reversed

#     master_yoda('I am home') --> 'home am I'
#     master_yoda('We are ready') --> 'ready are We'

def reverse_string(text):
      word_list = text.split()
      reversed_text_list = word_list[::-1]
      
      return ' '.join(reversed_text_list)
output = reverse_string('i am home')
print(output)


#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True

def almost_there(num):
      return (abs(100-num) <= 10 ) or (abs(200-num) <= 10)

number = int(input("enter the number to check the range : "))

op = almost_there(number)
print(op)