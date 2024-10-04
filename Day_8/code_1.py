import math

#Using the sort() function from the math module 
result = math.sqrt(16)
print(result)
#-----------------------------------------------------------------
#Question: 

#Write a simple prgm that calculates the square root of a number 
#prints the current date & Time 
#And displays the current working directory

import math
import datetime
import os


#calculate the square root of 30.
sqrt_value = math.sqrt(10)
print("Square root of 30: (sqrt_value)")

#Get the current date and time
current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")

#Displays the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")