from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

loadPrcFile('settings.prc')
class TheGame(ShowBase): #Extend Showbase class to create the game class

    def __init__(self): #Initializing class
        ShowBase.__init__(self) #Initializing Showbase Class
        grassBlock = loader.loadModel('assets/grass-block.glb')
        grassBlock.reparentTo(render) #render is equivalent to document object model, using "reparentTo" on block just attaches it to the screen
        
game = TheGame() #creates game from TheGame
game.run() #starts the game

