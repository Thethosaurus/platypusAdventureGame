platypoints = 0


print """You are a platypus. You were once captured and put into a zoo, but you escaped. 
Now as a rogue platypus, you must integrate yourself into human society. 
Your actions determine how obvious it is that you are actually a platypus, not a human. 
Actions that are non-humanlike add platypoints to your platypoints score. 
If you go over 10 platypoints, then you are fully visible to all people, and you will be discovered as a 
rogue platypus, leading to your reincarceration at the local zoo."""
ready = raw_input("Are you ready? Type yes if ready!")
while (ready == "no"):
	ready = raw_input("how about now?")
if (ready == "yes"):
	name = raw_input("What is your name?")
	print "Welcome to the platyteam %r. Be as inconspicuous as possible." %name
	print """Two days have passed since your escape, %r.
You are feeling hungry, and decide it is time to go buy groceries.
after a 10 minutes drive, with enjoyable music, you arrive at the store.""" % name
	store = raw_input("""What do you do at the grocery store?
		type 1 if you take a shopping cart and buy food.
		type 2 if you grab ice from a bag and pelt it at the wall.
		type 3 if you pee in the corner, marking your territory.
		>""")
	if (store == '1'):
		platypoints += 2
		print """You managed to make it to the checkout line until the cashier asked for ID.
		You broke into a sweat and and looked around. You found nothing.
		You look back at the cashier, who is staring expectingly. 
		You throw your money onto the checkout stand and run away.
		The cashier doesn't care about their job enough to chase you.
		You get away."""
		print "You are at ", platypoints, "platypoints!"
		print """Later in the week, you realize that you need to do your laundry.
		You have no washer or dryer, so you run down to the laundromat."""
		laundry = raw_input("""What do you do at the laundromat?
			type 1 if you realize you have no laundry detergent so you use shampoo
			type 2 if you drink the free coffee until closing time
			type 3 if you eat someone's sock
			>""")
		if (laundry == '1'):
			platypoints += 5
			print """The store staff takes a picture of you and hangs it on the wall.
			The frame reads "The biggest idiot of the year"
			The whole city knows about you."""
			print "You are at ", platypoints, "platypoints!"
		elif (laundry == '2'):
			platypoints += 3
			print """The manager asks you to leave at closing time, but you continue drinking coffee.
			You are hyped up to the point where you don't know where you are.
			You are zooming at light speed through the galaxy.
			You don't see the manager. The manager is nothing in the universe.
			You see all truth. You see the future.
			You are enlightened. 
			You now know all of the answers in the universe, and have seen all good and evil.
			You wake up in a puddle of your drool on the sidewalk."""
			print "You are at ", platypoints, "platypoints!"
		elif(laundry == '3'):
			platypoints += 8
			print """The sock tastes good. You eat another one. Then another.
			Soon enough, all socks have been devoured. 
			The crisp taste compliments the socks texture.
			You are addicted to eating socks."""
			print "You are at ", platypoints, "platypoints!"
		else :
			print "You compromised your position, platydummy."
	elif (store == '2'):
		platypoints += 5
		print """The store manager came out to talk to you.
		The manager asked you why you were throwing ice at the wall.
		You are illiterate and cannot speak English.
		You pee on the manager's shoe and escape."""
		print "You are at ", platypoints, "platypoints!"
		print """Later in the week, you realize that you need to do your laundry.
		You have no washer or dryer, so you run down to the laundromat."""
		laundry = raw_input("""What do you do at the laundromat?
			type 1 if you realize you have no laundry detergent so you use shampoo
			type 2 if you drink the free coffee until closing time
			type 3 if you eat someone's sock
			>""")
		if (laundry == '1'):
			platypoints += 5
			print """The store staff takes a picture of you and hangs it on the wall.
			The frame reads "The biggest idiot of the year"
			The whole city knows about you."""
			print "You are at ", platypoints, "platypoints!"
		elif (laundry == '2'):
			platypoints += 3
			print """The manager asks you to leave at closing time, but you continue drinking coffee.
			You are hyped up to the point where you don't know where you are.
			You are zooming at light speed through the galaxy.
			You don't see the manager. The manager is nothing in the universe.
			You see all truth. You see the future.
			You are enlightened. 
			You now know all of the answers in the universe, and have seen all good and evil.
			You wake up in a puddle of your drool on the sidewalk."""
			print "You are at ", platypoints, "platypoints!"
		elif(laundry == '3'):
			platypoints += 8
			print """The sock tastes good. You eat another one. Then another.
			Soon enough, all socks have been devoured. 
			The crisp taste compliments the socks texture.
			You are addicted to eating socks."""
			print "You are at ", platypoints, "platypoints!"
		else :
			print "You compromised your position, platydummy."
	elif(store == '3'):
		platypoints += 8
		print """You mark your territory.
		Everyone passing by stares at you.
		You don't understand embarassement so you waddle in your pee.
		You leave a few hours later, not realizing what you have done."""
		print "You are at ", platypoints, "platypoints!"
		print """Later in the week, you realize that you need to do your laundry.
		You have no washer or dryer, so you run down to the laundromat."""
		laundry = raw_input("""What do you do at the laundromat?
			type 1 if you realize you have no laundry detergent so you use shampoo
			type 2 if you drink the free coffee until closing time
			type 3 if you eat someone's sock
			>""")
		if (laundry == '1'):
			platypoints += 5
			print """The store staff takes a picture of you and hangs it on the wall.
			The frame reads "The biggest idiot of the year"
			The whole city knows about you."""
			print "You are at ", platypoints, "platypoints!"
		elif (laundry == '2'):
			platypoints += 3
			print """The manager asks you to leave at closing time, but you continue drinking coffee.
			You are hyped up to the point where you don't know where you are.
			You are zooming at light speed through the galaxy.
			You don't see the manager. The manager is nothing in the universe.
			You see all truth. You see the future.
			You are enlightened. 
			You now know all of the answers in the universe, and have seen all good and evil.
			You wake up in a puddle of your drool on the sidewalk."""
			print "You are at ", platypoints, "platypoints!"
		elif(laundry == '3'):
			platypoints += 8
			print """The sock tastes good. You eat another one. Then another.
			Soon enough, all socks have been devoured. 
			The crisp taste compliments the socks texture.
			You now have a crippling addiction for eating socks."""
			print "You are at ", platypoints, "platypoints!"
		else :
			print "You compromised your position, platydummy."
	else :
		print "Not a valid platy answer!"

else :
	print "That is not platypus like!"
