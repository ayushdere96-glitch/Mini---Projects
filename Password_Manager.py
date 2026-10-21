'''
1. Dictionary
2. Loops
3. Condiotonal
4. Module : Random
5. File Handling 
Example -->
Website : Password
'''
import random
import string

passwords = {}
try:
    with open('Password.txt', 'r') as file:
        for line in file:
            website, pwd = line.strip().split(' : ')
            passwords[website] = pwd
except:
    pass
def generate_passwords():
    chars = string.ascii_letters + string.digits + '!@#$%&'
    password = "".join(random.choice(chars) for _ in range(8))
    return password
while True:
    print('\n-----Personal Password Manager-----')
    print('1. Save Password')
    print('2. View Password ')
    print('3. Generate Password')
    print('4. Exit')
    choice = input('Eneter Your Choice : ')
    if choice == '1':
        site = input('Eneter Website : ')
        pwd = input('Enetr Password :')
        passwords[site] = pwd
        with open('Password.txt', "a") as file:
            file.write(f'{site}:{pwd}\n')
        print('Saved!')
    elif choice == '2':
        if not passwords:
            print('No Data')
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)
    elif choice == '3':
        print('Generate Password : ', generate_passwords())
    elif choice == '4':
        print('Ok Byee...')
        break
    else:
        print('In Valid Input')


