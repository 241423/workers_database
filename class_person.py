import check_person

class Person:
    def __init__(self, num_id, first_name, surname, birth_year, birth_month, birth_day, position, pesel):
        self.num_id=num_id
        self.first_name=first_name
        self.surname=surname
        self.birth_year=birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.position=position
        self.pesel=pesel

        self.pos_to_change = {
            1: self.edit_fname,
            2: self.edit_sur,
            3: self.edit_year,
            4: self.edit_month,
            5: self.edit_day,
            6: self.edit_pos,
            7: self.edit_pesel
        }

    def edit_fname(self):
        self.first_name=check_person.f_name()
    def edit_sur(self):
        self.surname=check_person.s_name()
    def edit_year(self):
        self.birth_year=check_person.b_year()
    def edit_month(self):
        self.birth_month=check_person.b_month()
    def edit_day(self):
        self.birth_day=check_person.b_day(self.birth_month)
    def edit_pos(self):
        self.position=check_person.pos()
    def edit_pesel(self):
        self.pesel=check_person.pesel()

    def edit(self):
        while(True):
            pos_to_change_disp = {
                1: "First name",
                2: "Surname",
                3: "Birth year",
                4: "Birth month",
                5: "Birth day",
                6: "Position",
                7: "Pesel"
            }

            print("What do you want change? ")
            for nr, pos in pos_to_change_disp.items():
                print(nr, pos)
            number = input("Input position (count) :")
            try:
                int(number)
            except:
                print("Wrong input")
                continue
            if int(number) == 0:
                break
            elif (int(number) < 1 or int(number) > len(pos_to_change_disp)):
                print("Wrong input")
                continue
            else:
                self.pos_to_change[int(number)]()
                return False





