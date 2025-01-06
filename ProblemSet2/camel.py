UserInput = input("CamelCase:")
print("snakecase:",end = "")
for letter in UserInput:
    if letter.isupper():
        print("_"+ letter.lower(),end = "")
    else:
        print(letter,end="")

print()


