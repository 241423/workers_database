import class_person
import termtables as tt

import os

def clear_screen():
    print ("\n" * 100)


def b_day_reedable(year, month, day):
    months={
        1:"Jan",
        2:"Feb",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"Jun",
        7:"Jul",
        8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nov",
        12:"Dec"
    }
    return day, months[int(month)], year



def disp(Data_base):
    clear_screen()
    table=[]
    for person in Data_base:
        p_table=[]
        p_table.append(person.num_id)
        p_table.append(person.first_name)
        p_table.append(person.surname)
        date=b_day_reedable(person.birth_year, person.birth_month, person.birth_day)
        p_table.append(date[0] +" "+ date[1] +" "+ date[2])
        p_table.append(person.position)
        p_table.append(person.pesel)
        table.append(p_table)


    string = tt.to_string(
        [table],
        header=["ID", "First name", "Surname", "Date of birth" , "Position", "Pesel"],
        style=tt.styles.ascii_thin_double,
        # alignment="ll",
        # padding=(0, 1),
    )
    print(string)

    input("Press Enter to continue...")


