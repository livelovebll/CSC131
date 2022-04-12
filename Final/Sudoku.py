import argparse

from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

BOARDS = ['DeBuG', 'sIMplE', 'meDiUm', 'HarD']
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class Error(Exception):

  '''
  Specific Error
  '''
  pass

def parse_argument():
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument("--board", help="Desired board", type=str, choices=BOARDS,required=True)

  args = vars(arg_parser.parse_args())
  return args['board']



class Board(object):
  def __init__(self, board_fl):
    self.board = self.__create_board(board_fl)

  def __create_board(self,board_fl):
    board = []

    for line in board_fl:
      line = line.strip()
      if len(line) != 9:
        board = []
        raise Error(
          "Each line in the puzzle must have 9 numbers."
        )

      board.append([])
      

      for c in line:
        if not c.isdigit():
          raise Error(
            "Numbers must be 0-9"
          )
        board[-1].append(int(c))

    if len(board) != 9:
      raise Error("Each puzzle must be 9 lines long")
    return board


class Game(object):
  
  #responsible for keeping the state of the board and checking whether the puzzle is complete

  def __init__(self, board_fl):
    self.board_fl = board_fl
    self.start_puzzle = Board(board_fl).board

  def start(self):
    self.end_game = False
    self.puzzle = []
    for i in xrange(9):
      for j in xrange(9):
        self.puzzle[i].append(self.start_puzzle[i][j])

  def check_win(self):
    for row in xrange(9):
      if not self.__check_row(row):
        return False

    for column in xrange(9):
      if not self.__check_column(column):
        return False

    for row in xrange(3):
      for column in xrange(3):
        if not self.__check_square(row,column):
          return False
    self.end_game = True
    return True

  def __check_block(self, block):
    return set(block) == set(range(1, 10))

  def __check_row(self, row):
    return self.__check_block(self.puzzle[row])

  def __check_column(self,column):
    return self.__check_block([self.puzzle[row][column] for row in xrange(9)])

  def __check_square(self, row, column):
    return self.__check_block([self.puzzle[r][c] for r in xrange(row * 3, (row + 1) * 3) for c in xrange(column * 3, (column + 1) * 3)])


class UI(Frame):

  def __init__(self, parent, game):
    self.game = game
    self.parent = parent
    Frame.__init__(self, parent)

    self.row, self.col = -1, -1

    self.UI()

  def UI(self):
    self.parent.title("Sudoku")
    self.pack(fill = BOTH, expand=1)
    self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
    self.canvas.pack(fill=BOTH, side=TOP)
    clear_button = Button(self, text="Clear Answers", command=self.__clear_answers)
    clear_button.pack(fill=BOTH, side=BOTTOM)

    self.__draw_grid()
    self.__draw_puzzle()

    self.canvas.bind("<Button-1>", self.__cell_clicked)
    self.canvas.bind("<Key>", self.__key_pressed)

  def __draw_grid(self):
    for i in xrange(10):
      color = "blue" if i % 3 == 0 else "gray"

      x0 = MARGIN + i * SIDE
      y0 = MARGIN
      x1 = MARGIN + i * SIDE
      y1 = HEIGHT - MARGIN
      self.canvas.create_line(x0, y0,x1, y1, fill=color)

  def __draw_puzzle(self):
    self.canvas.delete("numbers")
    for i in xrange(9):
      for j in xrange(9):
        answer = self.game.puzzle[i][j]
        if answer != 0:
          x = MARGIN + j * SIDE + SIDE / 2
          y = MARGIN + i * SIDE + SIDE / 2
          original = self.game.start_puzzle[i][j]
          color = "black" if answer == original else "sea grean"
          self.canvas.create_text(
            x, y, text=answer, tags="numbers", fill=color
          )

  def __clear_answers(self):
    self.game.start()
    self.canvas.delete("victory")
    self.__draw_puzzle()

  def __cell_clicked(self, event):
    if self.game.game_over:
      return

    x, y = event.x, event.y
    if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
      self.canvas.focus_set()

      row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

      if (row, col) == (self.row, self.col):
        self.row, self.col = -1, -1
      elif self.game.puzzlw[row][col] == 0:
        self.row, self.col = row, col
        
    self.__draw_cursor()

  def __draw_cursor(self):
    self.canvas.delete("cursor")
    if self.row >= 0 and self.col >= 0:
      x0 = MARGIN + self.col * SIDE + 1
      y0 = MARGIN + self.row * SIDE + 1
      x1 = MARGIN + (self.col + 1) * SIDE - 1
      y1 = MARGIN + (self.row + 1) * SIDE - 1
      self.canvas.create_rectangle(
        x0, y0, x1, y1,
        outline="red", tags="cursor"
      )

  def __key_pressed(self, event):
    if self.game.game_over:
      return
    if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
      self.game.puzzle[self.row][self.col] = int(event.char)
      self.col, self.row = -1, -1
      self.__draw_puzzle()
      self.__draw_cursor()
      if self.game.check_win():
        self.__draw_victory()

  def __draw_victory(self):
    x0 = y0 = MARGIN + SIDE * 2 
    x1 = y1 = MARGIN + SIDE * 7
    self.canvas.create_circle(
      x0, y0, x1, y1,
      tags="victory", fil="dark orange", outline="orange"
    )

    x = y = MARGIN + 4 * SIDE + SIDE / 2
    self.canvas.creste_text(
      x,y,
      text="YOU WIN!", tags="WINNER",
      fill="white", font=("Arial", 32)
    )


if __name__ == '__main__':
  board_name = parse_argument()

  with open('%s.sudoku' % board_name, 'r') as boards_file:
    game = SudokuGame(boards_file)
    game.start()

    root = Tk()
    UI(root, game)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()