def render(world, color_dark_wall, color_dark_ground):
    level = world.getMap()
    #go through all tiles, and set their background color
    for y in range(level.getMapHeight()):
        for x in range(level.getMapWidth()):
            wall = level.getTiles()[x][y].block_sight
            if wall:
                world.console.draw_char(x, y, None, fg=None, bg=color_dark_wall)
            else:
                world.console.draw_char(x, y, None, fg=None, bg=color_dark_ground)

    #draw all objects in the list
    for obj in world.getObjects():
        obj.draw(world.console)

    '''
    #Erase objects old locations
    for obj in world.getObjects():
        obj.clear(world.console)

    '''
    #blit the contents of "con" to the root console and present it
    world.root.blit(world.console, 0, 0, world.screenWidth, world.screenHeight, 0, 0)
