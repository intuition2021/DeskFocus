from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:

    command = input("Please enter: 1 for meaning | 2 for synonym | 3 for antonym\n"
                    "To quit, enter 0\n")

    if command == '0':
        break
    elif command != '1' or command != '2' or command != '3':
        print("Invalid command")
        continue

    word = input("Please input word: \n")

    if command == '1':
        print(dictionary.meaning(word))
    elif command == '2':
        print(dictionary.synonym(word))
    elif command == '3':
        print(dictionary.antonym(word))


