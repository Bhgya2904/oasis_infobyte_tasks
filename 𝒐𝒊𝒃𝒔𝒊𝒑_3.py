import random

uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters=uppercase_letters.lower()
digits="0123456789"
symbols="!@#$%^&*_~"
length=int(input("enter the length:"))
print('''enter the choice:
             1.upper case
             2.lowercase
             3.digits
             4.symbols
             5.exit''')
all=""
while(True):
    choice=int(input("enter ur choice:"))
    if (choice==1):
        all+=uppercase_letters
    elif (choice==2):
        all+=lowercase_letters
    elif (choice==3):
        all+=digits
    elif (choice==4):
        all+=symbols
    elif (choice==5):
        break
    else:
      print("enter valid choice")
password="".join(random.sample(all,length))
print(password)