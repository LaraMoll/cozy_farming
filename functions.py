import random
from main import farmers_name




# Function fishing game
def start_fishing():
    # Fall season fishes
    fall_fishes = ["Cod","Thumb","Swordfish","Mullet","Golden","Sea bass"]
    
    your_caught_fishes = []
    fishes_caught = 0
    while True:
        # import random. choosing one of the fishes in the fall_fishes list
        get_random_fish = random.choice(fall_fishes)
        print("\n--- You start fishing ---")
        print("  🦯")
        print("    |")
        print("    |")
        print("    |")
        print("    |    🐟")
        print("    |🐟")
        print(f"\n--- You did it! you caught a {get_random_fish}")
        your_caught_fishes.append(get_random_fish)
        print(your_caught_fishes)
        fishes_caught += 1
        # Continue fishing input
        continue_fishing = input("Do you want to continue fishing? yes/no ").lower()
        if continue_fishing == "yes":
            print(f"you caught {fishes_caught}")
        elif continue_fishing == "no":
            print("okay!")
            break
        else:
            print("That wasn't an option sadly.")
            break

# Function planting crops
def start_planting_crops():
    # Amount of crops planted
    global crops_planted
    crops_planted = 0
    while True:
        print("""
You have the following crops to choose from:
1) Wheat
2) Carrot
3) Corn
4) Exit planting mode
""")
    
        crop_choice = input("What would you like to plant? (Type the number)\n")
        
        if crop_choice == '1':
            crops_planted += 1
            print("You planted some Wheat!")
        elif crop_choice == '2':
            crops_planted += 1
            print("You planted some Carrots!")
        elif crop_choice == '3':
            crops_planted += 1
            print("You planted some Corn!")
        elif crop_choice == '4':
            print(f"\nYou have planted a total of {crops_planted} crops. Great job!")
            break
        else:
            print("Please select a valid option.")



def kids_func():
    global farmers_name
    print(f"""
As you approach the playing kids, one of them kicks a ball in your face.

{farmers_name}: Ouch! what the. These damn kids why did i approach them, Yikes.

Playing kids: Hey old geezer! can you give me my ball back?

""")
    while True:
        give_ball_back = input("Do you give the ball back? yes or no ").lower()
        if give_ball_back == "yes":
            print(f"""
--- As a petty person you are, you pick up the ball and throw it to one of the kids's face making them cry ---

{farmers_name}: Oop- time to run away. I don't want their mothers after me.

--- You run away ---
""")
            break
        elif give_ball_back == "no":
            print(f"""
--- As a petty person you are, you pick up the ball and throw it into the river ---

{farmers_name}: HA! that's what you little pests deserve. 

--- You walk away ---
""")
            break
        else:
            print("That wasn't an option")

def two_grannies_func():
    global farmers_name
    print("You see two grannies sitting on a bench talking with each other.")
    while True:
        want_to_approach = input("Do you want to approach them? yes or no ").lower()
        if want_to_approach == "yes":
            print(f"""
--- You walk confidently to the old grannies ---

{farmers_name}: Hey Beauties do you come here often? 

Grannie 1: Oh that's so kind of you
Grannie 2: Do you need something?

{farmers_name}: Not really.

Grannie 2: Okay? then leave
""")
            break
        elif want_to_approach == "no":
            print(f"""
--- As you walk past the two old grannies one of them stops you---

Grannie 1: Hey there young person. 

{farmers_name}: Hello, what do you ladies want?

Grannie 2: Oh nothing, you look uglier than i expected.
""")  
        break      

def young_female_func():
    global farmers_name
    riddle_tries = 2
    print(f"""
--- A young lady is watering the flowers ---

{farmers_name}: Hello! those are some beautiful flowers.

Young lady: Thank you i love flowers. I'll give you a flower if you guess my riddle.

Riddle starts
---
I always come, but also always go. i am always present, yet never still. What am I?
""")
    while True:
        riddle_answer = input("What is your riddle answer? ").lower()
        if riddle_answer == "time":
            print("Correct! here is your Flower. Enjoy :)")
            break
        else: 
            riddle_tries -= 1
            if riddle_tries > 0:
                print(f"Unfortunately, that is not the right answer. you have {riddle_tries} tries left.")
            else:
                print("the answer was a Time")
                break

def quit_talking_func():
    print("I guess no talking")
    print("")

def start_exploring():
    riddle_tries = 2
    riddle_tries1 = 2

    while True:
        print("""
You start going into the forest, and suddenly you fall into a pit and your sight blackens.
        """)
        print("Welcome to a dream...")
        print("Let's play!")
        
        setting = input("Do you want to go to the jungle or the desert? ").lower()
        
        if setting == 'jungle':
            print("Welcome to the mighty Amazon jungle. Your tour guide told you to wait here...")
            response = input("But he has been gone a long time. Follow him or wait here? ").lower()
            
            if response == "follow":
                print("""
You follow him into the trees... As autumn falls, you find yourself at the edge of the Whispering Woods. 
They say the forest awakens this time of year, filled with spirits and secrets.
An elf appears and offers you a riddle.
                """)
                solve_jungle_riddle = input("Do you want to solve the riddle or wait for the tour guide? (yes/wait): ").lower()
                
                if solve_jungle_riddle == "yes":
                    while riddle_tries > 0:
                        answer_jungle_riddle = input("I am easy to lift, but hard to throw. What am I? ").lower()
                        if answer_jungle_riddle == "feather":
                            print("Correct! You've succeeded in the jungle challenge!")
                            quit_game()
                        else:
                            riddle_tries -= 1
                            if riddle_tries > 0:
                                print(f"Unfortunately, that is not the right answer. You have {riddle_tries} tries left.")
                            else:
                                print("The correct answer was 'feather'. Game over.")
                                quit_game()
                elif solve_jungle_riddle == "wait":
                    print("You wait another 10 minutes, but the guide still isn't here. Game over.")
                    quit_game()
                else:
                    print("Not an option. Try again.")
            elif response == "wait":
                print("You wait another 10 minutes, but the guide still isn't here. Game over.")
                quit_game()
            else:
                print("Not an option. Try again.")

        elif setting == "desert":
            print("Welcome to the mighty Sahara desert. Your tour guide told you to wait here...")
            response = input("But he has been gone a long time. Follow him or wait here? ").lower()
            
            if response == 'follow':
                print("\nYou follow him into the dunes...")
                transport = input("You see a canoe nearby... Walk or take the canoe down the river? ").lower()
                
                if transport == 'walk':
                    print("\nYou walk into the desert and a scorpion stops you for a riddle.")
                    while riddle_tries1 > 0:
                        desert_riddle = input("Splendid! The riddle goes: When it falls it never gets hurt. What is it? ").lower()
                        if desert_riddle == "leaf":
                            print("Correct! You've succeeded in the desert challenge!")
                            quit_game()
                        else:
                            riddle_tries1 -= 1
                            if riddle_tries1 > 0:
                                print(f"Unfortunately, that is not the right answer. You have {riddle_tries1} tries left.")
                            else:
                                print("The correct answer was 'leaf'. Game over.")
                                quit_game()
                elif transport == "wait":
                    print("You wait another 10 minutes, but the guide still isn't here. Game over.")
                    quit_game()
                else:
                    print("Not an option. Try again.")
            elif response == "wait":
                print("You wait another 10 minutes, but the guide still isn't here. Game over.")
                quit_game()
            else:
                print("Not an option. Try again.")
        else:
            print("That's not an option. Try again.")

def quit_game():
    print("""

-----
Who would have imaged that 
This is the end
Bye""")
    quit()