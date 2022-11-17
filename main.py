import model
import controller
import view

gameState = True

logic = model.logic()
view = view.consoleIO
controller = controller.controller

playerTurn = 1
enemyPlayerTurn = 2
pieceList = logic.start()

spaceList = []
for i in range(1, 10):
    for j in range(0, 7):
        space = chr(ord("a") + j) + str(i)
        spaceList.append(space)

while gameState:
    enemyPositionList = []
    for i in pieceList:
        if i.player == enemyPlayerTurn:
            enemyPositionList.append(i.position)

    view.consoleOutput("*****************************")
    print(f"It is player {playerTurn} turn, choose your piece")

    for i in pieceList:
        if i.player == playerTurn:
            print(f'{i.name} {i.position}')
    view.consoleOutput("*****************************")

    inputName = view.consoleInput()
    case1 = controller.userInput(inputName, playerTurn, pieceList)

    if case1 == 0:
        view.consoleOutput("*****************************")
        for i in pieceList:
            if i.player != playerTurn:
                print(f'{i.name} {i.position}')
        view.consoleOutput("*****************************")
        case1 = -1

    elif case1 == 1:
        quit()
    
    elif case1 == 2:
        for i in pieceList:
            if i.player == playerTurn:
                if inputName in i.name:
                    current = i.position
                    player = i.player
                    rank = i.captureRank
                    inputSpace = view.consoleInput()
                    case2 = controller.userInput(inputSpace, playerTurn, pieceList)
                    if case2 == 0:
                        view.consoleOutput("*****************************")
                        for i in pieceList:
                            if i.player != playerTurn:
                                print(f'{i.name} {i.position}')
                        view.consoleOutput("*****************************")
                        case2 = -1
                    
                    elif case2 == 1:
                        quit()
                    
                    elif case2 == 3:
                        if inputSpace in enemyPositionList:
                            if logic.captureLogic(inputName, current, inputSpace, player, rank, pieceList) is True:
                                for j in pieceList:
                                    if inputSpace == j.position:
                                        print(f'{j.name[0].upper() + j.name[1:]} has been captured')
                                        pieceList.remove(j)
                                i.position = inputSpace
                                turn = playerTurn
                                playerTurn = enemyPlayerTurn
                                enemyPlayerTurn = turn
                                inputSpace = "null"
                                inputName = "null"
                                case1 = -1
                                case2 = -1
                            
                            else:
                                view.consoleOutput("Cannot capture selected piece, try again")
                                case1 = -1
                                case2 = -1
                            # break

                        elif logic.movementLogic(inputName, current, inputSpace, player, pieceList) is True:
                            i.position = inputSpace
                            turn = playerTurn 
                            playerTurn = enemyPlayerTurn
                            enemyPlayerTurn = turn
                            inputSpace = "null"
                            inputName = "null"
                            case1 = -1
                            case2 = -1
                        else:
                            view.consoleOutput("Cannot move to selected space, try again")
                            case1 = -1
                            case2 = -1
                    
                    elif case2 == 2 or case2 == 4:
                        view.consoleOutput("Incorrect input, try again")
                        case1 = -1
                        case2 = -1
    
    elif case1 == 3 or case1 == 4:
        view.consoleOutput("Incorrect input, try again")
        case1 = -1
        case2 = -1

    gameState = not logic.winCondition(pieceList)

print(f'Player {enemyPlayerTurn} wins')