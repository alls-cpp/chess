from piece import Pawn
from piece import Rook
from piece import Knight
from piece import Bishop
from piece import Queen
from piece import King

class Board:
    def __init__(self):
        self.rows = 8
        self.columns = 8

        self.board = [[0 for _ in range(8)] for _ in range(self.rows)]
        
        # for i in range(8):
            # self.board[1][i] = Pawn(1, i, "w")
            # self.board[6][i] = Pawn(6, i, "w")

        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][3] = Queen(0, 3, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")

        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[4][4] = Queen(4, 4, "w")
        self.board[7][4] = King(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")
    
    def draw(self, win, board):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win, board)
    
    def select(self, x, y):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

        if self.board[y][x] != 0:
            self.board[y][x].selected = True
    
    def move(self, start, end):
        removed = self.board[end[1]][end[0]]
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]]
        self.board[start[1]][start[0]] = 0

        return removed