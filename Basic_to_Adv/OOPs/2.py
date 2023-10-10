
class CA():
    #static variable
    min_bal  = 500
    def __init__(self,no,name,amount):
        self.Eno=no
        self.Ename=name
        self.Eamount=amount

    def get_min_Bal(self):
        return self.min_bal

    def deposit_amount(self,amount):
        self.Eamount = self.Eamount + amount
        
        print("Amount Deposited Successfully!")
        
        print("Deposited Amount :", amount )

    def cal_bal(self):
        return self.Eamount - self.min_bal
    
    
a3=CA(101,"Raju",5000)
a3.deposit_amount(1500)
print(a3.cal_bal())