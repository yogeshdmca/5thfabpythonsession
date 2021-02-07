students = [{'name': 'abha', 'age': '32', 'city': 'indore', 'clas': 'bca'}, {'name': 'arohi', 'age': '28', 'city': 'bhopal', 'clas': 'mca'}, {'name': 'vivek', 'age': '45', 'city': 'puna', 'clas': 'mca'}, {'name': 'kunal', 'age': '22', 'city': 'kargone', 'clas': 'bsc'}]

while True:
    comd = input("Input 1 for add data, \n Input 2 for  search data by name,\n enter 3 for all student \n Input 4 for exit?: ")
    try:
        comd = int(comd)
    except:
        print("You enter Wrong value")
        continue

    if comd == 1:
        name = input("Name:")
        age = input("Age:")
        city = input("city")
        clas = input("class")
        student = {'name':name, 'age': age, 'city':city, 'clas':clas}
        students.append(student)

    elif comd == 2:
        val = input("Enter name for find details:")
        name="Not available"
        for stu in students:
            if stu['name'] == val:
                name = stu
                break
        print(name)

    elif comd==4:
        exit(0)

    elif comd==3:
        print(students)

    else:
        print ("You have enter number that not defined")
