import create_person
import save_db
import display_db
import edit
from art import *


Object_DB=[]
save_db.Open(Object_DB)

menu_disp={1:"Display", 2:"Add", 3:"Edit", 0:"Quit"}


def Display():
    display_db.disp(Object_DB)
def Add():
    Object_DB.append(create_person.create_person())
    save_db.Save(Object_DB)
    input("Press Enter to continue...")
def Edit():
    edit.edit(Object_DB)
    save_db.Save(Object_DB)

menu={1: Display, 2: Add, 3:Edit}

while(True):
    print("\n" * 100)

    tprint("Mati - DB")

    for i, j in menu_disp.items():
       print(i, j)
    option=input("Input option: ")
    try:
        int(option)
    except:
        print("Invalid input")
        continue

    if int(option)==0:
        break

    menu[int(option)]()


save_db.Save(Object_DB)


