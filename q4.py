# wap to enter a string and print it in reverse also print the noof vowelsand consonart in it.
s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Reverse:", s[::-1])
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)