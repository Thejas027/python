from IPython.display import clear_output
import random

def display_board(board):
      clear_output(wait=True)
      # print('  |  |')
      print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
      # print('  |  |')
      print('---------')
      print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
      # print('  |  |')
      print('---------')
      print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
      # print('  |  |')

def player_input():
      # Function to take the player's marker input
      marker = ''
      while not (marker == 'X' or marker == 'O'):
            marker = input("Player 1: Choose X or O: ").upper()
            if marker == 'X':
                  return ('X', 'O')
            else:
                  return ('O', 'X')

def place_marker(board, marker, position):
      # Place the player's marker on the board at the chosen position
      board[position] = marker

def win_check(board, mark):
      # WIN TIC TAC TOE?
      # Check all rows, columns, and diagonals to see if they share the same marker
      return (
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)
      )

def choose_first():
      # Randomly choose which player goes first
      return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'

def space_check(board, position):
      # Check if the chosen position is available on the board
      return board[position] == ' '

def full_board_check(board):
      # Check if the board is full by verifying if all positions are occupied
      for i in range(1, 10):
            if space_check(board, i):
                  return False
      return True

def player_choice(board):
      # Get the player's next position choice
      position = 0
      while position not in range(1, 10) or not space_check(board, position):
            try:
                  position = int(input("Choose a position (1-9): "))
            except ValueError:
                  print("Please enter a valid number between 1 and 9.")
      return position

def replay():
      # Ask if the players want to play again
      choice = input("Play again? Enter Yes or No: ").strip().lower()
      return choice == 'yes'

# WHILE LOOP TO KEEP RUNNING THE GAME 
print("--------welcome to TIC TAC TOE game-----------")
while True:
      
      # PLAY GAME 
      
      ## SET EVERYTHING UP (BOARD,WHO'S FIRST,CHOOSE MARKER 'X','O')
      the_board = [' '] * 10
      
      player1_marker , player2_marker = player_input()
      
      turn = choose_first()
      
      print(turn + "will go first")
      
      
      play_game = input('Ready to play game ? Y or N ?')
      
      if play_game == 'Y':
            game_on = True
      else: 
            game_on = False
      
      
### PLAYER ONE TURN 
      while game_on:
            if turn == 'Player 1':
                  
                  ## show  the board 
                  display_board(the_board)
                  
                  ## choose a position 
                  position = player_choice(the_board)
                  
                  ## place a marker in a position 
                  place_marker(the_board,player1_marker,position)
                  
                  ## check if they won 
                  if win_check(the_board,player1_marker):
                        display_board(the_board)
                        print('PLAYER1 HAS WON!!')
                        game_on = False
                  else:
                  ## or check it for tie
                        if full_board_check(the_board):
                              display_board(the_board)
                              print('TIE GAME!')
                              game_on = False
                        else:
                              turn = 'Player 2'
                              
            ###PLAYER TWO TURN 
            else:
                  #display the marker 
                  display_board(the_board)
                  
                  # position 
                  position = player_choice(the_board)
                  
                  # place the marker on the position
                  place_marker(the_board,player2_marker,position)
                  
                  # check for who won 
                  if win_check(the_board,player2_marker):
                        display_board(the_board)
                        print("PLAYER2 HAS WON!!")
                        game_on = False
                  else:
                        ##check for tie
                        if full_board_check(the_board):
                              display_board(the_board)
                              print("GAME TIE!")
                              game_on = False
                        else:
                              turn = 'Player 1'

# IF NOT REPLAY THEN BREAK 
      if not replay():
            break;