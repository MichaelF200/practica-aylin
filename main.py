def on_up_pressed():
    princes.vy = -100
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_spike,
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile3)

def on_on_overlap(sprite4, otherSprite):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

princes: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
princes = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . f f f f f f . . . .
        . . . . f f e e e e f 2 f . . .
        . . . f f e e e e f 2 2 2 f . .
        . . . f e e e f f e e e e f . .
        . . . f f f f e e 2 2 2 2 e f .
        . . . f e 2 2 2 f f f f e 2 f .
        . . f f f f f f f e e e f f f .
        . . f f e 4 4 e b f 4 4 e e f .
        . . f e e 4 d 4 1 f d d e f . .
        . . . f e e e e e d d d f . . .
        . . . . . f 4 d d e 4 e f . . .
        . . . . . f e d d e 2 2 f . . .
        . . . . f f f e e f 5 5 f f . .
        . . . . f f f f f f f f f f . .
        . . . . . f f . . . f f f . . .
        """),
    SpriteKind.player)
dragon = sprites.create(img("""
        ........................
        ........................
        ...........ccc..........
        ...........cccc.........
        .......ccc..ccccccc.....
        .......cccccc555555cc...
        ........ccb5555555555c..
        .....cc..b555555555555c.
        .....cccb555555ff155555c
        ......cb55555555ff55d55c
        ......b5555555555555555c
        ...cc.b555dd5555bb13bbc.
        ...cccd55ddddd555b3335c.
        .....bdddddddddd55b335c.
        ..cccdddddb55bbddd5555c.
        ..cccdddddb555bbbbcccc..
        ...ccddddddb5555cbcdc...
        ccccbdddddd5cb55cbcc....
        cddddddddd5555ccbbc.....
        .cddddddbdd555bbbcc.....
        ..ccdddbbbdd55cbcdc.....
        ....ccbbcbddddccdddcc...
        ......cccdd555dcccccc...
        ........cccccccc........
        """),
    SpriteKind.enemy)
moneda = sprites.create(img("""
        . . b b b b . .
        . b 5 5 5 5 b .
        b 5 d 3 3 d 5 b
        b 5 3 5 5 1 5 b
        c 5 3 5 5 1 d c
        c d d 1 1 d d c
        . f d d d d f .
        . . f f f f . .
        """),
    SpriteKind.food)
controller.move_sprite(princes, 100, 0)
scene.camera_follow_sprite(princes)
tiles.place_on_random_tile(princes, sprites.dungeon.collectible_red_crystal)
princes.ay += 300
tiles.place_on_random_tile(dragon, sprites.builtin.field1)