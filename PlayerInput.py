def playerInput(tdl, player, level):
    #realtime input handling
    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
           user_input = event
           keypress = True
    if not keypress:
        return

    if user_input.key == 'UP':
        player.move(0, -1, level)

    elif user_input.key == 'DOWN':
        player.move(0, 1, level)

    elif user_input.key == 'LEFT':
        player.move(-1, 0, level)

    elif user_input.key == 'RIGHT':
        player.move(1, 0, level)

    if user_input.key == 'ENTER' and user_input.alt:
        #Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())

    elif user_input.key == 'ESCAPE':
        return True  #exit game
