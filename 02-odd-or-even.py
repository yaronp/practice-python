import operator

number = raw_input("Enter Number: ")

if not number.isdigit():
    print "This is not a valid number"
elif operator.mod(int(number), 2) is 0:
    if operator.mod(int(number), 4) is 0:
        print "This is an even number (4)"
    else:
        print "This is an even number"
else:
    print "This is odd number"
