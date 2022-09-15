# type casting


# first
a = '345.6' # string => float => int
b = float(a) # converted to float value....answere is 345.6
c = int(b) # converted to int value....answere is 345
print(type(b))
print(type(c))
print(b)
print(c)



#second
p = '34' # string => int
q = int(p) #  # converted to int value....answere is 34
r = float(q) # converted to float value....answere is 34.0
print(type(q))
print(type(r))
print(q)
print(r)



#third
s = 34 #int => string
t = str(s) # converted to string value....answere is '34'
u = float(s) # converted to float value....answere is 34.0
print(type(t))
print(type(u))
print(t)
print(u)



#fourth
v = 34.0 # float => int  
w = int(v) # converted to float value....answere is 34
x = str(v) # converted to string value....answere is '34.0'
print(type(w))
print(type(x))
print(w)
print(x)




#five
# error ==================== error ==================== error ===================
k = 'Ranvir Kapoor' # string => int
l = int(k) # converted to float value ....... error...we cant convert a text value into an int value
m = float(k) # converted to float value ....... error...we cant convert a text value into an float value
print(type(l))
print(type(m))
# ==============================================================================


