from direct.showbase.ShowBase import ShowBase #Imports ShowBase class, the the game "Window"
from panda3d.core import loadPrcFile
from panda3d.core import DirectionalLight #Imports the directional light class. Instance of which is used to create directional light in the scene
from panda3d.core import AmbientLight #Imports the ambient light class. Instace of it is used to create global illumination in the game
loadPrcFile('settings.prc')
class TheGame(ShowBase): #Extend Showbase class to create the game class

    def __init__(self):         #Initializing class
        ShowBase.__init__(self) #Initializing Showbase Class

    
        grassBlock = loader.loadModel('assets/grass-block.glb')
        grassBlock.reparentTo(render) #render is equivalent to document object model, using "reparentTo" on block just attaches it to the screen
        grassBlock.setPos(0,0,0)        

        dirtBlock = loader.loadModel('assets/dirt-block.glb')
        dirtBlock.reparentTo(render)
        dirtBlock.setPos(0,2,0)

        sandBlock = loader.loadModel('assets/sand-block.glb')
        sandBlock.reparentTo(render)
        sandBlock.setPos(2,0,0)

        stoneBlock = loader.loadModel('assets/stone-block.glb')
        stoneBlock.reparentTo(render)
        stoneBlock.setPos(2,2,0)


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

