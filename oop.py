##1 task
# class Employee:
#     __salary = 50000

#     def increament(self):
#         self.__salary += 5000
#         print("Salary after increament:", self.__salary)
    
#     def deduct(self):
#         if self.__salary > 5000:
#             self.__salary -= 5000
#             print("Salary after deduction:", self.__salary)

#     def get_salary (self):
#         print("current salary:", self.__salary)

# e = Employee()
# e.get_salary()
# e.increament()
# e.deduct()  




##3 problem
# class Father:
#     def property(self):
#         print("father owns this property")

#     def business(self):
#         print("father has a business")

# class Son(Father):
#     def Study(self):
#         print("Son studies well")

# class Daughter(Father):
#     def Dance(self):
#         print("daughter dances well")

# class GrandChild(Son,Daughter):
#     def gaming(self):
#         print("both of the child plays games")

# g = GrandChild()
# g.property()
# g.business()
# g.Study()
# g.Dance()
# g.gaming()






##2 task

# from abc import ABC, abstractmethod

# # Abstract Class
# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

#     @abstractmethod
#     def fuel_type(self):
#         pass


# # Child Class - Car
# class Car(Vehicle):

#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")

#     def fuel_type(self):
#         print("Petrol")


# # Child Class - Bike
# class Bike(Vehicle):

#     def start(self):
#         print("Bike started")

#     def stop(self):
#         print("Bike stopped")

#     def fuel_type(self):
#         print("Petrol")


# # Child Class - Tesla
# class Tesla(Vehicle):

#     def start(self):
#         print("Tesla started")

#     def stop(self):
#         print("Tesla stopped")

#     def fuel_type(self):
#         print("Electric")


# # Create Objects
# car = Car()
# bike = Bike()
# tesla = Tesla()

# # Call Methods
# car.start()
# car.stop()
# car.fuel_type()

# print()

# bike.start()
# bike.stop()
# bike.fuel_type()

# print()

# tesla.start()
# tesla.stop()
# tesla.fuel_type()