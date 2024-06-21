def prime(number):

    if number < 2:
        return False
    
    for i in range (2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        
    return True

number = int(input("Enter the number : "))

if prime(number):
    print(f"{number} is prime number")

else:
    print(f"{number} is not a prime number")

    