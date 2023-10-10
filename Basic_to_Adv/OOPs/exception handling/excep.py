def divide(x,y):
    return x/y
def calculate(a,b):
    try:
        result=divide(a,b)
        print("Result:",result)
    except:
        print("You Can't divide number by zero" )
calculate(10,0)