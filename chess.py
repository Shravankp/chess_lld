from enum import Enum
from pieces import *

class Colour(Enum):
    BLACK = 1
    WHITE = 2

class Player:
    def __init__(self, name: str, piece_colour: Colour) -> None:
        self.name = name
        self.piece_colour = piece_colour

    def move(self, source, destination, board) -> None:
        source_x, source_y = source
        dest_x, dest_y = destination

        piece: Pieces = board[source_x][source_y]

        if not piece or self.piece_colour != piece.colour:
            return False

        if not piece.isValidMove(dest_x, dest_y):
            return False
        
        piece.makeMove(dest_x, dest_y)
        board[source_x][source_y] = None
        board[dest_x][dest_y] = piece
        
        return True
        

class Board:
    def __init__(self) -> None:
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.board[0: 1] = Board.createPieces(Colour.BLACK)
        self.board[-1], self.board[-2] = Board.createPieces(Colour.WHITE)

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        newboard = ['----------------- Board -----------------']
        for row in self.board:
            curRow = []
            for col in row:
                curRow.append(f'{col}')
            rowStr = '\t'.join(curRow)
            newboard.append(rowStr)
        newboard.append('\n\n')
        return '\n'.join(newboard)

    @staticmethod
    def createPieces(colour: Colour) -> list:
        bottomRow = 0 if colour == Colour.WHITE else 7
        frontRow = 1 if colour == Colour.WHITE else 6

        bottom = [Rook(colour, (bottomRow, 0)), Knight(colour, (bottomRow, 1)), Bishop(colour, (bottomRow, 2)),
                    Queen(colour, (bottomRow, 3)), King(colour, (bottomRow, 4)), Bishop(colour, (bottomRow, 5)),
                    Knight(colour, (bottomRow, 6)), Rook(colour, (bottomRow, 7))]

        front = [Pawn(colour, (frontRow, col)) for col in range(8)]
        
        return [bottom, front]
    
    def getBoard(self) -> list:
        return self.board


class Chess:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.board = Board()
        self.player1 = player1
        self.player2 = player2


if __name__ == '__main__':
    player1 = Player('kp14', Colour.BLACK)
    player2 = Player('vr46', Colour.WHITE)
    
    chess = Chess(player1, player2)
    board = chess.board
    print(board)

    ##################### take player1 and player2 moves as inputs #############################
    player1.move((0, 0), (3, 3), board.getBoard())
    print(board)


    

















    
        