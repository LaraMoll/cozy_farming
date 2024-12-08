# Define a class to represent each scene
class Scene:
    def __init__(self, description, options):
        self.description = description  # Scene description
        self.options = options  # Available options

    def display_scene(self):
        print(self.description)  # Print the scene description
        for key, value in self.options.items():
            print(f"{key}: {value['description']}")  # Print each option

    def choose_option(self, choice):
        if choice in self.options:
            return self.options[choice]['next_scene']  # Return the next scene
        else:
            print("Invalid choice. Try again.")
            return None

# Create scenes
scene1 = Scene(
    description="You are in a dark forest. There are paths to the north and east.",
    options={
        '1': {'description': "Go north", 'next_scene': 'scene2'},
        '2': {'description': "Go east", 'next_scene': 'scene3'}
    }
)

scene2 = Scene(
    description="You reach a river. You can swim across or follow the river.",
    options={
        '1': {'description': "Swim across", 'next_scene': 'scene4'},
        '2': {'description': "Follow the river", 'next_scene': 'scene5'}
    }
)

scene3 = Scene(
    description="You find a cave. It's dark inside.",
    options={
        '1': {'description': "Enter the cave", 'next_scene': 'scene6'},
        '2': {'description': "Return to the forest", 'next_scene': 'scene1'}
    }
)

# Map scene names to scene objects
scenes = {
    'scene1': scene1,
    'scene2': scene2,
    'scene3': scene3
}

# Start the game at scene 1
current_scene = 'scene1'

# Main game loop
while current_scene:
    scene = scenes[current_scene]
    scene.display_scene()
    choice = input("Choose an option: ")
    next_scene = scene.choose_option(choice)
    if next_scene:
        current_scene = next_scene
    else:
        current_scene = 'scene1'  # You can change this to re-prompt or handle differently
