# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# ===================== parent class / base class ===========
# ===========================================================
class OldCar:
    def __init__(self,wheel,category):
        self.car_wheel = wheel 
        self.category = category
        
    def my_fun(self):
        print(self.category)


# ===================== child class / derived class =========
# ===========================================================
class RacingCar(OldCar): #RacingCar inherits the properties and methods from the Person class:
    # ========== inherited properties and functions ==========================================
    # car_wheel
    # category
    # def my_fun(self):
    #    print(self.category)
    #=========================================================================================
    def __init__(self,wheel_number,car_category,milage):
        self.car_wheel = wheel_number
        self.category = car_category
        self.car_milage = milage
        
    def speed(self):
        print("No speed yet")
        
r = RacingCar(4,"SUV",16)
r.my_fun()
r.speed()

# =======We can create many objects of same class ============================================
# ============================================================================================
# d = RacingCar(4,"Racing Car",14)
# d.my_fun()
# d.speed()
    
        
