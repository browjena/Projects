#
#
#
class QuoridorGame:
    """class QuoridorGame will interact with class player and class Cell
    it initializes two of its data members to player objects and initializes its gameBoard data member with 9x9 list of cells
    contains getter and setter methods for its private data members as well as methods to check for available fence moves
    check available player moves, move pawn, place fence, and check if a player has won the game
    """
    def __init__(self):
        """initializes the gameboard with cells, initializes playerOne and playerTwo with their proper starting positions/isTurn status
        initializes gameOver to False and sets the cell's has_pawn status in gameboard positions [4][0] and [4][8] to True
         """
        self._gameBoard = [[Cell(True,False,True,False),Cell(False,False,True,False),Cell(False,False,True,False),Cell(False,False,True,False),
                           Cell(False, False, True, False),Cell(False,False,True,False),Cell(False,False,True,False),Cell(False,False,True,False),
                           Cell(False,True,True,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False, False, False, False),Cell(False,False,False,False),Cell(False,False,False,False),
                           Cell(False,False,False,False),Cell(False,True,False,False)],[Cell(True,False,False,True),Cell(False,False,False,True),Cell(False,False,False,True),
                           Cell(False,False,False,True),Cell(False, False, False, True),Cell(False,False,False,True),Cell(False,False,False,True),
                           Cell(False,False,False,True),Cell(False,True,False,True)]]
        self._playerOne = Player(4,0,True,1)
        self._playerTwo = Player(4,8,False,-1)
        self._gameOver = False
        self._gameBoard[4][8].set_hasPawn(True)
        self._gameBoard[4][0].set_hasPawn(True)

    def checkLeft(self, current_player_coll, current_player_row):
        """takes as a parameter the desired players collumn/row returns True
        if the player is not blocked by a fence to the left (toward collumn 0) and
        no other player is in the spot to the left"""
        if not self._gameBoard[current_player_coll][current_player_row].get_left():
            if not self._gameBoard[current_player_coll-1][current_player_row].get_hasPawn():
                return True

    def checkRight(self,current_player_coll,current_player_row):
        """takes as parameters the desired players collum and row
        returns true if the player is not blocked by a fence to the right(toward collumn 8)
        and no other player is in the spot the right
        """
        if not self._gameBoard[current_player_coll][current_player_row].get_right():
            if not self._gameBoard[current_player_coll + 1][current_player_row].get_hasPawn():
                    return True
    def check_valid_moves(self,current_player,other_player):
        """check valid moves takes as parameters the current_player(player who wishes to move)and the otherplayer
         it returns availableMoves: a list of tuples of all possible available moves for the given player
         """
        availableMoves = []
        other_player_coll = other_player.get_currentPos()[0]
        other_player_row = other_player.get_currentPos()[1]
        current_player_coll = current_player.get_currentPos()[0]
        current_player_row = current_player.get_currentPos()[1]
        if self.checkLeft(current_player_coll,current_player_row):
            availableMoves.append((current_player_coll - 1, current_player_row))
        if self.checkRight(current_player_coll,current_player_row):
                availableMoves.append((current_player_coll + 1, current_player_row))
        if current_player.get_forwardDirec() == 1:
            if not self._gameBoard[current_player_coll][current_player_row].get_behind():
                if not self._gameBoard[current_player_coll][current_player_row - 1].get_hasPawn():
                    availableMoves.append((current_player_coll, current_player_row -1))
            if not self._gameBoard[current_player_coll][current_player_row].get_forward():
                if self._gameBoard[current_player_coll][current_player_row+1].get_hasPawn():
                    if not self._gameBoard[other_player_coll][other_player_row].get_forward():
                        availableMoves.append((other_player_coll,other_player_row+1))
                    else:
                        if self.checkRight(other_player_coll,other_player_row):
                            availableMoves.append((other_player_coll+1,other_player_row))
                        if self.checkLeft(other_player_coll,other_player_row):
                            availableMoves.append((other_player_coll-1,other_player_row))
                else:
                    availableMoves.append((current_player_coll,current_player_row + 1))
        else:
            if not self._gameBoard[current_player_coll][current_player_row].get_forward():
                if not self._gameBoard[current_player_coll][current_player_row + 1].get_hasPawn():
                    availableMoves.append((current_player_coll, current_player_row + 1))
            if not self._gameBoard[current_player_coll][current_player_row].get_behind():
                if self._gameBoard[current_player_coll][current_player_row-1].get_hasPawn():
                    if not self._gameBoard[other_player_coll][other_player_row].get_behind():
                        availableMoves.append((other_player_coll,other_player_row-1))
                    else:
                        if self.checkRight(other_player_coll,other_player_row):
                            availableMoves.append((other_player_coll+1,other_player_row))
                        if self.checkLeft(other_player_coll,other_player_row):
                            availableMoves.append((other_player_coll-1,other_player_row))
                else:
                    availableMoves.append((current_player_coll,current_player_row - 1))
        return availableMoves

    def move_pawn(self,player_num, coordinates):
        """takes as parameters the player number and coordinates of where player wants to move
        returns True if player makes a valid move, returns false otherwise
        calls method checkvalid moves to see if the coordinates are in the list of valid moves
        updates gameboard cells, gameOver status and player position accordingly
        """
        if self._gameOver:
            return False
        if player_num == 1:
            current_player = self._playerOne
            other_player = self._playerTwo
        else:
            current_player = self._playerTwo
            other_player = self._playerOne
        if not current_player.get_isTurn():
            return False
        if coordinates in self.check_valid_moves(current_player,other_player):
            self._gameBoard[current_player.get_currentPos()[0]][current_player.get_currentPos()[1]].set_hasPawn(False)
            self._gameBoard[coordinates[0]][coordinates[1]].set_hasPawn(True)
            current_player.set_currentPos([coordinates[0],coordinates[1]])
            current_player.set_isTurn(False)
            other_player.set_isTurn(True)
            if self.is_winner(player_num):
                self._gameOver = True
            return True
        return False


    def checkFenceMoves(self,direction):
        """takes as a parameter the direction of fence a player is trying to place
        then systematically runs through the game board and returns a list of tuples of all
        the spaces not already occupied by that direction. will pass this list to place_fence when called
        """
        availableFenceMoves = []
        if direction == "v":
            for x in range(9):
                for y in range(9):
                    if not self._gameBoard[x][y].get_left():
                        availableFenceMoves.append((x,y))
        elif direction == "h":
            for x in range(9):
                for y in range(9):
                    if not self._gameBoard[x][y].get_behind():
                        availableFenceMoves.append((x, y))
        return availableFenceMoves

    def place_fence(self,player_num,direction,position):
        """checks the corresponding players number of fences
        if player is out of fences, it is not the players turn or if game is over return false
        calls check fence moves to get a list of all available fence moves for the given direction
        if the desired position is in the list of available moves updates the gameBoard, players turn, and returns True
        """
        if player_num == 1:
            player = self._playerOne
            other_player = self._playerTwo
        elif player_num == 2:
            player = self._playerTwo
            other_player = self._playerOne
        if not player.get_isTurn():
            return False
        if player.get_numOfFences() < 1:
            return False
        if self._gameOver:
            return False
        availableFenceMoves = self.checkFenceMoves(direction)
        if position in availableFenceMoves:
            if direction == "v":
                self._gameBoard[position[0]][position[1]].set_left(True)
                if position[0] - 1 >= 0:
                    self._gameBoard[position[0]-1][position[1]].set_right(True)
            if direction =="h":
                self._gameBoard[position[0]][position[1]].set_behind(True)
                if position[1] - 1 >= 0:
                    self._gameBoard[position[0]][position[1]-1].set_forward(True)
            player.set_isTurn(False)
            other_player.set_isTurn(True)
            player.decrementFences()
            return True
        return False

    def is_winner(self,player_num):
        """Takes a player number and returns whether or not the player won the game
        interacts with the player class to get the players current position"""
        if player_num == 1:
            if self._playerOne.get_currentPos()[1] == 8:
                return True
        if player_num == 2:
            if self._playerTwo.get_currentPos()[1] == 0:
                return True
        return False

class Player():
    """is a data member of class QuoridorGame keeps track of the players current position, number of fences remaining
    and boolean value of if it is the players turn, has getter/setter methods for the players turn/ current position
    """
    def __init__(self,start_coll,start_row,turn,forward_direc):
        """initializes the current position to the given collum/row, initializes turn status to given boolean, and initializes
         forward_direc to the given forward_direc
         """
        self._currentPos = [start_coll,start_row]
        self._isTurn = turn
        self._numOfFences = 10
        self._forward_direc = forward_direc

    def get_isTurn(self):
        """getter method for is turn"""
        return self._isTurn

    def get_numOfFences(self):
        """getter method for number of fences"""
        return self._numOfFences

    def decrementFences(self):
        """method to decrement number of fences"""
        self._numOfFences -= 1

    def set_isTurn(self,status):
        """set isTurn status to given status"""
        self._isTurn = status

    def get_currentPos(self):
        """gette method for the current position"""
        return self._currentPos

    def set_currentPos(self,newPosition):
        """setter method for the current position"""
        self._currentPos = newPosition

    def get_forwardDirec(self):
        """getter method for the forward direction"""
        return self._forward_direc

class Cell:
    """is a data member of Class QuoridorGame well communicate with it to update its fence values:
     FenceBehind,FenceForward, FenceLeft, FenceRight  and hasPawn values getter and setter methods for every data member
     are included in this class
     """
    def __init__(self,behind,forward,left,right):
        """initializes the fence properties to the given Boolean values
        for reference behind is the row direction approaching zero, forward approachingf 8
          right is collum approaching 8, left is row approaching 0
          """
        self._fenceBehind = behind
        self._fenceForward = forward
        self._fenceLeft = left
        self._fenceRight = right
        self._hasPawn = False

    def get_behind(self):
        """getter method for fenceBehind"""
        return self._fenceBehind

    def get_forward(self):
        """getter method for fenceForward"""
        return self._fenceForward

    def get_right(self):
        """getter method for fenceRight"""
        return self._fenceRight

    def get_left(self):
        """getterMethod for fenceLeft"""
        return self._fenceLeft

    def set_behind(self,behind):
        """setter method for fenceBehind"""
        self._fenceBehind = behind

    def set_forward(self,forward):
        """setterMethod for fence Forward"""
        self._fenceForward = forward

    def set_right(self, right):
        """setter method for fenceRight"""
        self._fenceRight = right

    def set_left(self, left):
        """setter Method for fenceLeft"""
        self._fenceLeft = left

    def set_hasPawn(self,status):
        """setter method for hasPawn"""
        self._hasPawn = status

    def get_hasPawn(self):
        """getter method for hasPawn"""
        return self._hasPawn

