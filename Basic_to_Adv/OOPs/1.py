class Baseclass:
    a=10
    b=20
    def display(self):
        print("base class")
        
class Derivedclass(Baseclass):
    c=10
    d=50
    def show(self):
        print("derive class")
        

obj1=Derivedclass()
obj1.display()
obj1.show()

    