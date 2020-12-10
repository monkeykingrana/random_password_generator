import random
import string
print('''HEllO DEAR

What Do You Want To Do

1. Generate New Password

2. SAVED PASSWORDS

''')
usr_input_1= input('==>Enter Your Choice :')


string.result =''
if usr_input_1=='1':
    usr_input_1_1=input('==Enter Length For Your Password==\n\n==>acceptable inputs are : 6,7,8,9,10 : ')
    def get_random_string(usr_input_1_1):
        sample_puntuations='*@#_$&'

        random_source = string.ascii_letters + string.digits + sample_puntuations
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(sample_puntuations)
        string.result = ''.join((random.choice(password) for i in range (usr_input_1_1)))
        print(string.result)
    get_random_string(int(usr_input_1_1))
    if usr_input_1_1=='6':
        print('Thank You\nYour Input Is "6"')

        print("Your Generated Password Is : ",string.result)

    elif usr_input_1_1=='7':
        print('Thank You\nYour Input Is "7"')
        print("Your Generated Password Is : ",string.result)

    elif usr_input_1_1=='8':
        print('Thank You\nYour Input Is "8"')
        print("Your Generated Password Is : ",string.result)

    elif usr_input_1_1=='9':
        print('Thank You\nYour Input Is "9"')
        print("Your Generated Password Is : ",string.result)

    elif usr_input_1_1=='10':
        print('Thank You\nYour Input Is "10"')
        print("Your Generated Password Is : ",string.result)

    else:
        print('\n===> SORRY INVALID INPUT <===\n')
        print('====> TRY AGAIN PLEASE <====\n')


elif usr_input_1=='2':
    print('COMMING SOON')
else:
    print('\n===> SORRY INVALID INPUT <===\n')
    print('====> TRY AGAIN PLEASE <====\n')
