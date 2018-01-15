import time
import random

print("Press A to Start.")

start = input()
print()

HP = 100
EXP = 0
EHP = 50
MP = 100

##Battle Choice 1
def choice1():
    print("Alright there is a big dog blocking your path, what do you do?")
    print("-------------------------------")
    print("HP: " + str(HP) + "            " + "Enemy HP: " + str(EHP))
    print("-------------------------------")
    print("A - Hit it with a nearby stick")
    print("B - Kick it with your yeezys")
    print("C - Jump over it")
    print("D - Run")
    print()
    choice = input()

    if choice == "A":
        story1()
    elif choice == "B":
        story2()
    elif choice == "C":
        story3()
    elif choice == "D":
        story4()

def choice2():
    global EHP
    EHP = 75
    print("The officer wants to arrest you")
    print("-------------------------------")
    print("HP: " + str(HP) + "            " + "Enemy HP: " + str(EHP))
    print("-------------------------------")
    print("A - Slide him a $20")
    print("B - Drop kick him")
    print("C - Lie")
    print("D - Run")
    print()
    choice = input()

def choice2b():
    print("The officer is investigating the area for a stray dog.")
    time.sleep(3)
    print("The officer asks you for information on the dog")
    print()
    print("A - Truth")
    print("B - Lie")
    print("C - Ignore")
    print("D - Run")
    print()
    choice = input()

    if choice == "A":
        print("You tell the officer the dog is down the street")
        counter = 0
        while counter in range(3):
            print(".", end=" ")
            time.sleep(1)
            counter += 1
        print()
        print("The officer thanks you for your assistance!")
        ##Insert Next Part of Story Function Here
    elif choice == "B":
        print("You tell the officer you have not seen any dogs in the area")
        counter = 0
        while counter in range(3):
            print(".", end=" ")
            time.sleep(1)
            counter += 1
        print()
        belief = random.random()
        if belief >= 0.5:
            print("The officer believes you!")
            print()
            time.sleep(1)
            print("The officer thanks you for your assistance!")
            ##Insert Next Part of Story Function Here
    elif choice == "C":
        print("You act like the officer isn't there.")
        counter = 0
        while counter in range(3):
            print(".", end=" ")
            time.sleep(1)
            counter += 1
        print()
        success = random.random()
        if success >= 0.5:
            print("The officer thinks you're mentally impaired!")
            print()
            time.sleep(1)
            print("The officer walks away!")
            ##Insert Next Part of Story Function Here

def peta():
    print("Okay you are now on the run from PETA officers investigating the area")
    time.sleep(2)
    print("An officer approaches you!")
    print()
    global dog
    if dog == "dead":
        choice2()
    else:
        choice2b()

def story1():
    print("You pick up a nearby branch and hit the dog with it")
    counter = 0
    while counter in range(3):
        print(".", end=" ")
        time.sleep(1)
        counter += 1
    print()
    print("The dog is only slightly fazed by the attack")
    time.sleep(2)
    print("The dog takes a dump on your yeezys!")
    print()
    print(">>>>> YOU TAKE 10 DAMAGE <<<<<")
    print(">>>>> DOG TAKES 2 DAMAGE <<<<<")
    print()
    global HP
    global EHP
    HP -= 10
    EHP -= 2
    if HP <= 0:
        print("Your HP has reached 0.")
        print(">>>>> GAME OVER <<<<<")
        print()
        quit()
    choice1()

def story2():
    print("You kick the dog with your fresh new yeezys")
    counter = 0
    while counter in range(3):
        print(".", end=" ")
        time.sleep(1)
        counter += 1
    print()
    print("The dog takes an L")
    time.sleep(2)
    print("The dog dies!")
    print()
    print(">>>>> YOU GAIN 50 EXP <<<<<")
    print(">>>>> DOG IS DEFEATED <<<<<")
    print()
    dog = "dead"
    global dog
    global HP
    global EXP
    HP = 10
    EXP += 50
    peta()

def story3():
    print("You try to jump over the dog")
    counter = 0
    while counter in range(3):
        print(".", end=" ")
        time.sleep(1)
        counter += 1
    print()
    print("The dog jumps up!")
    time.sleep(2)

    global HP
    global EHP
    jump = random.random()
    if jump >= 0.5:
        print("You kick the dog in midair")
        print()
        print(">>>>> DOG TAKES 15 DAMAGE <<<<<")
        print()
        EHP -= 15
    else:
        print("The dog rips your sweatpants")
        print()
        print(">>>>> YOU TAKE 10 DAMAGE <<<<<")
        print()
        HP -= 10
    if HP <= 0:
        print("Your HP has reached 0.")
        print(">>>>> GAME OVER <<<<<")
        print()
        quit()
    choice1()

def story4():
    print("You dip out of there!")
    counter = 0
    while counter in range(3):
        print(".", end=" ")
        time.sleep(1)
        counter += 1
    print()
    print("The dog jumps up!")
    time.sleep(2)

    global HP
    global EHP
    run = random.random()
    if run >= 0.5:
        print("You get out of there!")
        dog = "alive"
        peta()
    else:
        print("The dog blocks your path!")
        print()
        print(">>>>> YOU TAKE 5 DAMAGE <<<<<")
        print()
        HP -= 5
    if HP <= 0:
        print("Your HP has reached 0.")
        print(">>>>> GAME OVER <<<<<")
        print()
        quit()
    choice1()
    

choice1()
