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
        self.generateTerrain()
        self.setupCamera()

    #Loop for rendering terrain 20 x 20 x 10
    def generateTerrain(self):
        for z in range(10):         #stack of planes / height
            for y in range(20):     #a plane / width
                for x in range(20): #a line  / breadth
                    newBlockNode = render.attachNewNode('new-block-placeholder')
                    newBlockNode.setPos(
                        x * 2 - 20,
                        y * 2 - 20,
                        -z * 2
                    )
                    if z == 0:
                        self.grassBlock.instanceTo(newBlockNode)
                    else:
                        self.dirtBlock.instanceTo(newBlockNode)
    def setupCamera(self):
        self.disableMouse()
        self.camera.setPos(0, 0, 3)

    def loadModels(self):
        self.grassBlock =   loader.loadModel('assets/grass-block.glb') #loads the model
        self.dirtBlock  =   loader.loadModel('assets/dirt-block.glb')
        self.sandBlock  =   loader.loadModel('assets/sand-block.glb')
        self.stoneBlock =   loader.loadModel('assets/stone-block.glb')

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

