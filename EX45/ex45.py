from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to print out the last scene
		current_scene.enter()
		
class EnterFlight(Scene):
	
	def enter(self):
		print "Welcome aboard LPTHW airline."
		print "I'm your captain E.C."
		print "You'll now be able to choose among\nAsia\nEurope\nAfrica\nAustralia\nAntarctica\nNorth America\nSouth America"
		print "Which one do you like the best?"
		
		action = raw_input("> ")
		
		if action == "Asia":
			print "Umm...would be a nice adventure."
			print "See you there soon!"
			print "-" * 20
			return 'asia'
			
		elif action == "Europe":
			print "I heard that there are a lot to see. Have fun!"
			print "See you there soon!"
			print "-" * 20
			return 'europe'
			
		elif action == "Africa":
			print "Wow...good choice and good luck mate!"
			print "See you there soon!"
			print "-" * 20
			return 'africa'
			
		elif action == "Australia":
			print "Can't you just choose somewhere more challenging?"
			print "See you there soon!"
			print "-" * 20
			return 'australia'
						
		elif action == "Antarctica":
			print "Wow...did you bring enoguh clothes?"
			print "See you there soon!"
			print "-" * 20
			return 'antarctica'
			
		elif action == "North America":
			print "Wish you a nice trip."
			print "See you there soon!"
			print "-" * 20
			return 'north_america'
			
		elif action == "South America":
			print "Oh...i can feel the hotness already."
			print "See you there soon!"
			print "-" * 20
			return 'south_america'
			
		else:
			print "Please choose before you jump out of the window!"
			return 'enter_flight'
			
class Asia(Scene):
	
	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "We are now in Thailand."
		print "Do you have a clue where that is?"
		print "Anyway, here we have a fortune teller to tell you your future."
		print "'Hi, little. I'm Chakrii Chaow. I can tell you anything you wanna know."
		print "I have heard that you have been chosen for the adventure."
		print "There will be a big trouble in your life...I am sure this adventure would be very dangerous"
		print "and maybe you won't survive this...'"
		print "Do you trust him? Yes or No?"
		
		action = raw_input("> ")
		
		if action == "Yes":
			print "You start to panic."
			print "Suddenly, there is a flood coming and you fall into the water."
			print "The fortune teller was right..."
			return 'death'
			
		if action == "No":
			print "'Nobody ever doubts me like you!'"
			print "*trick*"
			print "'Now wait for the animals to eat you up'"
			print "You can't see anything but black and you feel that you are flying."
			print "-" * 20
			return 'africa' 
			
			
class Europe(Scene):

	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "We are now in Germany, beer country!!!!!!"
		print "You can have as many beers as you can."
		print "Soooooo, how many bottles you want?"
		
		choice = raw_input("> ")
		how_much = int(choice)
		
		if how_much <=  15:
			print "Hahahahaha man...you can't even walk properly."
			print "You walk into a tunnel."
			print "It's so dark inside."
			print "-" * 20
			return 'finished'
			
		elif how_much > 16:
			print "You are totally drunk like shit."
			print "You are moved by somebody."
			print "-" * 20
			return 'africa'	
					
		else:
			print "Are you already drunk? You don't know how to type numbers?"
			return 'europe'
			

			
class Africa(Scene):

	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "We are now in Kenya."
		print "There are so many animals migrating."
		print "There is the lion king."
		print "Oh no, he spots you."
		print "Are you gonna run or try to fight with him? Run or Fight?"
		
		action = raw_input("> ")
		
		if action == "Run":
			print "You are not as fast as him..."
			return 'death'
			
		elif action == "Fight":
			print "You such a brave guy."
			print "Here you have the gun."
			print "Are you gonna kill him? Yes or No?"
			
			action = raw_input("> ")
			
			if action == "Yes":
				print "You are such a cruel guy."
				print "The other baby lions eat you up."
				return 'death'
				
			elif action == "No":
				print "You are brave and kind."
				print "The baby lions like you and see you as their new father."
				print "You sit on one of them and he will take you home."
				print "-" * 20
				return 'finished'
				
			else:
				print "Oh no, we have been waiting too long..."
				print "The lion king has......alrea....."
				return 'death'
			
		else:
			print "Oh no, we have been waiting too long..."
			print "The lion king has......alrea....."
			return 'death'
						
			
class Antarctica(Scene):
	
	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "Wow...it's so freaking cold here."
		print "Which way you wanna go? Go down the water or stay there and wait for help? Go down or Stay?"
		
		action = raw_input("> ")
		
		if action == "Go down":
			print "It's much warmer down here."
			print "There is a flow pushing you forward."
			print "Wooooooooow"
			print "-" * 20
			return 'finished'
			
		elif action == "Stay":
			print "You are getting colder and colder."
			print "Are you sure you wanna stay? Yes or No?"
			
			action = raw_input("> ")
			
			if action == "Yes":
				print "I like your persistence"
				print "But...it's just too cold."
				return 'death'
				
			elif action == "No":
				print "It's much warmer down here."
				print "There is a flow pushing you forward."
				print "Wooooooooow"
				print "-" * 20
				return 'finished'
			
			else:
				print "It's too cold..."
				return 'death'
		
		else:
			print "I am sorry...my brain doesn't work well under this freezing weather. What do you mean again?"
			return "antarctica"
			
class Australia(Scene):
	
	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "Wow...the view in Aussie is just tooooo great."
		print "Now we have three boats for you to choose."
		print "Which one do you prefer? 1? 2? or 3?"
		
		pirate_boat = randint(1,3)
		guess = raw_input("Boat: ")
		
		if int(guess) == pirate_boat:
			print "Oh shit...the pirates are so angry because you got on their boat."
			print "What are you gonna do? Run or Fight?"
			
			action = raw_input("> ")
			
			if action == "Run":
				print "You such a coward!"
				print "They caught you and stole all the money from you."
				print "The captain is walking closer..."
				print "Oh.......no....."
				return 'death'
				
			elif action == "Fight":
				print "You are very brave!"
				print "You see a sword on the ground."
				print "Do you wanna get it? Yes or No?"
				
				action = raw_input("> ")
				
				if action == "Yes":
					print "That's a magic sword."
					print "You know how to fight against them with this magic sword."
					print "Wow, you win the fight."
					print "Now you have the control of the boat."
					print "-" * 20
					return 'finished'
				
				elif action == "No":
					print "The captain and other pirates are beating you up."
					print "Oh no...you are bleeding so hard."
					return 'death'
				
			else:
				print "Oh no, we have been waiting too long..."
				print "The pirates hav......alrea....."
				return 'death'
						
		else:
			print "You have chosen a boat on the way to your home."
			return 'finished'

			
class NorthAmerica(Scene):
	
	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "I am feeling hotter here in Jamaica."
		print "Is it your first time to be here?"
		print "There is a group of people coming and singing"
		print "'Down the way where the nights are gray...'"
		print "Do you know what the next line is?"
		
		action = raw_input("> ")
		
		if action == "And the sun shines daily on the mountain top":
			print "Wow you know the song!"
			print "They seem to like you so much."
			print "They said they could drive you home."
			print "-" * 20
			return 'finished'
			
		else:
			print "You don't know the song 'Jamaica Farewell'?"
			print "They seem to be very angry and sad..."
			print "They kick you out of Jamaica"
			print "-" * 20
			return 'south_america'
			
	

class SouthAmerica(Scene):
	
	def enter(self):
		print "Welcome welcome! Happy to meet you again!"
		print "Oh god...it's freaking hot here in Brazil."
		print "Some soccer players invite you to play penalty-kick with them."
		print "They said if you win, they will let you join their team."
		print "Now, shoot Right or Left?"
		
		action = raw_input("> ")
		
		if action == "Right":
			print "GOAAAAALLLLLLLLLLLLLLLLLL!"
			print "You are born to be a soccer."
			print "Now you are one of their team members."
			print "---3 MONTHS LATER---"
			print "Your team wins the league."
			print "Now you have the money to go home."
			print "-" * 20
			return 'finished'
		
		elif action == "Left":
			print "No...the goal keeper caatches the ball."
			print "Man...you need to train yourself tho. Come back later!"
			print "-" * 20
			return 'enter_flight'
			
		else:
			print "Time out! Again."
			return 'south_america'
	
	
class Death(Scene):
		
		def enter(self):
			print "YOU ARE DEAD"
			print "I am sorry. I shouldn't have chosen you to this adventure..."
			exit(1)
			
class Finished(Scene):
	
	def enter(self):
		print "Finally you are home. Congrats!"
		return 'finished'
		
class Map(object):
	
	scenes = {
		'enter_flight': EnterFlight(),
		'asia': Asia(),
		'europe': Europe(),
		'africa': Africa(),
		'antarctica': Antarctica(),
		'australia': Australia(),
		'north_america': NorthAmerica(),
		'south_america': SouthAmerica(),
		'death' : Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('enter_flight')
a_game = Engine(a_map)
a_game.play()