class datahiding:
    __a=20
    def __display(self):
        print(datahiding.__a)
        print("hello ")
    def show(self):
        self.__display()
        
obj=datahiding()
obj.show()