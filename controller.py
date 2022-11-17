import model
import view

class controller:

    def userInput(input: str, playerTurn: int, list: list) -> int:
        allyAnimalList = []
        for i in list:
            if i.player == playerTurn:
                allyAnimalList.append(i.name)
        
        spaceList = []
        for i in range(1, 10):
            for j in range(0, 7):
                space = chr(ord("a") + j) + str(i)
                spaceList.append(space)

        if input == "info":
            return 0
        elif input == "exit":
            return 1
        elif input in allyAnimalList:
            return 2
        elif input in spaceList:
            return 3
        else:
            return 4
        