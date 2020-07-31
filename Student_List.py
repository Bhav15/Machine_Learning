# student list
#C- Insert R-Retrieve/View U-Update, D- Delete
#create empty list

student_name=[]
#infinite loop

while True:
    print("""Select a option from the below menu:
1. Inserting one name
2. Inserting multiple names
3. Updating an existing name
4. Deleting a name
5. View all names
6. Quit the program""")
    ch=int(input("Enter your choice:"))
    if ch==1:
    #pass means nothing
        #pass
        student_name.append(input("Enter student name: "))
    elif ch==2:
        names = input("Enter multiple names comma seperated:")
        names = names.strip()  #removes spaces before name
        if not names == "" or not names is None or not names == " ":
            student_name.extend(names.split(","))
    elif ch==3:
        ch1 = int(input("How would you like to input data\n 1. Name\n 2. Number\n"))
        if ch1==1:
            name= input("Enter the name you want to modify")
            if name in student_name:
                student_name[student_name.index(name)]=input("Enter modified name")
            else:
                print("This name is not available")
        else:
            for i in range(len(student_name)):
                print("{}. {}".format(i+1, student_name[i]))
            #input number
            idx = int(input("The number of the name you want to change:"))
            if idx <= len(student_name):
                student_name[idx-1] = input("Enter modified name:")
            else:
                  print("Invalid Input") 
                
    elif ch==4:
        ch2 = int(input("How would you like to input data\n 1. Name\n 2. Number\n"))
        if ch2==1:
            name=input("Enter the name you want to delete")
            if name in student_name:
                student_name==student_name.remove(name)
            else:
                print("This name is not available")
        else:
            for i in range(len(student_name)):
                print("{}. {}".format(i+1, student_name[i]))
            idx = int(input("The number of the name you want to delete:"))
            if idx <= len(student_name):
                student_name[idx-1] == student_name.pop(idx-1)
            else:
                print("Invalid Input")
    elif ch==5:
        for name in student_name:
            print(name)
    elif ch==6:
        print("""Thank you for using our program!""")
        break
    else:
        print("You have entered a wrong choice. Please try again")
