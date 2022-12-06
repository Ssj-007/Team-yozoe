import random

def display(face):
    if(face==1):
        print("~~~~~~~~~~\n[          ]\n[    0     ]\n[          ]\n~~~~~~~~~~")
    elif(face==2):
        print("~~~~~~~~~~\n[          ]\n[   0 0    ]\n[          ]\n~~~~~~~~~~")
    elif (face == 3):
        print("~~~~~~~~~~\n[    0     ]\n[    0     ]\n[    0     ]\n~~~~~~~~~~")
    elif (face == 4):
        print("~~~~~~~~~~\n[   0 0    ]\n[          ]\n[   0 0    ]\n~~~~~~~~~~")
    elif (face == 5):
        print("~~~~~~~~~~\n[   0 0    ]\n[    0     ]\n[   0 0    ]\n~~~~~~~~~~")
    elif (face == 4):
        print("~~~~~~~~~~\n[   0 0    ]\n[   0 0    ]\n[   0 0    ]\n~~~~~~~~~~")
T=input("Press y to roll.Press n to exit ")
while(T=='y' or T=='Y'):
    face_value = random.randint(0, 6)
    display(face_value)
    T=input("Press y to roll again.Press n to exit ")

