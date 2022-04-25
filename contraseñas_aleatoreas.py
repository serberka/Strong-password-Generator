import random
import string
import os
import sys

i = random.randrange(9) + 1
website="https://raw.githubusercontent.com/serberka/ACSII-S3/master/arte/"+ str(i) + ".txt"
os.system("curl " +  website)

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


print(f"{bcolors.OK}BIENVENIDO AL GENERADOR DE CONTRASEÑAS SEGURAS!{bcolors.RESET}")
print ("By S3")

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    length = int(input("Escribe la longitud de la contraseña: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
generate_random_password()
exit(0)
