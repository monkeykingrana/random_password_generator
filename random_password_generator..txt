#1 new password or saved password
#2 if selected new password
    #1 ask for length
    #2 create a password with length limit with category of number symbols and cpital and small letters
    #3 use this pasword or new
    #4 prompt for save password or not
    #5 if saves
        #1 save in a file named SAVED PASSWORDS
    #6 if not
        #1 redirect to homepage
#3 if selected saved passwords
    #open file SAVED PASSWORDS

print('HEllO DEAR')
print('What Do You Want To Do')
print('1. Generate New Password')
print('2. SAVED PASSWORDS')
usr_input_1= input('Enter Your Choice : ')

if usr_input_1=='1':
    usr_input_1_1=input('==Enter Length For Your Password==\n==>acceptable inputs are : 6,7,8,9,10 : ')
    if usr_input_1_1=='6':
        print('Thank You\nYour Input Is "6"')
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
