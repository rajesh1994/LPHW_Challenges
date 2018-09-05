# Create a mapping of state to abbrevation
print "-" * 145
states = {  'Oregon' : 'OR',
            'Florida' : 'FL',
            'California' : 'CA',
            'New York'  : 'NY',
            'Michigan' : 'MI'
            }
print states, "\n"

# Create a basic set of states and some cities in them

cities = {  'CA' : 'San Francisco',
            'MI' : 'Detroit',
            'FL' : 'Jacksonville'
            }
print cities

# Add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities

print '-' * 145
print "NY State has: ", cities['NY'], "\n"
print "OR State has: ", cities['OR']
print '-' * 145

# print some states
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
print '-' * 145

# Do it by using the state then cities dict

print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
print '-' * 145

# Print every state abbreviation

for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abbrev)
print "-" * 145

# Print every city abbreviation

for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)
print "-" * 145

# Now do both at the same time

for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])
print "-" * 145

# Safely get an abbreviation by state that might not be there

state = states.get("Texas", None)
if not state:
    print "Sorry, no Texas"
print "-" * 145

# Get city with a default value

city = cities.get("TX", "Does Not Exist")
print "The city for the state 'TX' is %s:" %city
print "-" * 145
