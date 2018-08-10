#-*-coding:utf-8-*-
from sys import argv
from os.path import exists

script, file_from, file_to = argv

print "Copying from %s to %s." %(file_from, file_to)

in_file = open(file_from)
indata = in_file.read()

#We could do these on one line too, how?

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist %r" %exists(file_to)
print "Ready, to hit RETURN to continue, CTRL+C to abort."

raw_input()

out_file = open(file_to, "w")
out_file.write(indata)

print "Alright, All done."

out_file.close()
in_file.close()
