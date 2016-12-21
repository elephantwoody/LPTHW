from nose.tools import *
from map import *

def test_room():
    gold = Scene("GoldScene", "goldroom", """
    This room has gold in it you can grab. There's a door
    to the north.
    """)
    assert_equal(gold.title, "GoldScene")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})

def test_room_paths():

    central_corridor = Scene("central Corridor", "central_corridor",
    """The Gothons of Planet Percal #25 have invaded your ship and destroyed
    your entire crew. You are the last surviving member (oh noes!) and your
    last mission is to get the neutron destruct bomb from the Weapons Armory,
    put it in the bridge, and blow up the ship after getting into an escape pod.

    You're now running down the central corridor to the Weapons Armory when a
    Gothon hops out in an evil clown costume filled with hate. He's blocking the door
    to the Armory and about to pull a weapon to blast you.
    """)

    laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory",
    """
    Lucky for you they made you learn Gothon insults in the academy.
    You tell the one Gothon joke you know:
    Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr.
    The Gothon bursts into laughter and rolls around on the ground. While insults laughing
    you run up and use your copy of Nietzsche's notebooks (translated into Gothon)
    to lecture the Gothon on the shaky foundations of its ideologies. While it tries
    to cope with its existential crisis, you leap through the Weapon Armory door.

    You dive roll into the Weapon Armory, crouch and scan the room more Gothons
    that might be hiding. It's dead quiet, too quiet. You stand up and run to the far
    side of the room and find the neutron bomb in its container. There's a keypad lock
    on the box and you need the code to get the bomb out. The code is 3 digits.
    """)
    one_bullet_left = Scene("One bullet to go", "one_bullet_left",
    """
    You shoot them all down but one. And most importantly, you have only
    one bullet left. This shot is critcal. Do you want to shoot him left or right?
    """)
    island = Scene("Welcome to Magic Island", "island",
    """
    You have been thrown out from the ship and now landed on this Magic Island.
    This island is so quiet. You walk around and explore a bit. A few hours later,
    you feel so hungry and exhausted. You really need some food.

    You walk and walk...Oh, there are some food! You see some apples on the tree,
    some mushrooms on the ground, and wait...an unfinished proper meal.
    Which one do you choose?
    """)

    central_corridor.add_paths({'tell a joke': laser_weapon_armory, 'shoot': one_bullet_left,
                                'dodge': island})
    assert_equal(central_corridor.go('tell a joke'), laser_weapon_armory)
    assert_equal(central_corridor.go('shoot'), one_bullet_left)
    assert_equal(central_corridor.go('dodge'), island)

def test_map():
    start = Scene("Start", "start", "You can go west and down a hole.")
    west = Scene("Trees", "trees", "There are trees here, you can go east.")
    down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    room = START.go('shoot')
    assert_equal(room, one_bullet_left)
    room = START.go('dodge')
    assert_equal(room, island)
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
