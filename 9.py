# use len()
text = input("Enter a string: ")
print('X' * len(text))
# not use len()
text = input("Enter a string: ")
result = ""
for i in text:
    result += "X"
print(result)