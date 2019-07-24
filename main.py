import create_person
import save_db
import display_db

Object_DB=[]

save_db.Open(Object_DB)
#new=create_person.create_person()

#Object_DB.append(new)

#print(Object_DB[0].first_name)

display_db.disp(Object_DB)

save_db.Save(Object_DB)


