from direct.showbase.ShowBase import ShowBase

class TheGame(ShowBase): #Extend Showbase class to create the game class
    def __init__(self): #Initializing class
        ShowBase.__init__(self) #Initializing Showbase Class

game = TheGame() #creates game from TheGame
game.run() #starts the game

