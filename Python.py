#imports

import time
import random




#-------------------------


name = input("Enter Your name: ")
print("hello " + name)
time.sleep (1)

age = int(input("What is your age?"))

time.sleep(1)

print("nice to meet you " + str(name))

time.sleep(2)

current_year = 2021
birth_year = current_year - age

print("So you are born in " + str(birth_year))

time.sleep(1)

print("lets play a game!!!")
time.sleep(1)

print("loading")
time.sleep(0.1)
print("loading.")
time.sleep(0.1)
print("loading..")
time.sleep(0.1)
print("loading...")
time.sleep(0.1)
print("loading....")
time.sleep(0.1)
print("loading.....")
time.sleep(0.1)
print("loading......")
time.sleep(0.1)
print("loading.......")
time.sleep(0.1)
print("loading........")
time.sleep(0.1)
print("loading..........")
time.sleep(0.1)
print("loading...........")
time.sleep(0.1)
print("loading............")
time.sleep(0.1)
print("loading.............")
time.sleep(0.1)
print("loading..............")
time.sleep(0.1)
print("loading................")
time.sleep(0.1)
print("loading.................")
time.sleep(0.1)
print("loading..................")
time.sleep(0.1)
print("loading...................")
time.sleep(0.1)
print("loading....................")
time.sleep(0.1)
print("loading.....................")####
time.sleep(0.1)
print("loading......................")
time.sleep(0.1)
print("loading.......................")
time.sleep(0.1)
print("loading........................")
time.sleep(0.1)
print("loading.........................")
time.sleep(0.1)
print("loading..........................")
time.sleep(0.1)
print("loading...........................")
time.sleep(0.1)
print("loading............................")
time.sleep(0.1)
print("loading.............................")
time.sleep(0.1)
print("loading..............................")
time.sleep(0.1)
print("loading...............................")
time.sleep(0.1)
print("loading................................")
time.sleep(0.1)
print("loading.................................")
time.sleep(0.1)
print("loading..................................")
time.sleep(0.1)
print("loading \033[1;32m 100%")
time.sleep(0.1)

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

