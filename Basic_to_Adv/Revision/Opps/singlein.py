# Single inheritance
# the base class inherting the properties and methods from baseclass is called single inhertance

class BaseClass:
    a=10
    b=100
    def display(self):
        print("displaying")
class Derivedclass(BaseClass):
    c=100
    d=200
    def show(show):
        print("showing..")
        
        
""" obj=BaseClass()
obj2=Derivedclass()
print(obj.a,obj.b)
obj.display() """
obj2=Derivedclass()
print(obj2.a,obj2.b,obj2.c,obj2.d)
obj2.show()
obj2.display()
