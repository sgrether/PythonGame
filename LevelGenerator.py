class Map:
    def __init__(self, width, height):
        self.mapWidth = width
        self.mapHeight = height

    def makeMap(self):
        #fill map with "unblocked" tiles
        self.tiles = [[Tile(False) for y in range(self.mapHeight)] for x in range(self.mapWidth)]

        #place two pillars to test the map
        self.tiles[30][22].blocked = True
        self.tiles[30][22].block_sight = True
        self.tiles[50][22].blocked = True
        self.tiles[50][22].block_sight = True

    def getTiles(self):
        return self.tiles

    def getMapHeight(self):
        return self.mapHeight

    def getMapWidth(self):
        return self.mapWidth

class Tile:
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight
