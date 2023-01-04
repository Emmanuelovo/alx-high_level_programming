#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
grater_five = "and is greater than 5"
zero = "and is 0"
less_six = "and is less than 6 and not 0"
print("last digit of", end=" ")
if (number % 10 > 5):
	print("{} is {} {}".format(number, number %, grater_five))
elif (number % 10 == 0):
	print("{} is {} {}".format(number, number % 10, sero))
elif (number < 0):
	print("{} is -{} {}".format(number, (number * -1) % 10, less_six))
else:
	print("{} is {} {}".format(number, number % 10, less_six))
