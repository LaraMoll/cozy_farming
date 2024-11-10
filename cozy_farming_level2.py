# Fall season fishes
fall_fishes = ["Cod","Thumb","Swordfish","Mullet","Golden","Sea bass"]

#Starting with the story line
def fall_story_beginning():
    riddle_tries = 2
    # Dialogue 
    print("""After waking up. You check your mailbox and see a mysterious letter inside.\nThe letter is red with fangs on it.  Out of curiosity you open it.\nA bat comes out from it!, you drop the envelope and take steps back.\n
---
Farmer: Holy! That startled me, a bat? How. Magic? Since when, I thought this was a normal village. 
---\n
You regain your composure and walk words the envelop to pick it up again. As you pick up the envelope you get a strange chill but you ignore it.\n
    """)
    while True:
        envelope = input("Do you want to read what's inside the letter? yes or no ").lower()
        if envelope == "no":
            print("You put the envelope away")
            break
            # To be continued. 
        elif envelope == "yes":
            print("You open the letter and start reading.")
            # letter in de envelope. 
            print("""---
You fool! Your land is now my land.
HAHAHAHA
I'll give you a chance to redeem yourself. with a riddle!
If you fail the riddle i'll drain a lot of your hp! if you pass it, i'll let you go for just this once.
Im giving you two chances.\n
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
                break
            else: 
                riddle_tries -= 1
                if riddle_tries > 0:
                    print(f"Unfortunately, that is not the right answer. you have {riddle_tries} tries left.")
                else:
                    print("the answer was a vampire")
                    print("loser >:)")
                    break
        else:
            print("sorry what?")
            


fall_story_beginning()  