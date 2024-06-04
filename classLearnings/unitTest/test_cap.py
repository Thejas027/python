import unittest   # inbuilt library which is begin imported 
import cap

'''
unit testing can be done in 2 ways 
      1) pylint :-
                  install a package of pylint set in to environment variables then in terminal use 
                        ---> pylint filename.py  , execute it it gives errors and all other details 
      2) Unittest method as show below
'''

class TestCap(unittest.TestCase):
      
      def one_word_cap(self):
            text = 'python'
            result = cap.cap_text(text)
            
            self.assertEqual(result,'Python')  # self.assertEqual() --> the result can be expected like this 
            
      def test_multiple_word(self):
            text = 'monty python'
            result = cap.cap_text(text)
            
            self.assertEqual(result,'Monty Python')


if __name__ == '__main__':
      unittest.main()
