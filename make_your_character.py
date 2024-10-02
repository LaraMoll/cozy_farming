# Skin tone list 
skin_tones_list = ["Pale skin","Fair skin","Medium skin","Olive skin","Naturally brown skin","Very dark"]

# Hair color:
hair_color_list = ["Blond","Brown","Black","Ginger"]

# Eye color:
eye_color_list = ["Blue","Green","Blown","Black","Grey"]

# Body type:
body_type_list = ["Muscular","Curvy","Skinny"]

# Accessoiries: 
accessories_list = ["Straw hat","Glasses","Ribbon","Ferdora hat","Necklace","Bracelet","Earrings"]

# Empty list for the farmers choice
farmer_choice = []

def skin_tone_valid(skin_tone):
    if skin_tone.isdigit() and 0 <= int(skin_tone) < len(skin_tones_list):
        return True
    return False

def hair_color_valid(hair_color):
    if hair_color.isdigit() and 0 <= int(hair_color) < len(hair_color_list):
        return True
    return False


# Function voor de skin tones
def choose_skin_tone():
    while True:
        for index, value in enumerate(skin_tones_list):
            print(f"{index}: {value}")
        
        skin_tone_question = input("Please select a skin tone by entering a number (0-3): ")

        if not skin_tone_valid(skin_tone_question):
            print("Not in the list, choose again :(! ")
        else:
            skin_tone = skin_tones_list[int(skin_tone_question)]
            print(f"You chose: {skin_tone}")
            skin_tone_lockin = input("Are you sure that you want this skin color. yes or no : ").lower()
            if skin_tone_lockin == "yes":
                print(f"Okay! you chose: {skin_tone}")
                farmer_choice.append(skin_tone)
                break
            if skin_tone_lockin == "no":
                print(f"Oh okay then, choose again.")
                return choose_skin_tone()


# Function voor de hair color
def choose_hair_color():
    while True:
        for index, value in enumerate(hair_color_list):
            print(f"{index}: {value}")
        
        hair_color_question = input("Please select a hair color by entering a number (0-5): ")

        if not hair_color_valid(hair_color_question):
            print("Not in the list, choose again :(! ")
        else:
            hair_color = hair_color_list[int(hair_color_question)]
            print(f"You chose: {hair_color}")
            hair_color_lockin = input("Are you sure that you want this hair color. yes or no : ").lower()
            if hair_color_lockin == "yes":
                print(f"Okay! you chose: {hair_color}")
                farmer_choice.append(hair_color)
                break
            if hair_color_lockin == "no":
                print(f"Oh okay then, choose again.")
                return choose_hair_color()
            



def main():
    choose_skin_tone()
    print("")
    choose_hair_color()
    print("")


main()