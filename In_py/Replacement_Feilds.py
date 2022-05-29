age = 24
print("\n")
print("My age is " + str(age)) # Normal concatination
print("My age is {0}".format(age)) # Using replacement feilds

# Why do this ?
# Well consider this.

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}. My age is {8}"
.format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec", age))
# python does all the concatination automatically you can also manipulate the 
# the order the concatination happens like so bellow.

print("My name is {3}, sounds like {3}. Age {0} so i was born {1} and lived to be {2}"
    .format(24, 1990, "an immortal", "BOB")) 
    # The arguments in format can be taken as .format(0,1,2,3) like an index
    # Thus python replaces them to the coresponding numbers in the print function text
print("\n")# blank line

# We can also format the the printing function so that it appears better
for i in range(1, 13):
    print("No.{0:2} square is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
# left alignment
print("\nLeft alignment")
for i in range(1, 13):
    print("No.{0:<2} square is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))
# Center alignment
print("\nCenter alignment")
for i in range(1, 13):
    print("No.{0:^2} square is {1:^4} and cubed is {2:^4}".format(i, i**2, i**3))
print("\n\n\n")

# precision, you can also set the precision of the printed text 
print('Pi is approximately {0:12}'.format(22/7)) # Normal
print('Pi is approximately {0:12f}'.format(22/7)) # Normal + 'f' format that will defualt to decimal up to 6 position
print('Pi is approximately {0:12.50f}'.format(22/7)) # Normal + specified precision of 50 decimal point, precision superseeds the 12 space allocated to it
print('Pi is approximately {0:52.50f}'.format(22/7)) #  Normal with enough space for precision
print('Pi is approximately {0:62.50f}'.format(22/7))
print('Pi is approximately {0:72.50f}'.format(22/7))
print('Pi is approximately {0:<72.50f}'.format(22/7))
