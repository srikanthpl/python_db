class Employee:
    org_name="Wipro"
    def __init__(self,id,name):
        self.Eid=id
        self.Enmae=name
    def get_sal(self,sal):
        self.Esal=sal
        
E1=Employee(101,"sri")
E2=Employee(102,"Hari")
E1.get_sal(15000)
E2.get_sal(20000)
print(E1.org_name)
print(E1.__dict__)
print(E2.__dict__)
        
      