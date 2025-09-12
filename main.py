from direct.showbase.ShowBase import ShowBase #Imports ShowBase class, the the game "Window"
from panda3d.core import loadPrcFile
from panda3d.core import DirectionalLight #Imports the directional light class. Instance of which is used to create directional light in the scene
from panda3d.core import AmbientLight #Imports the ambient light class. Instace of it is used to create global illumination in the game
loadPrcFile('settings.prc')
class TheGame(ShowBase): #Extend Showbase class to create the game class

    def __init__(self):         #Initializing class
        ShowBase.__init__(self) #Initializing Showbase Class
        
        self.loadModels()
        self.setupLights()
    
    def loadModels(self):
        
        self.grassBlock = loader.loadModel('assets/grass-block.glb')
        self.grassBlock.reparentTo(render) #render is equivalent to document object model, using "reparentTo" on block just attaches it to the screen
        self.grassBlock.setPos(0,0,0)        

        self.dirtBlock = loader.loadModel('assets/dirt-block.glb')
        self.dirtBlock.reparentTo(render)
        self.dirtBlock.setPos(0,2,0)

        self.sandBlock = loader.loadModel('assets/sand-block.glb')
        self.sandBlock.reparentTo(render)
        self.sandBlock.setPos(2,0,0)

        self.stoneBlock = loader.loadModel('assets/stone-block.glb')
        self.stoneBlock.reparentTo(render)
        self.stoneBlock.setPos(2,2,0)

    def setupLights(self):
        mainLight = DirectionalLight('Main Light')  #Creates instance from DirectionaLight class called main light
        mainLightNodePath = render.attachNewNode(mainLight) #Attaches the instance object to render creating a node
        mainLightNodePath.setHpr(30,-60, 0) #Hpr means Heading, Pitch, Roll. i.e The spatial rotation data.
                                            #Heading -> X axis rotation data , Pitch -> Y axis rotation data, Roll -> Z-axis rotation data 
        render.setLight(mainLightNodePath) #Set light
        
        globalLight = AmbientLight('Global Illumination')       #
        globalLight.setColor((0.3, 0.3, 0.3, 1))
        globalLightNodePath = render.attachNewNode(globalLight)
        render.setLight(globalLightNodePath)
        
game = TheGame() #creates game from TheGame
game.run() #starts the game

