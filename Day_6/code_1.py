file = open("example.txt","r") #reads the entire content of the file as a single string
for line in file: 
    print(line)
file.close()
#--------------------------------------------------------

file = open("example1.txt","w") #overwrite 
file.write("welcome to the python with sathya!")
file.close()
#------------------------------------------------------------

file = open("example1.txt","a") #appending a line in existing file
file.write("\n welcome to the python sesssion with sathya and chandu")
file.close()

#------------------------------------------------------------

