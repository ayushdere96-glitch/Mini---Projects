'''
Student Result Manager
Use -: 
1. Loops
2. Dictionaries 

'''
student = {}

while True:
    print('\n-----Student Manager App-----')
    print('1. Add Student')
    print('2. View Student ')
    print('3. Check Result')
    print('4. Exit')

    choice = input('Enter Your Choice : ')
    if choice == '1':
        name = input('Eneter Student Name : ')
        marks = int(input('Enetr Marks : '))
        student[name] = marks
        print(f"{name} Succesfully Added!")
    elif choice == '2':
        if not student:
            print('No Student Found!')

        else:
            for name, marks in student.items():
                print(name,':', marks)
    elif choice == '3':
        name = input('Enter The Name : ')
        if name in student:
            marks = student[name]
            if marks >=40:
                print('PASS')
            else:
                print('FAIL')
        else:
            print('Student Not Found!')
    elif choice == '4':
        print('Exiting....')
        break
    else:
        print('In - Valid Input')
