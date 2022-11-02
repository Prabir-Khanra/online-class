# Creating List
#         0        1       2          3    ====================> index no of item in list
name = ['Gourav','Ankit','Monalisa','Koyel'] # contains 4 items
list2 = ["abc", 34, True, 40, "male"] # contains 5 items
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9] # contains 9 items
list3 = [True, False, False,True,True] # contains 5 items
print(name)





# ====== accessing list item 
x = name[1] # accessing seecond item from name list 
print(x)





# ====== update or change list item 
name[1] = "Hrittik Roshan"  # change second item from name list 
print(name)





# ====== add list item 
#                  0               1              2             3
super_star = ["Katrina Kaif","Disha Patani","Pooja Hegde","Kriti Sanon"]
super_star.append("Sradhya Kapoor") # item will be added in the last position
#super_star.insert(1,"Urvashi Rautela") # item will be added in the second position
print(super_star)





# ====== remove list item 
#                  0               1              2             3
super_star = ["Katrina Kaif","Disha Patani","Pooja Hegde","Kriti Sanon"]
super_star.remove("Disha Patani")
# super_star.pop(2) # Removing third item 
# super_star.pop() # Removing last item 
print(super_star)





# ====== add two lists
heros = ["Shahrukh Khan","Akshay Kumar","Hrittik Roshan"]
heroines = ["Katrina Kaif","Disha Patani","Pooja Hegde","Kriti Sanon"]
heros.extend(heroines) # here we added heroines list to heros list
print(heros)
# list2 = heros + heroines
# print(list2)

