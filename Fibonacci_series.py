def fibonacci(num):

    a, b = 0, 1

    if num < 1: print(num)

    elif num == 1: print(a)

    elif num == 2: 
        print(a) 
        print(b)

    elif num > 2:
        print(a)
        print(b)

        for _ in range (num - 2):
            c = a+b
            a, b = b, c
            print(c)

num = int(input("Enter a number : "))
fibonacci(num)