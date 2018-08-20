def add(a, b):
    print "Adding %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" %(a, b)
    return a - b

def multiply(c, d):
    print "Multiply %d * %d" %(c, d)
    return c * d

def divide(c, d):
    print "Divide %d / %d" %(c, d)
    return c / d

print "Let's do some math with just functions!"

age = add(30, 6)
height = subtract(150, 10)
weight = multiply(31, 2)
iq = divide(100.0, 1.5)

print "age: %d, height: %d, weight: %d, iq: %d" %(age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That's becomes: ", what, "What can you do it by hand?"
