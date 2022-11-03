#All classes have a function called __init__(), which is always executed when the class is being initiated.

#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

#The self parameter is a reference to the current instance of the class, and is used to access variables and invoke functions that belong to the class.


class Student:
    # my_name = "Hrittik"
    def __init__(self,name,title,age):
        self.my_name = name 
        self.my_title = title
        self.my_age = age 
        
    def showName(self):
        print(self.my_name,self.my_title,self.my_age)
        
        
s = Student("Hrittik","Roshan",46)
s.my_age = 50
s.showName()

# =======We can create many objects of same class =================
# =================================================================
#p = Student("Shahrukh","Khan",54)
#p.my_age = 60
#p.showName()


# =======We can create many objects of same class =================
# =================================================================
#d = Student("Deepika","Padukon",36)
#d.my_age = 40
#d.showName()
        