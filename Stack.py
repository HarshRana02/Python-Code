stack = []

def push():
    if len(stack) == n:
        print("Stack is full")
    else:
        element = input("Enter the element : ")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print("Stack is empty")

    else:
        e = stack.pop()
        print("Removed element : ", e)
        print(stack)

n = int(input("Enter the limit of stack : "))
while True:
    print("Select the operations : 1. Push 2. Pop 3. Quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else: print("Choose correct options")