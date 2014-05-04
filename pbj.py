# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

#variables are amounts of ingredients. One full sandwich is 2 slices of bread, and one spoonful each of peanut butter and jelly.

bread =13 #slices
jelly = 0 #spoonfuls
pb = 9  #spoonfuls

if bread/2==1 or jelly==1 or pb==1:
	plural="sandwich"
else:
	plural="sandwiches"
if jelly==1:
	jspoon="spoonful"
else:
	jspoon="spoonfuls"
if pb==1:
	pspoon="spoonful"
else:
	pspoon="spoonfuls"
if bread==1:
	slice="slice"
	plural="sandwiches"
else:
	slice="slices"

#greeting
print "\nHi!\nWe\'re going to figure out if you can make a PB&J.\n"

#inventory
print "You have:\n{0} {5} of bread,\n{1} {3} of jelly, and\n{2} {4} of peanut butter.\n".format(bread, jelly, pb, jspoon, pspoon, slice)

if bread >=2 and jelly >=1 and pb >=1:
	print "It looks like you have enough ingredients for PB&J.\n"
	
else:
	print "No PB&J for you!\n"

#how many can you make?

#bread limiting
if bread/2 <= jelly and 0 < bread/2 <=pb and bread % 2 != 1:	
	print "You have enough bread for {0} {1}.\n".format(bread/2, plural)
elif bread/2 +1<= jelly and bread/2 +1<=pb and bread%2==1:	
	print "You have enough ingredients to make {0} full {1} and one open face sandwich.\n".format(bread/2, plural)

#jelly limiting
elif jelly <= bread/2 and jelly >0: #more bread than jelly
	if jelly < pb: #more jelly than pb
		print "But you only have enough jelly to make {0} {1}.\n".format(jelly, plural)
	if pb == 0 and bread != 0: #no pb
		print "But you still can make {0} jelly {1}.\n".format(jelly, plural)
	
	
elif jelly >= bread/2 and jelly > 0 == pb: #more jelly than bread and no pb
	if bread % 2 ==1: # odd slice of bread
		print "But you still can make {0} jelly {1} and one open face jelly sandwich.\n".format(bread/2, plural)
	if 0 != bread % 2 != 1: # not odd, non zero
		print "But you still can make {0} jelly {1}.\n".format(bread/2, plural)
	
# elif bread % 2 == 1 and pb < jelly and jelly >2:
# 	print "But you only have enough jelly to make {0} full {1} and one open face sandwich.\n".format(jelly-1, plural)
	
#peanut butter limiting
elif pb <= bread/2 and pb > 0: #more bread than pb
	if pb < jelly: #more pb than jelly
		print "But you only have enough peanut butter to make {0} {1}.\n".format(pb, plural)
	if jelly == 0 and bread != 0: #no jelly
		print "But you still can make {0} peanut butter {1}.\n".format(pb, plural)
	
	
elif pb >= bread/2 and jelly == 0 < pb : #more pb than bread and no jelly
	if bread % 2 ==1: #odd slice of bread
		print "But you still can make {0} peanut butter {1} and one open face peanut butter sandwich.\n".format(bread/2, plural)
	if 0 != bread % 2 != 1: #not odd, non zero
		print "But you still can make {0} peanut butter {1}.\n".format(bread/2, plural)
		
#peanut butter and jelly limiting
elif bread % 2 == 1 and pb < jelly and pb >2:
	print "But you only have enough peanut butter to make {0} full {1} and one open face sandwich.\n".format(pb-1, plural)
	
elif jelly <= bread/2 and pb == jelly>0:
	print "But you only have enough peanut butter and jelly to make {0} {1}.\n".format(jelly, plural)
	
	
#shopping list
if bread<=1 or jelly<=1 or pb<=1:
	print "You need to go to the store for more:"
	if bread <=1 :
		print "bread"
	if jelly <=1:
		print "jelly"
	if pb <=1:
			print "peanut butter"
	print "\n"
