# Hiding The implemention showing essential part
#to perform abstraction to import abc module it contain(ABC class)
#We can't create object for Abstract class
 
from abc import *

class AbstractDemo(ABC):
    @abstractmethod
    def HousingIntrest(self):
        None
    @abstractmethod
    def VehicleIntrest(self):
        None
  
class SBI(AbstractDemo):
    def HousingIntrest(self):
        print("House Intrest")
    # def VehicleIntrest(self):
    #     print("Vehicle Intrest")
    # def Loan(self):
    #     print("Loan")

class NewSbi(AbstractDemo):
    def HousingIntrest(self):
        print("New House Intrest")
    def VehicleIntrest(self):
        print("NewVehicle Intrest")


obj1=SBI()
obj1.HousingIntrest()
obj=NewSbi()
obj.HousingIntrest()
obj.VehicleIntrest()
