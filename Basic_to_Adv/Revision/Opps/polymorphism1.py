#run-time(Method overriding)#to overriding parent class method using 
#child class "With the help of same method name and parameter"

class Parent:
    def transport(self):
        print("Cycle")
class Child(Parent):  # child inherits the parent class
    def transport(Self):
        print("Bike")   #same functionality we used it's overided
    
c=Child()
d=Parent()
d.transport()
c.transport()


