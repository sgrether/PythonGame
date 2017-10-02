class GameObject:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy, level):
        tiles = level.getTiles()
        #move by the given amount
        if not tiles[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self, console):
        #draw the character that represents this object at its position
        console.draw_char(self.x, self.y, self.char, self.color)

    def clear(self, console):
        #erase the character that represents this object
        console.draw_char(self.x, self.y, ' ', self.color, bg=None)
