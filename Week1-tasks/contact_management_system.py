#to print contact list
def printlist(contact_list):
    print("Contacts:-")
    if len(contact_list) > 0:
        i = 1
        for key, value in sorted(contact_list.items()):
            Number = str(value)
            if len(Number) == 10:
                Number = Number[:3] + "-" + Number[3:6] + "-" + Number[6:]
            print(i,"->",str(key).capitalize(),"   ", Number)
            i = i + 1
    else:
        print("No Contact")

#to take number with validation
def take_number_by_validation():
    loop = True
    while(loop):
        try:
            Number = int(input("Enter the new Number: "))
            loop = False
        except Exception as e:
            print("Number can't contain letters.")
            loop = True
    return Number

#to store contacts
contact_list = {}
while(1):
    print("press 1: Display Contacts")
    print("press 2: Add Contact")
    print("press 3: Update Contact")
    print("press 4: Delete Contact")
    print("press 5: Search Contact")
    print("press 0: To Exit")

    #handle input data that it should be integer. 
    while(1):
        try:
            choise = int(input("Enter your choice here: "))
            break
        except Exception as e:
            print("Give input in Numbers.")

    print()
    if choise == 0:
        break
    elif choise > 5:
        #if given input is wrong
        print("wrong input:(")
    else:

        #print list
        if choise == 1:
            printlist(contact_list=contact_list)

        #add number
        elif choise == 2:
            while(1):
                Name = str(input("Enter the Name: "))
                if Name not in contact_list:
                    break
                print("Name is taken. choose another.")
            Number = take_number_by_validation()
            contact_list[Name] = Number
            print("Add Successfully.")

        #update contact
        elif choise == 3:
            printlist(contact_list=contact_list)
            old_Name = str(input("Enter the Name from List: "))
            if old_Name in contact_list:
                new_Name = str(input("Enter new Name: "))
                Number = take_number_by_validation()
                del contact_list[old_Name]
                contact_list[new_Name] = Number
                print("Update Successfully.")
            else:
                print("Name is not present in phone.")

        #delete contact
        elif choise == 4:
            printlist(contact_list=contact_list)
            Name = str(input("Enter the Name: "))
            if Name in contact_list:
                del contact_list[Name]
                print("Delete Successfully.")
            else:
                print("Contact is not found.")

        #search contact
        else:
            Name = str(input("Enter the Name: "))
            if Name in contact_list:
                print(Name,"   ", contact_list[Name])
            else:
                print("Contact is not found.")
    print()
