
# BRR
# MSAW

name = input("Please enter your name: ")
number = input("Please enter a number: ")

# TODO: Make sure the number is an integer
num=int(number)


# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print("Hey {}, \nYour number is: {} ".format(name, num))


# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************
fizz_num=num % 3==0
buzz_num=num % 5==0

if fizz_num and buzz_num:
	print("is a FizzBuzz number")
elif fizz_num:
	print("is a Fizz number")
elif buzz_num:
	print("is a Buzz number")

else:
	print('is a neither a fizzy or buzzy number')



# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.


# Using the variables, check the condition of the value, and print the necessary
# string
