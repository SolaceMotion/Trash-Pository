import random

# Create a list that can hold 9 items and fill them with 0
board = [0] * 9

def renderBoard():
  # Print X or O for each square
  # 0 means unoccupied. 1 means player 1 (X) 2 means the computer (O)
  for i in range(0,9):
    if board[i] == 0:
      print(".", end=' ')
      # If any of the board values contain 0 then print .
    if board[i] == 1:
      print("X", end=' ')
    
    if board[i] == 2:
      print("O", end=' ')

    # Make board look like a tic-tac-toe-board
    if i == 2 or i == 5 or i == 8: print("")

# Initial values used in while loop
userTurn = -1
computerTurn = -1

def winLogic():
  # If you get three in a row you win
  if board[0] == board[1] and board[1] == board[2]: return board[0]
  if board[3] == board[4] and board[4] == board[5]: return board[3]
  if board[6] == board[7] and board[7] == board[8]: return board[6]
  if board[0] == board[3] and board[3] == board[6]: return board[0]
  if board[1] == board[4] and board[4] == board[7]: return board[1]
  if board[2] == board[5] and board[5] == board[8]: return board[2]
  if board[0] == board[4] and board[4] == board[8]: return board[0]
  if board[2] == board[4] and board[4] == board[6]: return board[2]

  return False

# While the return value is false
while (winLogic() == False):
  
  # If a place is occupied by the player or computer, don't run. If user input index is not 0 meaning it's empty, carry on
  while userTurn == -1 or board[userTurn] != 0:
    print("Enter number from 0 through 8")
    userTurn = int(input())
  
  board[userTurn] =1

  while computerTurn == -1 or board[computerTurn] != 0:
    # Pick a random number within range of the list
    computerTurn = random.randint(0, 8)

    # Always occupy the middle column and the middle row if it isn't already occupied
    if board[4] == 0: computerTurn = 4

    # print(computerTurn)

  board[computerTurn] = 2

  # Re-render board on every iteration
  renderBoard()
  print("")

if winLogic() == 1:
  print("The player won the game")
else:
  print("The computer won the game")