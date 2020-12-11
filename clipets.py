import random
import string
from os import system, name
def clear():
	if name == 'nt':
		_ = system('cls')
clear()

from datetime import datetime, date
now,date = datetime.now() ,date.today()
now,date = now.strftime("%H:%M:%S"), date.strftime("%d/%m/%Y")
print(date,now)
print('\nHEllO DEAR\nWhat Do You Want To Do\n1. Generate New Password\n2. SAVED PASSWORDS\n')
usr_input_1= input('\n==>Enter Your Choice :')
clear()
print(date,now)
clear()
print(date,now)

def file_append(generated_password):
	file=open('saved_password.txt', 'a')
	data='\n\n==>Date :  '+date+' | ==>Time :  '+now+'\n==>Website :  '+usr_input_web+' | ==>PASSWORD :  '+generated_password+'\n\n-----------\n\n'
	file.write(data)
	file.close()

def file_read():
	file2=open('saved_password.txt','r+')

	for i in file2:
		print(i)

	file2.close()


if usr_input_1=='1':
    usr_input_1_1=input('\n==Enter Length For Your Password==\n\n==>acceptable inputs are : 6,7,8,9,10 : ')
    usr_input_web=input('\n==Enter Name Of Website For Which PASSWORDS Is To Be Generated : ')

    def get_random_string(usr_input_1_1):
        sample_puntuations='*@#_$&'
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(sample_puntuations)
        string.result = ''.join((random.choice(password) for i in range (usr_input_1_1)))
    get_random_string(int(usr_input_1_1))
    
    file_append(string.result)

    clear() ,print(date,now)

    if usr_input_1_1=='6':
        print('\nThank You\nYour Input Is '+'"'+ usr_input_1_1 + '"' +"\nYour Generated Password Is : ",string.result)
    elif usr_input_1_1=='7':
        print('\nThank You\nYour Input Is '+'"'+ usr_input_1_1 + '"' +"\nYour Generated Password Is : ",string.result)
    elif usr_input_1_1=='8':
        print('\nThank You\nYour Input Is '+'"'+ usr_input_1_1 + '"' +"\nYour Generated Password Is : ",string.result)
    elif usr_input_1_1=='9':
        print('\nThank You\nYour Input Is '+'"'+ usr_input_1_1 + '"' +"\nYour Generated Password Is : ",string.result)
    elif usr_input_1_1=='10':
        print('\nThank You\nYour Input Is '+'"'+ usr_input_1_1 + '"' +"\nYour Generated Password Is : ",string.result)

    else:
        print('\n===> SORRY INVALID INPUT <===\n====> TRY AGAIN PLEASE <====\n')
elif usr_input_1=='2':
    file_read()
else:
    print('\n===> SORRY INVALID INPUT <===\n====> TRY AGAIN PLEASE <====\n')

