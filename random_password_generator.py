import random
import string
print('HEllO DEAR\nWhat Do You Want To Do\n1. Generate New Password\n2. SAVED PASSWORDS\n\n')
usr_input_1= input('==>Enter Your Choice :')




if usr_input_1=='1':
    usr_input_1_1=input('==Enter Length For Your Password==\n\n==>acceptable inputs are : 6,7,8,9,10 : ')

    def get_random_string(len):

        random_source = string.ascii_letters + string.digits
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        result = ''.join((random.choice(sample_puntuations) for i in range (usr_input_1_1)))
        get_random_string(usr_input_1_1)
    if usr_input_1_1=='6':
        print('Thank You\nYour Input Is "6"')
        print("Your Generated Password Is : ",result)

    elif usr_input_1_1=='7':
        print('Thank You\nYour Input Is "7"')
    elif usr_input_1_1=='8':
        print('Thank You\nYour Input Is "8"')
    elif usr_input_1_1=='9':
        print('Thank You\nYour Input Is "9"')
    elif usr_input_1_1=='10':
        print('Thank You\nYour Input Is "10"')
    else:
        print('\n===> SORRY INVALID INPUT <===\n')
        print('====> TRY AGAIN PLEASE <====\n')


elif usr_input_1=='2':
    print('COMMING SOON')
else:
    print('\n===> SORRY INVALID INPUT <===\n')
    print('====> TRY AGAIN PLEASE <====\n')
