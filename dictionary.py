# ============ creating dictionary =======================================
# ========================================================================
person = {
    "name":"Hrittik Roshan", # name is the key and 'Hrittik Roshan' is its value 
    "age": 46,  # age is the key and '46' is its value 
    "proffession": "Actor" #  # proffession is the key and 'Actor' is its value 
}



# ============ accessing item ============================================
# ========================================================================
x = person["name"]
print(x)
#y = thisdict.get("name")
#print(y) # ======================print same result




# ============ add item ==================================================
# ========================================================================
person["height"] = 5.9 
print(person)




# ============ update/change item ============================================
# ============================================================================
person["age"] = 48 # age will be updated 46 to 48
print(person)




# ============ delete/remove item ============================================
# ============================================================================
person.pop("age") # ===> removes the item with specified key name 
print(person)