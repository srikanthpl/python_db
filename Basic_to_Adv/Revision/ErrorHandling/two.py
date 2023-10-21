class Demo:
    a=10

try:
    obj=Demo()
    obj.b
except:
    print("Accessed Member is not a part")
    