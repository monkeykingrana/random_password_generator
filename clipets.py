from datetime import datetime, date
now,date = datetime.now() ,date.today()
now,date = now.strftime("%H:%M:%S"), date.strftime("%d/%m/%Y")
print(date,now)
# Python code to illustrate append() mode
file = open('saved_password.txt','a')
data='\n\n\n\n' + date+ now
file.write(data)
file.close()
file2 = open('saved_password.txt','r+')

for each in file2:
    print(each)
file2.close()
##########################################################################################################################################################

from datetime import datetime, date
now,date = datetime.now() ,date.today()
now,date = now.strftime("%H:%M:%S"), date.strftime("%d/%m/%Y")
print(date,now)
# Python code to illustrate append() mode
file = open('saved_password.txt','a')
data='\n\n\n\n' + date+ now
file.write(data)
file.close()
file2 = open('saved_password.txt','r+')

for each in file2:
    print(each)
file2.close()
