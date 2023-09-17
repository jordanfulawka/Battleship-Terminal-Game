class Board:
  board = [[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',]]
  occupied = []

  square_mapping = {'A':0,'B':1,'C':2,'D':3,'E':4,'1':0,'2':1,'3':2,'4':3,'5':4}

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
    
  def validate_input(self, positions, user_input):
    if user_input == 'W':
      for position in positions:
        if position[0] == 0:
          return False
    elif user_input == 'S':
      for position in positions:
        if position[0] == 4:
          return False
    elif user_input == 'A':
      for position in positions:
        if position[1] == 0:
          return False
    elif user_input == 'D':
      for position in positions:
        if position[1] == 4:
          return False
    elif user_input == 'R':
      for position in positions:
        if [position[1], position[0]] in self.occupied:
          return False
    return True


  def place_ships(self, squares):
    positions = squares
    confirmed = 0
    while (confirmed != 1):
      try:
        self.preview_board(positions)
      except IndexError:
        print("Invalid")
      print("R: Rotate", "W: Up", "S: Down", "A: Left", "D: Right", "Space: Place")
      user_input = input()
      user_input = user_input.upper()
      if(self.validate_input(positions,user_input)):
        if user_input == "D":
          for position in positions:
            position[1] += 1
        elif user_input == 'A':
          for position in positions:
            position[1] -= 1
        elif user_input == 'W':
          for position in positions:
            position[0] -= 1
        elif user_input == 'S':
          for position in positions:
            position[0] += 1
        elif user_input == 'R':
          for position in positions:
            temp = position[0]
            position[0] = position[1]
            position[1] = temp
        elif user_input == 'P':
          for position in positions:
            self.board[position[0]][position[1]] = '■'
            confirmed = 1
            self.occupied.append([position[0], position[1]])
    self.print_board() 


class Player():
  def __init__(self):
    self.playerboard = Board()
  def place_ships(self):
    self.playerboard.place_ships([[0,0],[1,0],[2,0],[3,0]])
    self.playerboard.place_ships([[0,0],[1,0],[2,0]])
    
player1 = Player()
player1.place_ships()

