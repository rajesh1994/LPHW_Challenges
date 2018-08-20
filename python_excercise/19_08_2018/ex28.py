b1 = True and True
print 'Expected result is "True".'
print "Actual result is %r.\n" %b1

b2 = False and False
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b2

b3 = 1 == 1 and 2 == 2
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b3

b4 = "test" == "test"
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b4

b5 = 1 == 1 or 2 != 1
print 'Expected result is "True".'
print 'Actual result is %r\n' %b5

b6 = True and 1 == 1
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b6

b7 = False and 0 != 0
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b7

b8 = True or 1 == 1
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b8

b9 = "test" == "testing"
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b9

b10 = 1 != 0 and 2 == 1
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b10

b11 = "test" <> "testing"
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b11

b12 = "test" == 1
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b12

b13 = not (True and False)
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b13

b14 = not (1 == 1 and 0 <> 1)
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b14

b15 = not (10 == 1 or 1000 == 1000)
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b15

b16 = not (1 != 10 or 3 == 4)
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b16

b17 = not ("testing"  == "testing" and "Ezio" == "Cool Guy")
print 'Expected result is "True".'
print 'Actual result is %r.\n' %b17

b18 = 1 == 1 and not ("testing" == 1 or 1 == 0)
print 'Expected result is "True".'

b19 = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b19

b20 = 3 == 3 and not ("testing" == "testing" or "python" == "Fun")
print 'Expected result is "False".'
print 'Actual result is %r.\n' %b20
