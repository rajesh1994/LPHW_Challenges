#-*-coding:utf-8-*-
# Declaring variables like name, age, height, weight, eye color, teeth color and hair color.
my_name = "Rajesh Suryaprakash"
my_age = 24.7
my_height = 150 # Height in cm
my_weight = 65 # Weight in kg
eye_color = "White & Blue"
my_teeth = "White"
my_hair = "Black"

# Printing name, height, weight, age, eye color, teeth color, hair color using printf string formating.
print "Let's talk about %s." %my_name
print "He's %d centimeter tall." %my_height
print "He's %F years old." %my_age
print "He's %d kilo gram heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eye_color,my_teeth)
print "His teeth are usually %s depending on the coffee." %my_teeth

# Performing addition operation with age, weight, height variables using printf string formating
print "If I add %d, %d and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
