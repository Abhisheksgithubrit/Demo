# # #writing a program that only accepts positive numbers.
# # #You can raise an exception if the user enters a negative number.

# # def check_positive(number):
# #     if number < 0:
# #         raise ValueError("Negative numbers are not allowed!")

# # try:
# #     print(check_positive(5))
# # except ValueError as e:
# #     print(e)

# # #--------------------------------------------------------------



# #using try except block

# try :
#     result = 10/0
# except ZeroDivisionError:
#     print("oops! you cant divide by zero,")

# #finally-clause

# try:
#     file = open("example.txt","r")
#     #some kind of code to raise an exception 

# except FileNotFoundError:
#     print("File not found")

# finally:
#     file.close() 
#     print("file closed")

# #write a program that accepts 


try:
    num1 = float(input("Enter the 1st number:"))
    num2 = float(input("Enter the 2nd number:"))
    result = num1/num2
    print(f"The result is:{result}")

except ZeroDivisionError:
  print("Error:You cannot divide by zero")

except ValueError:
  print("Error : please Enter valid numbers,")

finally:
  print("program execution completed.")
