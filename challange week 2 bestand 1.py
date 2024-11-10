start = input("Welcome to level two...\nwould you like to play the game or die?: ")
if start == 'play':
    print ("Great let's play the game! ")
    setting = input("want to go to the jungle or the desert?")
else:
    print("Lame, okay you are dead now...")
    quit()

if setting == 'jungle':
    print("Welcome to the mighty amazon jungle, your tour guide told you to wait here...")
    response = input("But he has been gone a long time... follow him or wait here?")


    if response == 'follow':
        print("""You follow him into the trees...as autumn falls... \nyou find yourself at the edge of the Whispering Woods... 
            \nthey say the forest awakens this time of year, filled with spirits and secrets. 
            \nas you ponder upon the trees an elf comes up to you. \nit asks you if you want to solve a riddle: yes or no go back and wait on tour guide? : """)
        

if response == 'yes':
    print("Great , the riddle goes:  I am easy to lift, but hard to throw. What am I?")





elif response == 'wait':
        print("You wait another 10 minutes and he still isn't here")
else:
    print('Invalid response... You lose!')
    
if setting == 'desert':
    print("Welcome to the mighty sahara desert , your tour guide told you tyo wait here...")
    response = input("But he has been gone a long time... follow him or wait here?")


if response == 'follow':
        print("You follow him into the dunes")
        transport = input('You see a canoe nearby... walk or take the canoe down the river?')


        if transport == 'walk':
            response = input("You walk into the desert and a scorpion stops you for a riddle.. do you want to solve the riddle?:")

        if response =='yes':
            print("splendid! the riddle goes: When it falls it never gets hurt, what is it? ")

        elif input == 'leaf':
            response = input ("")
            print("Correct, you may continue your journey")

        else:
            print("False, you die! the scorpion says at it injects you with venom...")
            quit()

            if response == 'canoe':
    else:
        print('invalid response... you lose!') 

    elif response == 'wait':
        print("You wait another 10 minutes and he still isn't here")
    else:
        print('Invalid response... You lose!')

    else: 
        print('Invalid response... You lose!')