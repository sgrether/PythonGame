'''
http://www.roguebasin.com/index.php?title=Roguelike_Tutorial,_using_python3%2Btdl
Used this tutorial to get the basics
I separated pieces into their own files for readability
'''

import tdl
from GameObject import GameObject
from PlayerInput import playerInput
from LevelGenerator import Map
from Render import render

#Set constants for screen size and FPS
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#Constans for Map size
MAP_WIDTH = 80
MAP_HEIGHT = 45

#Colors for the ground and walls (temporary set up)
color_dark_wall = (0, 0, 100)
color_dark_ground = (50, 50, 150)

#World class that has console, map, and object data
#I'd like to move this class to it's own file, but haven't gotten around to it yet
class World:
    def __init__(self, screenWidth, screenHeight, fps):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        #set up window through tdl
        tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
        self.root = tdl.init(screenWidth, screenHeight, title="Roguelike", fullscreen=False)
        self.console = tdl.Console(screenWidth, screenHeight)
        tdl.setFPS(fps)

        self.objects = []

    #Set a font for the objects
    def setFont(self, image, grey, layout):
        tdl.set_font(image, greyscale=True, altLayout=True)

    #Create a map object of given size
    def createMap(self, mapWidth, mapHeight):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.map = Map(MAP_WIDTH, MAP_HEIGHT)
        self.map.makeMap()

    #Create a GameObject and add it to our array
    def createObject(self, x, y, char, color):
        self.objects.append(GameObject(x, y, char, color))

    def getObjects(self):
        return self.objects

    def getMap(self):
        return self.map

    def getObjects(self):
        return self.objects

#World initialization
world = World(SCREEN_WIDTH, SCREEN_HEIGHT, LIMIT_FPS)

#Make Player
world.createObject(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, '@', (255, 255, 255))
#Make NPC
world.createObject(SCREEN_WIDTH//2 - 5, SCREEN_HEIGHT//2, '@', (255,255,0))

#Make Map
world.createMap(MAP_WIDTH, MAP_HEIGHT)

#Main Game Loop
while not tdl.event.is_window_closed():
    #Draw all objects
    render(world, color_dark_wall, color_dark_ground)

    #Flush screen every frame, required for tdl loops
    tdl.flush()

    #Erase objects old locations
    for obj in world.getObjects():
        obj.clear(world.console)

    #Read input and close game if escape is pressed
    exit_game = playerInput(tdl, world.getObjects()[0], world.getMap())
    if exit_game:
        break;
