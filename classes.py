#classes file

# Function to start talking to townspeople for in level 2 (fall)
# A class attribute to start talking to towns people
class start_talking_to_townspeople:
    def __init__(self, description , options):
        # Towns people dialogue
        self.description = description
        # Talking options 
        self.options = options

    def towns_dialogue(self):
        # Print the scene dialogue
        print(self.description)
        for key, value in self.options.items():
            print(f"{key}: {value['description']}")

    def choose_options(self, choice):
        if choice in self.options:
            # Return the next dialogue
            action = self.options[choice]['action']
            action()
        else:
            print("invalid option")