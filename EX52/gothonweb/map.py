class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
central_corridor = Scene("Central Corridor", "centreal_corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
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

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clickes open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.

You burst into the Bridge with the bomb under your arm and surprises 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of the fear that they will set off
the bomb under your arm.
""")

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they
can't get out. Now that the bomb is placed you run to the escape pod.

You rush through the ship desperately trying to make it to the escape pod. It seems
like there's no Gothons around, so you run as fast as possible. Eventually you reach
the room with escape pods, and you now need to pick one to take. Some of them could
be damaged, but you don't have time to look. There's 5 pods, which one do you take?
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it!
""")

the_end_loser = Scene("...", "the_end_loser",
"""
Meanwhile, the bomb exploded in the pod. All the innocent people were
there... You killed them all. Even though you survive but you will live
with guilty forever, you loser!
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

healthy = Scene("Healthy agian", "healthy",
"""
Thanks to the apples, they cure you. Now you are strong and
healthy again. Do you want to leave the island or stay?
""")

escape_pod_dodge = Scene("Escape Pod", "escape_pod",
"""
You had been swimming for more than 2 days. And here you are finally, the Escape Pod. Eventually
you reach the room with escape pods, and you now need to pick one to take. Some of them could be
damaged, but you don't have time to look. There's 5 pods, which one do you take?
""")

magic_power = Scene("You got some magic power", "magic_power",
"""
Now you know why this island is called "Magic Island".
All the mushrooms contain special supernatural power.
Once you eat them, you will have a strong magic power.
You could time travel back to whenever you want.
Which period do you want to travel back?
""")

central_corridor_dodge = Scene("Central Corridor", "centreal_corridor",
"""
You are here again. How is the time travelling experience?
Good? Exciting? The invaders are still here. What do you
want to do this time? Still dodge them or do other actions?
""")

one_bullet_left = Scene("One bullet to go", "one_bullet_left",
"""
You shoot them all down but one. And most importantly, you have only
one bullet left. This shot is critcal. Do you want to shoot him left or right?
""")

have_control = Scene("You have control", "have_control",
"""
Wow, you have made it. You are born to be a killer. Now
you have the control of the ship, which way do you want to go?
""")

have_control_shoot = Scene("You have control", "have_control",
"""
You found a gun in the first drawer and you shooted the man.
You are born to be a killer. Now you have the control of the ship,
which way do you want to go?
""")

tied = Scene("You got tied", "tied",
"""
Oh no...you missed the shot and he tied you. Now it's doomed. Wait...
there is a cupboard behind you. There must something to help you get out of here.
Do you want to open the first drawer, second drawer or the third drawer?
""")

phone = Scene("Phone", "phone",
"""
You found a phone in the second drawer. You open the contact list.
Emergency: 112
Head Quarter: 648394794801
Which number do you want to dial?
""")

laser_weapon_armory_shoot = Scene("Laser Weapon Armory", "laser_weapon_armory",
"""
You arrived the Weapon Armory. You leap through the Weapon Armory door.

You dive roll into the Weapon Armory, crouch and scan the room more Gothons
that might be hiding. It's dead quiet, too quiet. You stand up and run to the far
side of the room and find the neutron bomb in its container. There's a keypad lock
on the box and you need the code to get the bomb out. The code is 3 digits.
""")

the_end_winner_shoot = Scene("Head Quarter has control", "the_end_winner",
"""
You tell everything to the head quarter. And now, they will send
another team to the Weapon Armory to do the rest. You have already
done a great job. You will receive the highest honour from Gothon.
""")

generic_death_nth = Scene("Death", "death",
"""
This drawer has nothing in it...The man saw you opening
the drawer. He is now really mad and gonna take out his
gun...Booooooommbbbbbb! You are dead.
""")

generic_death_police = Scene("Death", "death",
"""
You called the police and guess what. They are too stupid
and said they didn't know where exactly you were and could
not help. You are dead.
""")

generic_death_poison = Scene("Death", "death",
"""
This meal is poisonous. That's why it is unfinished because
the last one who ate this could not finish it and died after
two bites. The corpse is still missing. Now it's your turn.
You are dead.
""")

generic_death = Scene("Death", "death",
"""
Looks like you bit the dust.
""")

# Define the action commands available in each Scene
escape_pod.add_paths({
    '1': the_end_loser,
    '2': the_end_winner,
    '3': the_end_loser,
    '4': the_end_loser,
    '5': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot':one_bullet_left,
    'dodge':island,
    'tell a joke': laser_weapon_armory
})

island.add_paths({
    'apples':healthy,
    'mushrooms':magic_power,
    'unfinished proper meal': generic_death_poison
})

healthy.add_paths({
    'leave':escape_pod_dodge,
    'stay': the_end_loser
})

magic_power.add_paths({
    'central corridor': central_corridor_dodge,
    'island': island
})

one_bullet_left.add_paths({
    'left': have_control,
    'right': tied
})

have_control.add_paths({
    'laser weapon armory': laser_weapon_armory_shoot,
    'home': the_end_loser
})

tied.add_paths({
    'first drawer': have_control_shoot,
    'second drawer': phone,
    'third drawer': generic_death_nth
})

phone.add_paths({
    '112': generic_death_police,
    '648394794801': the_end_winner_shoot
})

# Make some useful variables to be used in the web application
SCENES = {
    central_corridor.urlname : central_corridor,
    central_corridor_dodge.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    laser_weapon_armory_shoot.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    escape_pod_dodge.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_winner_shoot.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death,
    generic_death_nth.urlname : generic_death,
    generic_death_police.urlname : generic_death,
    generic_death_poison.urlname : generic_death,
    island.urlname : island,
    healthy.urlname : healthy,
    magic_power.urlname : magic_power,
    one_bullet_left.urlname : one_bullet_left,
    have_control.urlname : have_control,
    have_control_shoot.urlname : have_control,
    tied.urlname : tied,
    phone.urlname : phone
}
START = central_corridor
