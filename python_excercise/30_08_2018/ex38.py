ten_things = "Apples Orages Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that.\n"

# The split() method returns a list of strings after brea
stuff = ten_things.split()
print stuff

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) <> 10:
    next_one = more_stuff.pop()
# The pop() method takes single argument (index) and removes the element present at that index from the list.
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." %len(next_one)
    
print "There we go: ", stuff

print stuff[1]
print stuff[-1]

# The pop() method takes single argument (index) and removes the element present at that index from the list.
print stuff.pop()

# The join() method is string method that returns a string in which the elements of sequence have been joined by string seperator.
print ' '.join(stuff)
print "#".join(stuff[1:5])
