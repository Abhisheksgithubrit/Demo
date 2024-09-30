#1)List
#It is mutable

my_list = [1,2,3, "apple","banana",3]
print(my_list)
print(type(my_list))

#2)Tuples
#It isimmutable
my_tuple = [1,2,3, "apple","banana"]
print(my_tuple)
print(type(my_tuple))

#concatenation of tuples
my_tuple1 = [1,2,3,"apple","banana",3]
my_tuple2 = [4,5,6,"guava","orange"]
result = my_tuple1 + my_tuple2 #concatenation 
print(result)

#3) Dictionaries
#It is mutable
#Is is stored as a key value pairs
#It is unordered

my_dict = {"name":"Abhi","age":50,"city":"lxr"}
print(my_dict["name"]) #accessing values

my_dict["email"] = "abhialavandi@gmail.com" #Adding/updating values
print(my_dict)
my_dict.pop("age") #Removing item
print(my_dict)

4) sets
It is unordered 
It is mutable
example
step 1 create a list of students
students = ["Abhi","ganesh","Pavan"]

#step 2 create a dictionary eith the students names & the key values are their scores are values
scores = {"Abhi" : 80,"ganesh":79, "Pavan" :90}
#step 3 Add a new student & their score to the dictionary
scores ["harish"] = 90
#step 4 print the updated 
print(students)
print(scores)



