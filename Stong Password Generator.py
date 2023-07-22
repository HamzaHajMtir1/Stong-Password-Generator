import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

nb_char = (input("write the nember of caracter of the password ? "))
while True:
    try:
        nb_char = int(nb_char)
        if nb_char < 6:
            print("you need at least 6 caraccters")
            nb_char = input("enter the number aigain please : ")
        else:
            break
    except:
        print("*****You must give a number*****")
        nb_char = input("how many caracter for the password you want ? ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(nb_char *30/100)
part2 = round(nb_char *20/100)

password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])


for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
random.shuffle(password)
password = "".join(password)
print(password)
