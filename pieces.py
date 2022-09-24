from abc import ABCMeta, abstractmethod

class Pieces(metaclass = ABCMeta):
    @property
    @abstractmethod
    def colour(self):
        pass
    
    @abstractmethod
    def validMoves(self):
        pass

    @abstractmethod
    def isValidMove(self, x, y):
        pass

    @abstractmethod
    def makeMove(self):
        pass

class Rook(Pieces):

    def __init__(self, colour, location) -> None:
        self.location = location
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    def validMoves(self):
        # first check if moving current piece causes a check
        return [(3,3), (4,4)]
    
    def isValidMove(self, x, y):
        return (x, y) in self.validMoves()
    
    def makeMove(self, x, y):
        self.location = (x, y)
    
    def __repr__(self):
        return 'Rk'

class Knight(Pieces):

    def __init__(self, colour, location) -> None:
        self.location = location
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    def validMoves(self):
        # first check if moving current piece causes a check
        pass

    def isValidMove(self, x, y):
        pass

    def makeMove(self, x, y):
        pass
    
    def __repr__(self):
        return 'Kn'


class Bishop(Pieces):

    def __init__(self, colour, location) -> None:
        self.location = location
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    def validMoves(self):
        # first check if moving current piece causes a check
        pass

    def isValidMove(self, x, y):
        pass

    def makeMove(self, x, y):
        pass

    def __repr__(self):
        return 'Bi'


class King(Pieces):

    def __init__(self, colour, location) -> None:
        self.location = location
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    def validMoves(self):
        # first check if moving current piece causes a check
        pass

    def isValidMove(self, x, y):
        pass

    def makeMove(self, x, y):
        pass

    def __repr__(self):
        return 'K'


class Queen(Pieces):

    def __init__(self, colour, location) -> None:
        self.location = location
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    def validMoves(self):
        # first check if moving current piece causes a check
        pass

    def isValidMove(self, x, y):
        pass

    def makeMove(self, x, y):
        pass

    def __repr__(self):
        return 'Q'


class Pawn(Pieces):

    def __init__(self, colour, location) -> None:
        self.location = location
        self._colour = colour

    @property
    def colour(self):
        return self._colour

    def validMoves(self):
        # first check if moving current piece causes a check
        pass

    def isValidMove(self, x, y):
        pass
    
    def makeMove(self, x, y):
        pass

    def __repr__(self):
        return 'Pa'














