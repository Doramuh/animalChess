import model
import controller

class consoleIO:
    def __init__(self):
        pass

    def consoleInput() -> str:
        userInput = input()
        return userInput

    def consoleOutput(input: str):
        print(input)
