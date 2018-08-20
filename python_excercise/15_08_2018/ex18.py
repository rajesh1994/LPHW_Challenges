#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#Ok, that time *args is actually pointless, we just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#This just takes one argument
def print_one(arg1):
    print "arg1: %r" %arg1

#This one takes no arguments
def print_none():
    print "I got nothing!"

print_two("Bharathi", "Prakash")
print_two_again("Bharathi", "Prakash")
print_one("Bharathi")
print_none()
