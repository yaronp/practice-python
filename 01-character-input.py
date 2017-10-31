import datetime

name = raw_input("Give me your name: ")
print "Your name is " + name

age = int(raw_input("Give me your age: "))
print "Your age is " + name

print "You will be 100 in:" + str(datetime.datetime.now().year + (100-age))