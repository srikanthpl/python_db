stack=[]
def push():
    if len(stack)==n:
        print("Stack is Full")
    else:
        element=(input("Enter the Element:"))
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("STack is Empty!")
    else:
        e=stack.pop()
        print("Removed Element:",e)
        print(stack)
n=int(input("Enter the Limit:"))
while True:
    print("Select The Operation \n 1.Push \n 2.Pop \n 3.Quit")
    choice=int(input("Enter the number:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("***Enter the Correct Operatipon!***")    