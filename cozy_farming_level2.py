import random
from main import *
from functions import *
from classes import *

# Fall season fishes
# fall_fishes = ["Cod","Thumb","Swordfish","Mullet","Golden","Sea bass"]

#Starting with the story line
def fall_story_beginning():
    # Printing the start of the dialogue 
    print("""After waking up. You check your mailbox and see a mysterious letter inside.
The letter is red with fangs on it. Out of curiosity you open it.
A bat comes out from it! you drop the envelope and take some steps back.
---
Farmer: Holy! That startled me, a bat? How. Magic? Since when, I thought this was a normal village. 
---
You regain your composure and walk words the envelop to pick it up again. As you pick up the envelope you get a strange chill but you ignore it.
    """)
    # While loop for reading content inside the letter.
    while True:
        envelope = input("Do you want to read what's inside the letter? yes or no ").lower()
        if envelope == "no":
            print("You put the envelope away")
            to_read_letter_no()
            break
        elif envelope == "yes":
            to_read_letter_yes()
            break
        else:
            print("sorry what?")

def to_read_letter_no():
    # Start dialogue for the town that puts them to different functions 
    start_talking = start_talking_to_townspeople(
        description="After pondering for a while you talk to the town.",
        options={
            '1': {'description': "Kids that are playing.", 'action': kids_func},
            '2': {'description': "Two old grannies", 'action': two_grannies_func},
            '3': {'description': "A young female who is busy tending the flowers", 'action': young_female_func},
            '4': {'description': "Quit talking", 'action': quit_talking_func}
        }
    )
    while True:
        print("What do you want to do?")
        choose_activity = input("""
Plant crops (P)
Go fishing (F)
Talk to town people (T)
Explore (E)
""").lower()
        
        if choose_activity == "p":
            start_planting_crops()
        elif choose_activity == "f":
            start_fishing()
        elif choose_activity == "t":
            start_talking.towns_dialogue()
            choice = input("Choose who you want to talk to: ")
            start_talking.choose_options(choice)
        elif choose_activity == "e":
            start_exploring()
        else:
            print("That wasn't an option sadly")
def to_read_letter_yes():
    riddle_tries = 2
    print("You open the letter and start reading.")
    # letter in de envelope. 
    print("""---
You fool! Your land is now my land.
HAHAHAHA
I'll give you a chance to redeem yourself. with a riddle!
If you fail the riddle i'll drain a lot of your hp! if you pass it, i'll let you go for just this once.
Im giving you two chances.
---""")
        # Riddle 1. 
    while riddle_tries > 0:
        vampire_riddle = input("""The riddle starts:
----
I come out at night, I am neither human nor an animal.
I rarely eat I only drink, I can be only found at night, 
I will glow in the sunlight. What am i?
----
""").lower()
        if vampire_riddle == "vampire" or vampire_riddle == "a vampire":
            print("to be continued")
            # Start dialogue for the town that puts them to different functions 
            start_talking = start_talking_to_townspeople(
                description="After pondering for a while you talk to the town.",
                options={
                    '1': {'description': "Kids that are playing.", 'action': kids_func},
                    '2': {'description': "Two old grannies", 'action': two_grannies_func},
                    '3': {'description': "A young female who is busy tending the flowers", 'action': young_female_func},
                    '4': {'description': "Quit talking", 'action': quit_talking_func}
                }
            )
            while True:
                print("What do you want to do?")
                choose_activity = input("""
Plant crops (P)
Go fishing (F)
Talk to town people (T)
Explore (E)
""").lower()
                
                if choose_activity == "p":
                    start_planting_crops()
                elif choose_activity == "f":
                    start_fishing()
                elif choose_activity == "t":
                    start_talking.towns_dialogue()
                    choice = input("Choose who you want to talk to: ")
                    start_talking.choose_options(choice)
                elif choose_activity == "e":
                    start_exploring()
                else:
                    print("That wasn't an option sadly")
        else: 
            riddle_tries -= 1
            if riddle_tries > 0:
                    print(f"Unfortunately, that is not the right answer. you have {riddle_tries} tries left.")
            else:
                    print("the answer was a vampire")
                    print("You're going back to the beginning for a new chance ")
                    print("")
                    fall_story_beginning()
            
if __name__ == "__main__":
    # call_functions()
    fall_story_beginning()