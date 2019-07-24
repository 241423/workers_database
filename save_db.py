import class_person


def Save(Data_base):
    with open("database.txt", "w+") as file:
        for object in Data_base:
            file.write(str(object.num_id) + ",")
            file.write(str(object.first_name) + ",")
            file.write(str(object.surname) + ",")
            file.write(str(object.birth_year) + ",")
            file.write(str(object.birth_month) + ",")
            file.write(str(object.birth_day) + ",")
            file.write(str(object.position) + ",")
            file.write(str(object.pesel))
            file.write('\n')


def Open(Data_base):
    base = [line.strip() for line in open("database.txt", 'r')]
    for line in base:
       data = line.split(",")
       id=data[0]
       first_name = data[1]
       surname = data[2]
       year = data[3]
       month = data[4]
       day = data[5]
       position = data[6]
       pesel = data[7]
       new = class_person.Person(id, first_name, surname, year, month, day, position, pesel)

       Data_base.append(new)


