import pickle


class ToDoItem:
    def __init__(self, toDo, dueDate):
        self.toDo = toDo
        self.dueDate = dueDate

    def display(self):
        return (self.toDo + ", " " to be done by " + self.dueDate)

class MiniTasks:
    def __init__(self, miniTask):
        self.miniTask = miniTask
    def display(self):
        return (self.miniTask)


    def update(self, field, newValue):
        oldRecord = self.display()
        if field == 1:
            self.toDo = newValue
        elif field == 3:
            self.dueDate = newValue
        elif field == 1:
            self.miniTask = newValue
        newRecord = self.display()

        print("Updated:\n" + oldRecord + "\nto:\n" + newRecord)


def create(todolist, sidelist):
    newToDo = input("What do you need to do? ")
    newDueDate = input("When is the due date? ")
    newMiniTask = input("What are the tasks you need to do for this item?" )
    newToDoItem = ToDoItem(newToDo, newDueDate)
    todolist.append(newToDoItem)
    sidelist.append(newMiniTask)


def display(todolist, sidelist):
    print("Your to do list: ")
    for i in range(len(todolist)):
        print(str(i + 1) + ". " + todolist[i].display())
    print("Your side tasks:")
    for i in range(len(sidelist)):
        print(str(i + 1) + ". " + sidelist[i].display())


def update(todolist, sidelist):
    display(todolist, sidelist)
    errFlag = True
    while errFlag:
        try:
            position = int(input("Which item number do you want to update? "))
            errFlag = False
        except:
            print("Invalid item number")

    fieldToUpdate = promptUserForItem("""Which field do you want to update?
1. To do description
2. Due date
3. Mini Tasks
>>> """)
    newValue = input("What is the new value?")

    todolist[position - 1].update(fieldToUpdate, newValue)
    sidelist[position - 1].update(fieldToUpdate, newValue)


def promptUserForItem(promptMsg):
    errFlag = True
    while errFlag:
        try:
            itemSelected = int(input(promptMsg))
            errFlag = False
        except:
            print("Please enter a number")
    return itemSelected



def delete(todolist, sidelist):
    display(todolist)
    display(sidelist)
    try:
        position = int(input("Which item number do you want to delete? "))
        del todolist[position - 1]
        display(todolist)
        position2 = int(input("Which item number do you want to delete? "))
        del sidelist[position - 1]
        display(sidelist)
    except:
        print("Invalid item number")

def delete_all(todolist, sidelist):
    deleteques = input("Are you sure you would like to clear your whole to-do list?").lower()
    if deleteques == "yes":
        todolist.clear()
        sidelist.clear()
        print("Your list has been cleared!")
    else:
        print("Here's your todolist")
        display(todolist)
        display(sidelist)


try:
    myFile = open("todolist2.pickle", "rb")
    myList = pickle.load(myFile)
    sideList = pickle.load(myFile)
    myFile.close()
except:
    myList = []
    sideList = []
command = ""
while command != "F":
    command = input("""What would you like to do
                    C - create new item
                    V - view to do list
                    U - update the to do item
                    D - delete existing item
                    E - clear all
                    F - exit the program
>>> """).upper()
    if command == "C":
        create(myList, sideList)
    elif command == "V":
        display(myList, sideList)
    elif command == "U":
        update(myList, sideList)
    elif command == "D":
        delete(myList, sideList)
    elif command == "E":
        delete_all(myList, sideList)
    elif command == "F":
        print("Have a nice day")
        myFile = open("todolist2.pickle", "wb")
        pickle.dump(myList, myFile)

