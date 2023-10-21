# MultiLevel inheritance
# One class inherits from base class and the base class inherits from derived class 


class BaseClass:
    a=10
    b=100
    def display(self):
        print("displaying")
        
class BaseClass2(BaseClass):
    name="Sri"
    def Employee(self):
        print("Employee Name is:",self.name)
class Derivedclass(BaseClass2):
    c=100
    d=200
    def show(show):
        print("showing..")

        
        

obj2=Derivedclass()
print(obj2.a,obj2.b,obj2.c,obj2.d)
obj2.Employee()
obj2.show()
obj2.display()
