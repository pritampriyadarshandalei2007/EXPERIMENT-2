# enter a word and check wheather it is a palindrome or not.
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")