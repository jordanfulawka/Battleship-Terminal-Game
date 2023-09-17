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
    temp_board = self.board.copy()
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

  def validate_input(self, square):
    if len(square) != 2: 
      print("Length incorrect")
      return False
    if square[0] not in self.square_mapping: 
      print("First letter wrong")
      return False
    if square[1] not in self.square_mapping: 
      print("Second number wrong")
      return False
    if self.board[self.square_mapping[square[0]]][self.square_mapping[square[1]]] != ' ': 
      print("Spot is taken")
      return False
    return True

  def place_ships(self):
    # self.print_board()
    positions = [[0,0],[1,0],[2,0],[3,0]]
    confirmed = 0
    while (confirmed == 0):
      self.preview_board(positions)
      print("R: Rotate", "U: Up", "D: Down", "L: Left", "R: Right", "P: Place")
      user_input = input()
      user_input = user_input.upper()
      if user_input == "R":
        for position in positions:
          position[1] += 1



class Player():
  def __init__(self):
    self.playerboard = Board()
    # self.board.print_board()
  
  def place_ships(self):
    self.playerboard.place_ships()
    
player1 = Player()
player1.place_ships()

