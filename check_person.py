import datetime

def f_name():
    while(True):
        f_name=input("Insert first name :")
        if len(f_name) < 3 or len(f_name) > 20:
            print("3 - 20 characters")
        else:
            return f_name

    return f_name

def s_name():
    while(True):
        s_name=input("Insert surname :")
        if len(s_name) < 3 or len(s_name) > 20:
            print("3 - 20 characters")
        else:
            return s_name

    return s_name




def b_year():
    now_time=datetime.datetime.now()
    while(True):
        year = input("Year of birth: ")
        try:
            int(year)
        except:
            print("Wrong input")
            continue
        if int(year)>now_time.year or int(year)<1900:
           print("Wrong input")
           continue
        else:
           return year


def b_month():
    while(True):
        month=input("Month of birth (count): ")
        try:
            int(month)
        except:
            print("Wrong input")
            continue
        if int(month)<1 or int(month)>12:
            print("Wrong format")
            continue
        else:
            return month

def b_day(month):
    while(True):
        day=input("Day of birth: ")
        try:
            int(day)
        except:
            print("Wrong input")
            continue
        if(int(day)<1 or int(day)>29 and int(month)==2):
            print("This month has less than 29 days")
            continue
        elif (int(day) < 1 or int(day) > 30 and (int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11)):
            print("This month has less than 30 days")
            continue
        elif (int(day)<1 or int(day)> 31):
            print("This month has less than 31 days")
        else:
            return day


def pos():
    while(True):
        pos_type={
            1:"Boss",
            2:"Manager",
            3:"IT support",
            4:"Worker",
            5:"Accountman"
        }

        print("Position Type:")
        for nr, pos in pos_type.items():
            print(nr, pos )

        position=input("Input position (count) :")
        try:
            int(position)
        except:
            print("Wrong input")
            continue
        if(int(position)<1 or int(position)>len(pos_type)):
            print("Wrong input")
            continue
        else:
            return pos_type[int(position)]


def pesel():
    while(True):
        pesel=input("Input your pesel number: ")
        try:
            int(pesel)
        except:
            print("Wrong input")
            continue
        if len(pesel)!=11:
            print("Wrong input")
            continue
        else:
            return pesel


