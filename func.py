#in python, function is defined using def

# ============================================================================================
# first ======================================================================================
#creating a funciton
def myName () :
    print("Hello Programmer")
# call a funciton
myName()







# ============================================================================================
# second =====================================================================================
def myAddress (x): # Here 'x' is a parameter
    print("My address: "+x)

myAddress("Tamluk") # Here 'Tamluk is an argument'







# ============================================================================================
# third ======================================================================================
# This function expects 2 arguments, but gets only 1
def showSomething(name,age):
    print("Show something")

showSomething("Prabir")
# error ===================







# ============================================================================================
# fourth ======================================================================================
# if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def showSomething(name,age):
    print("Show something")

showSomething("Prabir",25)







# ============================================================================================
# fifth ======================================================================================
# if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myProffession ():
    print("I am a Mobile Application Developer")

def myHobby ():
    pass

myProffession()
myHobby()




