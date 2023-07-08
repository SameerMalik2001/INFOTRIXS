#to print contact list
def printlist(contact_list):
    print("Contacts:-")
    print("     Name","                                               ","Number")
    print()
    if len(contact_list) > 0:
        i = 1
        for key, value in sorted(contact_list.items()):
            Number = str(value)
            if len(Number) == 10:
                Number = Number[:3] + "-" + Number[3:6] + "-" + Number[6:]
                space = ""
                for j in range(len(key),51):
                    space = space + " "
            print(i,"->",key,space, Number)
            i = i + 1
    else:
        print("No Contact")

#to take number with validation
def take_number_by_validation():
    loop = True
    while loop:
        try:
            Number = int(input("Enter the Number: "))
            if len(str(Number)) != 10:
                print("Number should be of 10 digit.")
                continue
            loop = False
        except Exception as e:
            print("Number can't contain letters.")
            loop = True
        

    return Number

#to remove leading spaces from name, if user add that by mistake
def trim_name(Name):
    Name1 = Name
    for i in range(0,len(Name)):
        if Name[i] == " ":
            Name1 = Name1[1:]
        else:
            break
    break_point = 0
    for i in range(0,len(Name1)):
        if Name1[i] != " ":
            break_point = i
    if break_point+1 != len(Name1):
        Name1 = Name1[:break_point+1]
    return Name1

#to store contacts
contact_list = {}
while 1:
    print("press 1: Display Contacts")
    print("press 2: Add Contact")
    print("press 3: Update Contact")
    print("press 4: Delete Contact")
    print("press 5: Search Contact")
    print("press 0: To Exit")

    #handle input data that it should be integer. 
    while 1:
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
            while 1:
                Name = str(input("Enter the Name: "))
                if Name in contact_list:
                    print("Name is taken. choose another.")
                elif len(Name) > 40:
                    print("Name is too long. Try short Name.")
                elif Name not in contact_list:
                    break
            Number = take_number_by_validation()
            contact_list[trim_name(Name)] = Number
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
            print()
            print("Name","                                               ","Number")
            if Name in contact_list:
                space = ""
                for j in range(len(Name),51):
                    space = space + " "
                print(Name,space, contact_list[Name])
            else:
                print("Contact is not found.")
    print()
