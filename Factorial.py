def factorial(number):
    
    factorial = 1

    if number < 0: print("Invalid input")

    elif number == 0: print("0 factorial is 1")

    else:
        for i in range(1, number+1):
            factorial = factorial * i
        print(factorial)

number = int(input("Enter a number : "))
if factorial(number):
    print(f"The factorial of {number} is ")