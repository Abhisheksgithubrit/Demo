#reads data from a file & process it 
file = open("data.txt","r")
total = 0

for line in file:
    total += int(line .strip()) #converts each line to an integer & add to total

#we want the total sum while closing the file to release the memory
file.close()
print("The sum of the numbers is:",total)