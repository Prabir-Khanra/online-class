import datetime



'''
 What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''





# datetime to work with dates as date object
x = datetime.datetime.now()  #returns current date 
print(x.year)
print(x.strftime("%A")) # Saturday
print(x.strftime("%a")) # Sat
print(x)






# ================= year month day
y = datetime.datetime(2022,3,12)
print(y)






# ================== year month day  hour  minute second
z = datetime.datetime(2022,3,12,20,35,12)
print(z)






# Remember
# "%A"   Weekday, full version =============== Saturday
# "%a"	 Weekday, short version      ========= Sat
# "%b"   Month name, short version =========== Sep
# "%B"   Month name, full version ============ September
# "%m"   Month as a number 01-12 ============= 09