 #compile -time(" Method Overloading")python not allows directly 
 #overloading with the help of default args it's possible

class Demo:
    def add(self,a,b=100,c=100):
        print(a+b+c)
        
obj=Demo()
obj.add(200)
obj.add(200,100)
obj.add(200,200,200)
        
