class Person:
    def showName(self):
        print("Hrittik Roshan")
        
class Student:
    x = "Prabir" # property
    y = "Proloy" # property
    
    def fun(self): # method / function
        print("Hello Programmer")
        
# We can access all the properties and functions through objects of this specific class         
s = Student() #s is a object of Student class 
a = Student() #a is a object of Student class 
b = Student() #b is a object of Student class
c = Student() #c is a object of Student class
d = Student() #d is a object of Student class
print(s.x) # Prabir 
s.fun() # Hello Programmer 
