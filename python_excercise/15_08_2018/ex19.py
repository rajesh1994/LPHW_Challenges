def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crakers
    print "Man that's enough for the party!"
    print "Get a blanket.\n"

print "We can just give the funtions numbers directly:"
cheese_and_crackers(30, 50)

print "Or, we use varibles from our script:"
amount_of_cheese = 18
amount_of_crackers = 34

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside too:"
cheese_and_crackers(22+11, 39+41)

print "We can combine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 30)
