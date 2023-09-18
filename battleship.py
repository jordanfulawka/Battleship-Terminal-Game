import random
import time

class Board:
  square_mapping = {'A':0,'B':1,'C':2,'D':3,'E':4,'1':0,'2':1,'3':2,'4':3,'5':4}
  def __init__(self):
    self.board = [[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',]]
    self.guessing_board = [[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',]]
    self.occupied = []

  def print_board(self):
    print("   1  2  3  4  5 ")
    rows = ['A','B','C','D','E']
    row_num = 0
    for row in self.board:
      print("{} ".format(rows[row_num]), end='')
      row_num += 1
      for square in row:
        print("[{}]".format(square), end='')
      print("")

  def print_guessing_board(self):
    print("   1  2  3  4  5 ")
    rows = ['A','B','C','D','E']
    row_num = 0
    for row in self.guessing_board:
      print("{} ".format(rows[row_num]), end='')
      row_num += 1
      for square in row:
        print("[{}]".format(square), end='')
      print("")
    
  def preview_board(self, squares):
    temp_board = [[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',]]
    for square in self.occupied:
      temp_board[square[0]][square[1]] = '■'
    for square in squares:
      temp_board[square[0]][square[1]] = 'X'
    print("   1  2  3  4  5 ")
    rows = ['A','B','C','D','E']
    row_num = 0
    for row in temp_board:
      print("{} ".format(rows[row_num]), end='')
      row_num += 1
      for square in row:
        print("[{}]".format(square), end='')
      print("")
    
  def validate_input(self, target, player):
    if target[0].upper() not in ['A','B','C','D','E']: return False
    if target[1] not in ['1','2','3','4','5']: return False
    if self.guessing_board[self.square_mapping[target[0].upper()]][self.square_mapping[target[1]]] != ' ': return False

    if player.playerboard.board[self.square_mapping[target[0].upper()]][self.square_mapping[target[1]]] == '■':
      self.guessing_board[self.square_mapping[target[0].upper()]][self.square_mapping[target[1]]] = 'X'
      self.print_guessing_board()
      print("You hit a ship!")
      player.ships_left -= 1
    else:
      self.guessing_board[self.square_mapping[target[0].upper()]][self.square_mapping[target[1]]] = '0'
      self.print_guessing_board()
      print("You missed!")
    print("-----------------------------")
    return True

    
  def validate_position(self, positions, user_input):
    if user_input == 'W':
      for position in positions:
        if position[0] == 0:
          return 0
        elif [position[0]-1, position[1]] in self.occupied:
          if [position[0]-2, position[1]] in self.occupied:
            return 0
          return 2
    elif user_input == 'S':
      for position in positions:
        if position[0] == 4:
          return 0
        elif [position[0]+1,position[1]] in self.occupied:
          if [position[0]+2,position[1]] in self.occupied:
            return 0
          return 2
    elif user_input == 'A':
      for position in positions:
        if position[1] == 0:
          return 0
        elif [position[0],position[1]-1] in self.occupied:
          if [position[0],position[1]-2] in self.occupied:
            return 0
          return 2
    elif user_input == 'D':
      for position in positions:
        if position[1] == 4:
          return False
        elif [position[0],position[1]+1] in self.occupied:
          if [position[0], position[1]+2] in self.occupied:
            return 0
          return 2
    elif user_input == 'R':
      counter = 0
      if positions[1][0] == positions[0][0] + 1:
        for position in positions:
          if [positions[0][0],position[1]+counter] in self.occupied or position[1]+counter>4:
            return 0
          counter += 1
      else:
        for position in positions:
          if [position[0]+counter,positions[0][1]] in self.occupied or position[0]+counter>4:
            return 0
          counter += 1
    return 1
  
  def place_ships(self, squares, is_computer = 0):
    positions = squares
    if is_computer == 0:
      confirmed = 0
      while (confirmed != 1):
        try:
          self.preview_board(positions)
        except IndexError:
          print("Invalid")
        print("R: Rotate", "W: Up", "S: Down", "A: Left", "D: Right", "Space: Place")
        user_input = input()
        user_input = user_input.upper()
        num = self.validate_position(positions,user_input)
        if(num):
          if user_input == "D":
            for position in positions:
              position[1] += num
          elif user_input == 'A':
            for position in positions:
              position[1] -= num
          elif user_input == 'W':
            for position in positions:
              position[0] -= num
          elif user_input == 'S':
            for position in positions:
              position[0] += num
          elif user_input == 'R':
            self.counter = 0
            if positions[1][0] == positions[0][0] + 1:
              for position in positions:
                position[0] = positions[0][0]
                position[1] += self.counter
                self.counter += 1
            else:
              for position in positions:
                position[1] = positions[0][1]
                position[0] += self.counter
                self.counter += 1
          elif user_input == 'P':
            for position in positions:
              self.board[position[0]][position[1]] = '■'
              confirmed = 1
              self.occupied.append([position[0], position[1]])
    else:
      for position in positions:
        self.board[position[0]][position[1]] = '■' 

class Player:
  def __init__(self, is_computer = 0):
    self.playerboard = Board()
    self.is_computer = is_computer
    self.ships_left = 9
    self.already_guessed = []
  def place_ships(self):
    if self.is_computer == 0:
      self.playerboard.place_ships([[0,0],[1,0],[2,0],[3,0]])
      self.playerboard.place_ships([[0,0],[1,0],[2,0]])
      self.playerboard.place_ships([[0,0],[1,0]])
    else:
      current_ships = []
      valid = 0
      # first ship, length 4
      rotation = random.choice([0,1])
      # 0 means ship is vertical
      if rotation == 0:
        first_square_row = random.choice([0,1])
        first_square_column = random.choice([0,1,2,3,4])
        current_ships.append([[first_square_row,first_square_column],
                              [first_square_row+1,first_square_column],
                              [first_square_row+2,first_square_column],
                              [first_square_row+3,first_square_column]])
      else:
        first_square_row = random.choice([0,1,2,3,4])
        first_square_column = random.choice([0,1])
        current_ships.append([[first_square_row,first_square_column],
                              [first_square_row,first_square_column+1],
                              [first_square_row,first_square_column+2],
                              [first_square_row,first_square_column+3]])
      #second ship length 3
      while(valid == 0):
        valid = 1
        rotation = random.choice([0,1])
        if rotation == 0:
          first_square_row = random.choice([0,1,2])
          first_square_column = random.choice([0,1,2,3,4])
          temp_ship = [[first_square_row,first_square_column],
                      [first_square_row+1,first_square_column],
                      [first_square_row+2,first_square_column]]
        else:
          first_square_row = random.choice([0,1,2,3,4])
          first_square_column = random.choice([0,1,2])
          temp_ship = [[first_square_row,first_square_column],
                      [first_square_row,first_square_column+1],
                      [first_square_row,first_square_column+2]]
        for ship in current_ships:
          for square in temp_ship:
            if square in ship:
              valid = 0
        if valid == 1:
          current_ships.append(temp_ship)
        else:
          valid = 0
      valid = 0
      while (valid == 0):
        valid = 1
        rotation = random.choice([0,1])
        if rotation == 0:
          first_square_row = random.choice([0,1,2,3])
          first_square_column = random.choice([0,1,2,3,4])
          temp_ship = [[first_square_row,first_square_column],
                      [first_square_row+1,first_square_column]]
        else:
          first_square_row = random.choice([0,1,2,3,4])
          first_square_column = random.choice([0,1,2,3])
          temp_ship = [[first_square_row,first_square_column],
                      [first_square_row,first_square_column+1]]
        for ship in current_ships:
          for square in temp_ship:
            if square in ship:
              valid = 0
        if valid == 1:
          current_ships.append(temp_ship)
        else:
          valid = 0
      self.playerboard.place_ships(current_ships[0],1)
      self.playerboard.place_ships(current_ships[1],1)
      self.playerboard.place_ships(current_ships[2],1)
  
  def take_turn(self, player1, player2):
    if self.is_computer == 0:
      while(True): 
        self.playerboard.print_guessing_board()
        print("Player 1: Please guess a square")
        target = input()
        if(not self.playerboard.validate_input(target, player2)):
          print("Invalid input! Please try again")
        else: break
    else:
      valid = 0
      while(not valid):
        row = random.choice([0,1,2,3,4])
        column = random.choice([0,1,2,3,4])
        if [row, column] in self.already_guessed: continue
        else: self.already_guessed.append([row,column])
        valid = 1
        if player1.playerboard.board[row][column] == '■':
          player1.playerboard.board[row][column] = 'X'
          player1.ships_left -= 1
          player1.playerboard.print_board()
          print("Player 2 hits a ship!")
        else:
          player1.playerboard.board[row][column] = '0'
          player1.playerboard.print_board()
          print("Player 2 missed!")
        
      print("-----------------------------")
      


class Game:
  def __init__(self):
    self.player1 = Player()
    self.player2 = Player(1)
    self.player1.place_ships()
    self.player2.place_ships()
    print("Here is your board: ")
    self.player1.playerboard.print_board()
  
  def start_game(self):
    game_over = 0
    while(not game_over):
      self.player1.take_turn(self.player1, self.player2)
      if self.player2.ships_left == 0:
        print("Player 1 wins!")
        break
      time.sleep(1)
      self.player2.take_turn(self.player1, self.player2)
      if self.player1.ships_left == 0:
        print("Player 2 wins!")
        break
      time.sleep(1)


game1 = Game()
game1.start_game()