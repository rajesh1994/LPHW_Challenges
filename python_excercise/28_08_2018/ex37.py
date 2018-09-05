#-*-coding:utf-8-*-
# del[a : b] - This method deletes all the elements in the range starting from index "a" till "b" mentioned in arguments.

# Python code to demonstrate the working of del and pop().

# Initializing the list

l1 = [3, 2, 1, 7, 9, 10, 33, 20, 02, 16, 22, 39]

print "List's actual length: ", len(l1)
print "Actual list: ", l1
# Using the del to delete the elements from position 4 to 8
# Deletes 9, 10, 33, 20, 100
del l1[4 : 8]

print "Elements deleted list's length: ", len(l1)
print "Modified list: ", l1


# "and" keyword gives the result "TRUE" if both the operands are "TRUE".

a1, b1, c1, d1 = 10, 28, 32, 10

#a1 = 10
#b1 = 28
#c1 = 32
#d1 = 10

if a1 == d1 and b1 == c1:
    print "The given statement is true."
else:
    print "The given statement is false."
    
# from…import is used to import specific attributes or functions into the current namespace

from math import cos
a = cos(1)
print "The value of cos(1) is ", a

# not operator is used to invert the given value(TRUE, FALSE)
t1 = t2 = 10
#t2 = 10

if not t1 == t2:
    print "The given value is TRUE"
else:
    print "The given value is FALSE"
    
# The statement inside a "While loop" continue to execute until the condition for while loop evaluates to "False or Break" statement is encountered.
i = 5
while(i):
    i = i - 1
    print (i)

# "as" is used to create an alias while importing a module. It means giving a diffrent name to a module while importing it.

# As for example, Python has a standard module called math. Suppose we want to calculate what cosine pi is using an alias. We can do it as follows using as:

import math as m1
a = m1.cos(m1.pi)

print a

# if, elif, else are used for conditional branching or decision making.

def if_example(a):
    if a == 1:
        print "One"
    elif a == 2:
        print "Two"
    else:
        print "Something else"
if_example(7)
if_example(1)
if_example(2)


