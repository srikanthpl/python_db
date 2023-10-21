class Demo:
    __a=10
    b=20
    # __def Display(self):  method too contact access  
    def Display(self):
        print(self.__a)    
        print("Hello")
        
obj=Demo()
# print(obj.__a)  #outsie the class can't access
print(obj.b)
obj.Display()