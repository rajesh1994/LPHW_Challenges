# Declaring cars, space_in_a_car, drivers & passengers
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# Calculating number of cars not driven
cars_not_driven = cars - drivers

# Calculating number of cars driven
cars_driven = drivers

# Calculating carpool capacity
carpool_capacity = space_in_a_car * cars_driven

# Calculating average passengers per car 
average_passengers_per_car = passengers / cars_driven

# Printing number of cars available
print "There are", cars, "available."

# Printing number of drivers availabe
print "There are", drivers, "available."

# Printing number of cars not driven
print "There will be", cars_not_driven, "empty cars today."

# Printing today's carpool capacity
print "We can transport", carpool_capacity, "people today."

# Printing today's number of travelled passengers
print "We have", passengers, "to carpool today."

# Printing today's carpool capacity
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"
