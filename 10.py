word = input("Enter a string word: ")
n = int(input("Enter a number: "))
if word == "good" and 7 <= n <= 15:
    print("It's good")
elif word == "bad" and n < 7 or n > 15:
    print("It's bad")