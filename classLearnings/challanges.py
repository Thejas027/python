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


###################   LEVEL - ONE problems 

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
# output = reverse_string('i am home')
# print(output)


#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True

# def almost_there(num):
      # return (abs(100-num) <= 10 ) or (abs(200-num) <= 10)

# number = int(input("enter the number to check the range : "))

# op = almost_there(number)
# print(op)

############# LEVEL-2 

##### 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

def has_three(my_list):
      # Iterate through the list up to the third-to-last element
      for i in range(len(my_list) - 2):
      # Check if current element and the next two elements are all 3
            if my_list[i] == 3 and my_list[i + 1] == 3:
                  return True
      return False

# Example usage
my_list = [1, 1, 3]
op = has_three(my_list)
# print(op)  


#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#     paper_doll('Hello') --> 'HHHeeellllllooo'
#     paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
      repeated_text = ''
      for char in text:
            repeated_text  += char * 3
      return repeated_text      

# text_op = paper_doll('Thejas')
# print(text_op)



#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

def blackjack(my_list):
      for i in my_list:
            
            if(sum(my_list) <= 21):
                  return sum(my_list)                  
                        
            elif 11 in my_list and sum(my_list) <= 31:
                  value = sum(my_list) - 10
                  return value
      return 'BUST'

my_list = [5,6,7]
blackjack_result = blackjack(my_list)
print(blackjack_result)