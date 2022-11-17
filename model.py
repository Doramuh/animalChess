import controller
import view

class pieces:
    def __init__(self, name, captureRank, player, position):
        self.name = name
        self.captureRank = captureRank
        self.player = player
        self.position = position

    def move(self, position: str, logic: bool):
        if logic is True:
            self.position = position
            pass

    def capture():
        pass


class board:
    def __init__(self, board):
        self.board = board
    
    def space():
        pass

    def reset():
        pass


class logic:
    def __init__(self):
        pass

    def captureLogic(self, chessName: str, space: str, nextSpace: str, player: int, rank: int, list: list):
        traps = ["c1","d2","e1","d8","c9","e9"]
        river = ["b4","b5","b6","c4","c5","c6","e4","e5","e6","f4","f5","f6"]
        if self.movementLogic(chessName, space, nextSpace, player, list) is False:
            return False
        
        for i in list:
            if i.position == nextSpace:
                enemyRank = i.captureRank
        
        if nextSpace in traps:
            return True

        if chessName == "rat":
            if space in river:
                return False
            
            elif enemyRank == 8:
                return True
        
        elif chessName == "elephant":
            if enemyRank == 1:
                return False
        
        if rank >= enemyRank:
            return True
        
        else: 
            return False


    def movementLogic(self, chessName: str, space: str, nextSpace: str, player: int, list: list) -> bool:
        # true if movement
        # false if error
        river = ["b4","b5","b6","c4","c5","c6","e4","e5","e6","f4","f5","f6"]
        riverJump = []
        riverJumpFile = ["a","b","c","d","e","f","g"]
        potentialSpace = []
        potentialSpace.append(str(chr(ord(space[0]) + 1)) + space[1])
        potentialSpace.append(str(chr(ord(space[0]) - 1)) + space[1])
        potentialSpace.append(space[0] + str(int(space[1]) + 1 ))
        potentialSpace.append(space[0] + str(int(space[1]) - 1 )) 

        for i in riverJumpFile:
            if i in ["a","d","g"]:
                for j in range(4, 7):
                    riverJump.append(i + str(j))
            elif i in ["b","c","e","f"]:
                riverJump.append(i + "3")
                riverJump.append(i + "7")
                
            elif i in ["b","c","e","f"]:
                riverJump.append()

        allyPositionList = []
        enemyPositionList = []

        for i in list:
            if i.player == player:
                allyPositionList.append(i.position)
            else:
                enemyPositionList.append(i.position)

        valid = False

        if chessName == "tiger" or chessName == "lion":

            if nextSpace in allyPositionList:
               return valid

            elif nextSpace in potentialSpace:
                valid = True
                return valid

            elif space in riverJump and nextSpace in riverJump:
                if space[0] == nextSpace[0] or space[1] == nextSpace[1]:
                    valid = True
                    return valid
            else:
                return valid
        
        elif chessName == "rat":

            if nextSpace in allyPositionList:
               return valid
            elif nextSpace in potentialSpace:
                valid = True
                return valid
            else:
                return valid
        
        elif nextSpace in allyPositionList:
            return valid
        
        elif nextSpace in river:
            return valid

        elif nextSpace in potentialSpace:
            valid = True
            return valid

        else:
            return valid

    def winCondition(self, list: list) -> bool:
        playerList = []
        for i in list:
            playerList.append(i.player)
        for i in list:
            if i.position == "d1" or i.position == "d9":
                return True
            if 1 not in playerList or 2 not in playerList:
                return True

        return False

    def start(self) -> list:
        list = []
        list.append(pieces("tiger", 6, 1, "a1"))
        list.append(pieces("lion", 7, 1, "g1"))
        list.append(pieces("cat", 2, 1, "b2"))
        list.append(pieces("dog", 3, 1, "f2"))
        list.append(pieces("elephant", 8, 1, "a3"))
        list.append(pieces("wolf", 4, 1, "c3"))
        list.append(pieces("leopard", 5, 1, "e3"))
        list.append(pieces("rat", 1, 1, "g3"))

        list.append(pieces("tiger", 6, 2, "g9"))
        list.append(pieces("lion", 7, 2, "a9"))
        list.append(pieces("cat", 2, 2, "f8"))
        list.append(pieces("dog", 3, 2, "b8"))
        list.append(pieces("elephant", 8, 2, "g7"))
        list.append(pieces("wolf", 4, 2, "e7"))
        list.append(pieces("leopard", 5, 2, "c7"))
        list.append(pieces("rat", 1, 2, "a7"))

        return list

    def end():
        pass
