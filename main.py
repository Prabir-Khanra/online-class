# ===== A module is same as a code library. ============
# ======================================================



# ========================================
import my_module  # =======> First process
my_module.myFun() 
print(my_module.person['location'])




# =============================================
import my_module as m # =======> Second process 
m.myFun()
print(m.person['location'])
print(m.person['name'])




#=======================================================
from my_module import person # ==========> Third process 
print(person['name'])


    
    










