# enter a 3 digit number and print all prime factors.
n = int(input("Enter a 3 digit number: "))

i = 2

while n > 1:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i = i + 1