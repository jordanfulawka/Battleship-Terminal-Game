class Board:
  board = [[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',],[' ',' ',' ',' ',' ',]]

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
    for square in squares:
      print(square)
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

  def place_ships(self):
    positions = [[0,0],[1,0],[2,0],[3,0]]
    confirmed = 0
    while (confirmed != 1):
      try:
        self.preview_board(positions)
      except IndexError:
        print("Invalid")
      print("R: Rotate", "W: Up", "S: Down", "A: Left", "D: Right", "Space: Place")
      user_input = input()
      user_input = user_input.upper()
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


class Player():
  def __init__(self):
    self.playerboard = Board()
  def place_ships(self):
    self.playerboard.place_ships()
    
player1 = Player()
player1.place_ships()

