string = input("Enter a string: ")
dictionary = dict()

for char in string:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

for char in dictionary:
    print(f"{char} - {dictionary[char]}")
