name = "Akshay Kumar"
status = "I like Hrittik"


# len() - returns legth of a string =================================================================
x = len(name)
y = len(status)
print(x)
print(y)




# =====================================================================================================
# =====================================================================================================
#checking if a certain phrase or character is present in a string
# in ========
a = "like" in status # True
b = "likes" in status # False
c = "ke Hr" in status # True
#not in =====
d = "like" not in status # False
e = "likes" not in status # True
f = "ke Hr" not in status # False 





# ex: 1 ===========================================================================================
if "like" not in status : #False
    print("AND")
else:
    print("I am in else part")

# ans: I am in else part




# ex: 2 ===========================================================================
if "like" in status : #True
    print("AND")
else:
    print("I am in else part")

# ans: AND





# ====================================================================================================
# =============================================================================================================
if x > 10 : #True
    print("AND")
else:
    print("I am in else part")

# ans: AND