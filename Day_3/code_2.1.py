# # # fruits = ["apple","banana","Guava"]

# # # for fruit in fruits:
# # #     print(fruit)

# # count = 1

# # while count <=100:
# #     print(count)
# #     count += 1

# #-------------------------------------------------------

# numbers = [1,2,3,4,5,6]

# for number in numbers :
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")

# -----------------------------------------------
# Get user input
number = int(input("Enter a number:"))

#check the number is positive or negative or zero
if number > 0:
    print(f"{number}positive,")
elif number < 0:
    print(f"{number} negative,")
else:
    print("The number is zero")