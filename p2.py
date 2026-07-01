#This Python program is used to store single characters in a list. The user first enters how many characters they want to store. The program accepts only one character at a time and displays an error message if more than one character is entered. After storing the characters, it displays the list, performs an undo operation by removing the last entered character using the pop() method, and then displays the updated list.


a=[]
def add():
    no=int(input("Enter how many character you want to store :"))
    for i in range(no):

        while(True):
            ch=input("Enter character :")

            if len(ch)==1:

                a.append(ch)
                break
            else:
                print("enter only single character...")


        

def display():
    print(a)


def undo():
    a.pop();

def menu():
    add()
    display()
    print("pop")
    undo()
    display()

menu()