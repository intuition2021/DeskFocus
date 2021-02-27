from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:

    command = input("Please enter: 1 for meaning | 2 for synonym | 3 for antonym\n"
                    "To quit, enter 0\n")

    if command == '0':
        break

    if command == '1':
        word = input("Please input word: \n")
        print(dictionary.meaning(word))
    elif command == '2':
        word = input("Please input word: \n")
        print(dictionary.synonym(word))
    elif command == '3':
        word = input("Please input word: \n")
        print(dictionary.antonym(word))
    else:
        print("Invalid command\n")
        continue


