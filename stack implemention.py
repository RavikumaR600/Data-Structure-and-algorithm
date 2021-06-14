stack=[]
def push():
    element=input("enter the element: ")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty! ")
    else:
        e=stack.pop()
        print("removed elment :",e)
        print(stack)
while True:
    print('''select the operations:
    1.push
    2.pop
    3.Quit ''')
    choice= int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter the correct")
