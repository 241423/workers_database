import check_person
import class_person
import random

def num_id():
    id=random.randint(100,999)
    return id

def create_person():
    id=num_id()
    first_name=check_person.f_name()
    surname=check_person.s_name()
    year=check_person.b_year()
    month=check_person.b_month()
    day=check_person.b_day(month)
    position=check_person.pos()
    pesel=check_person.pesel()

    print("Do you accept person data? Input Y")
    print("First name: ", first_name )
    print("Surname: ", surname)
    print("Birth year: ", year)
    print("Birth month: ", month)
    print("Birth day :", day)
    print("Position :", position)
    print("Pesel :", pesel)

    decision=input("Decision: ")

    if decision=="Y" or decision=="y":
        return class_person.Person(id, first_name, surname, year, month, day, position, pesel)

    else:
        print("Creating stopped!")


