from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
			print "Nice, you're not greedy, you win!"
			exit(0)
	else:
			dead("You greedy bastard!")
			

def male():
	print "Now you have a little boy."
	print "What're you gonna do with it?"
	print "1. Arm it"
	print "2. Train it"
	
	choice = raw_input("> ")
		
	if choice == "1":
		arm("Your little pet will be armed.")
	elif choice == "2":
		healthy("Your little pet is now very strong with the traning you have given.")
	else:
		print "It has beening waiting for too long. It dies from hunger!"
		exit(0)
			

def female():
	print "Now you have a little girl"
	print "What're you gonna do with it?"
	print "1. Feed her her favourite snacks"
	print "2. Train it"
	
	choice = raw_input("> ")
	
	if "1" in choice:
		print "She now becomes very obese and unhealthy."
		print "What're you gonna do with it?"
		print "1. Let it be."
		print "2. Encourage her to do some exercise."
		
		choice = raw_input("> ")
		
		if choice == "1":
			print "She eats too many snacks. She dies from obesity!"
			exit(0)
		elif choice == "2":
			healthy("She gets much healthier and looks much better than before.")
	elif "2" in choice:
		healthy("Your little pet is now very strong with the traning you have given.")
	else:
		print "It has beening waiting for too long. It dies from hunger!"
		exit(0)
		

def arm(why):
	print why, "Now choose what weapon you want for him.", "\n1. Spear", "\n2. Shield"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "It's dead because he didn't know how to use it."
		exit(0)
	elif choice == "2":
		healthy("He is growing healthily with the protection of the shield.")
	else:
		print "It has beening waiting for too long. It dies from hunger!"
		exit(0)
		
def healthy(why):
	print why, "\nFew years later, your pet meets a really nice partner. \nDo you want them to get married and have offsprings? \nYES or NO?"
	
	choice = raw_input("> ")
	
	if choice == "YES":
		print "They got married and now their baby is coming!"
		start()
	elif choice == "NO":
		print "Your pet is a real loner. It dies from loneiness!"
		exit(0)		

		
def start():
	print "Now you have an egg which is your new little pocket pet."
	print "You want a MALE one or a FEMALE one?"
	
	choice = raw_input("> ")
	
	if choice == "MALE":
		male()
	elif choice == "FEMALE":
		female()
	else:
		print "It has been waiting for too long. It dies from hunger!"
		exit(0)
		

start()