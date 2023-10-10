class Account:
    def __init__(self):         
        print("This is an Constructor Method")
    def get_bal(self):
        print("This is an instance Method")
    @classmethod
    def set_branch(cls):
        print("This is an Class Method")
    @staticmethod
    def something():
        print("Static Method")
        
Customer=Account()
Customer.get_bal()
Customer.set_branch()
Customer.something()

        