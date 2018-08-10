txt1 = open("ex15.2.txt", "a")
txt1.write("Now the file has one more line!.")

txt1 = open("ex15.2.txt", "r")

print txt1.read()
