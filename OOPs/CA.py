from Account import * 

class  CA(Account):
    
    #static variable 
    min_bal = 5000
    def __init__(self,aid,name,amount):
        super().__init__(aid,name)
        self.acc_amount = amount
        print("Customer Id:",aid)
        print("Customer Name:",name)
    def get_min_Bal(self):
        return self.min_bal 
    
    def deposit_amount(self,amount):
        self.acc_amount = self.acc_amount + amount 
        print("Deposited Successfully rupees:",amount)
        print("THE Account Balance is:",self.acc_amount)
    def withdrawl(self,amount):
        print(self.acc_amount - amount)
        print("The Withdrwaled Amount is:",amount)
        print("The BAlance Amount in your bank is :",self.acc_amount-amount)
        



a2=CA(102,'sonia',70000)
# a2.deposit_amount(60)
# print(a2.cal_bal())
a2.withdrawl(5000)
