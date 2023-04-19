def isPrime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True


x = int(input("Enter an integer: "))
result = isPrime(x)
print(f"{x} is{'' if isPrime(x) else ' not'} prime")
