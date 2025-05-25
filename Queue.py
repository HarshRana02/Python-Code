queue = []

def enqueue():
    element = input("Enter the element : ")
    queue.append(element)

def dequeue():
    if not queue:
        print("Queue is empty")

    else:
        e = queue.pop(0)
        print("Removed element : ", e)
        print(queue)

def display():
        print(queue)

while True:
    print("Select the operations : 1. Add 2. Remove 3. Show 4. Quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else: print("Choose correct options")