
#class contains variables and methods
class Account:    
    def open_account(self):
        print("Acoount opened Successfully")
    def deposit_amount(self):
        print("Amount Deposited")
    def get_bal(self):
        print("Displayed Balance")
    def withdrawl(self):
        print("Amount Withdrawled")
        
Customer=Account()
print(Customer)
print(Customer)
print(Customer.__dict__)
        
        