import display_db
def edit(Data_base):
    display_db.disp(Data_base)
    id=input("Input ID to change: ")
    print(Data_base[0].num_id)
    for i in Data_base:
        if i.num_id==id:
            i.edit()

