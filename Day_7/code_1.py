#Defining a class
class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def start(self):
        print(f"The {self.color} {self.model} is starting,")

#creating a object
my_Car = Car("Red","Honda civic")
my_Car.start()

#---------------------------------------------------------------------

class BankAccount:
    def __init__(self,balance) :
        self._balance = balance #private variable 
    
    def deposit(self,amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

#creating a object 
account = BankAccount (2000)
account.deposit(300)
print(account.get_balance()) 

#This code demonstrates object-oriented programmming concepts like:
#class,objects,


#------------------------------------------------------------------

#Iparent class 
class Animal:
    def speak(self):
        print("Animal is making a sound")

#child class 
class Dog(Animal):
    def speak(self):
        print("Dog is barking")

#creating an object of the child class
my_dog = Dog()
my_dog.speak()

#-------------------------------------------------------------

#Polymorphism 

class Bird:
    def fly(self):
        print("Bird id flying")

class Airplane:
    def fly(self):
        print("Airplane is flying,")

#Polymorphism in action
def make_it_fly (flying_object):
    flying_object.fly()

#creating objects
sparrow = Bird()
boeing = Airplane()

make_it_fly(sparrow)
make_it_fly(boeing)
        