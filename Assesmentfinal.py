import os # Importing the os module
os.system("clear") # Clearing the terminal screen
from time import sleep # Importing the sleep function from the time module

speed = float(input("Before we get started, what speed would you like to play at (enter the amount of seconds you want between each letter): ")) # Asking the user for the speed they want to play at

def print_slow(txt): # Defining a function to print text slowly
    for x in txt:
        print(x, end='', flush=True)
        sleep(speed)
    print()


# Inventory system
inventory = []  # List to hold items
total_weight = 0  # Total weight of items in the inventory
MAX_WEIGHT = 10  # Maximum weight the player can carry

# Function to add item to inventory
def add_to_inventory(item, weight):
    global total_weight
    if total_weight + weight <= MAX_WEIGHT:
        inventory.append(item)
        total_weight += weight
        print_slow(f"You added {item} to your inventory.")
    else:
        print_slow("You can't carry that much! Your inventory is full.")

# Function to define what happens when the player enters the game
def intro():
    print_slow("Welcome to Kai's Amazing IST adventure!")
    print_slow("There will be lots of problems facing your way.")
    print_slow("You're going to need to try your hardest to survive.")
    print_slow("This is serious.")
    print_slow("But before you go in, I have a message for you.")
    print_slow("Pretty please give me a good mark.")
    print_slow("***********************")

# Function to ask the first question to start the game
def fav_student():
    fav = input("Am I your favourite student, and because of that you will give me a really good mark?\n"
                "Also, this is legally binding according to the Electronics Transactions Act 1999 Part 2 Section 8-11.\n"
                "So if you answer yes, that means you have to admit I'm your favourite,\n"
                "Also a 'really good mark' is 90 percent and above so I need higher than a 90 percent\n"
                "(yes/no): ").lower()
    return fav

# Function which gives a diffrent output based if the input is odd or even
def choose_clue(number):
    if number % 2 == 0:
        return "You enter a high-tech room. The walls are covered with screens displaying code. A giant security door stands ahead."
    else: 
        return "You step into a dark room filled with flickering monitors. The air is stale, and you hear whispers from the shadows..."

# Function to allow the user to choose between two portals
def choose_portal():
    print_slow("***********************")
    portal = input("You see two glowing portals ahead. One is pulsing with **purple energy**, the other with a **green mist**.\n"
                   "Which portal do you enter? (purple/green): ").lower()
    return portal

# Function to handle the first scenario: Laser Maze with three options to choose from and what happens based on the choice
def laser_maze():
    print_slow("You step into a long hallway filled with moving security lasers.")
    print_slow("You'll need to either **duck**, **jump**, or **run through** at the right time.")
    move = input("What do you do? (duck/jump/run): ").lower()

    if move == "duck":
        print_slow("You slide under the lasers successfully!")
    elif move == "jump":
        print_slow("You mistime your jump... The lasers zap you! Game Over.")
        exit()
    elif move == "run":
        print_slow("You sprint through perfectly, avoiding the lasers!")
    else:
        print_slow("You hesitate and the lasers cut you down. Game Over.")
        exit()

# Function to handle the second scenario: Decryption Puzzle with a code to enter and what happens based on the code
def decryption_puzzle():
    print_slow("You find a locked vault containing secret files.")
    print_slow("There's a keypad. The hint says: 'The first 3 prime numbers multiplied together.'")
    code = input("Enter the 3-digit code: ")

    if code == "30":  # 2 * 3 * 5 = 30
        print_slow("The vault unlocks! You grab the files and move on.")
    else:
        print_slow("Wrong code! The alarm triggers. Guards rush in. Game Over.")
        exit()

# Function to handle the third scenario: High-Speed Chase with two options to choose from
def high_speed_chase():
    print_slow("You're spotted by security drones! You jump onto a futuristic bike and speed away.")
    print_slow("Do you take the **fast route** (direct but risky) or **stealth route** (longer but safer)?")
    choice = input("(fast/stealth): ").lower()

    if choice == "fast":
        print_slow("You dodge obstacles at high speed, barely making it out alive!")
    elif choice == "stealth":
        print_slow("You sneak through back alleys and safely escape.")
    else:
        print_slow("You crash into a wall. Game Over.")
        exit()

# Function to handle the fourth scenario: Encounter Enemy with two options to choose from
def encounter_enemy():
    print_slow("A robotic guard spots you!")
    action = input("Do you **fight** or **hide**? (fight/hide): ").lower()

    if action == "fight":
        print_slow("You engage in combat and disable the robot with an EMP!")
    elif action == "hide":
        print_slow("You slip into the shadows and avoid detection.")
    else:
        print_slow("You freeze... The robot captures you. Game Over.")
        exit()

# Function to handle the hacking method choice with 4 options to choose from
def hacking_method():
    print_slow("Choose your hacking method:")
    print_slow("1. Brute Force Attack")
    print_slow("2. Social Engineering")
    print_slow("3. SQL Injection")
    print_slow("4. DDoS Attack")
    choice = input("Enter the number of your method(1/2/3/4): ")

    responses = { # Dictionary to store the responses based on the choice
        "1": "You attempt a brute force attack, but the security is too strong!",
        "2": "You trick an employee into giving you access codes!",
        "3": "You inject malicious SQL commands and gain access to the database!",
        "4": "Your DDoS attack slows down the hackers, but they are still active!"
    }

    return responses.get(choice, "Invalid choice, but let's move forward anyway!")

# Function to allow the user to choose a weapon and add it to the inventory
def choose_weapon():
    print_slow("You find three weapons:")
    print_slow("1. A high-voltage Taser (2 kg)")
    print_slow("2. A futuristic Laser Pistol (3 kg)")
    print_slow("3. A mysterious Energy Blade (4 kg)")
    weapon = input("Which weapon do you take? (1/2/3): ")

    # Add the chosen weapon to the inventory
    if weapon == "1":
        add_to_inventory("Taser", 2)
    elif weapon == "2":
        add_to_inventory("Laser Pistol", 3)
    elif weapon == "3":
        add_to_inventory("Energy Blade", 4)
    else:
        print_slow("You fumble around and pick up a random rock instead...")

# Function to handle the unexpected betrayal scenario with two options to choose from
def betrayal():
    print_slow("***********************")
    print_slow("Your supposed **ally** turns against you!")
    betrayal_choice = input("Do you **fight** them or **try to reason**? (fight/reason): ").lower()

    if betrayal_choice == "fight":
        print_slow("You engage in a tense battle and barely come out victorious.")
    elif betrayal_choice == "reason":
        print_slow("You manage to convince them to help you instead.")
    else:
        print_slow("You hesitate... and they take you out. Game Over.")
        exit()

# Function to handle the final confrontation with two options to choose from
def final_confrontation():
    print_slow("***********************")
    print_slow("You find yourself face-to-face with the hacker mastermind.")
    print_slow("A fierce cyber battle ensues...")
    print_slow("You can either:")
    print_slow("1. Use a virus to destroy their system.")
    print_slow("2. Challenge them to a hacking duel.")

    final_choice = input("Enter your choice (1/2): ")

    if final_choice == "1":
        print_slow("You unleash a powerful virus, wiping their data completely. The hacker mastermind is defeated!")
    elif final_choice == "2":
        print_slow("You engage in a legendary hacking duel... and emerge victorious!")
    else:
        print_slow("You hesitate... The hacker takes over. Game Over.")
        exit()

    print_slow("***********************")
    print_slow("Congratulations! You have beaten the game. Don't forget the legally binding agreement! :)")

# Print player's inventory at the end
def print_inventory():
    print_slow("***********************")
    print_slow("Your inventory includes:")
    if inventory:
        for item in inventory:
            print_slow(f"- {item}")
        print_slow(f"Total weight: {total_weight} kg")
    else:
        print_slow("Your inventory is empty.")
    print_slow("***********************")

# Main game function
def play_game():
    intro()
    if fav_student() == "no":
        print_slow("Wrong choice, you die!")
        exit()
    
    print_slow("***********************")
    number = int(input("You roll a dice to determine which door you enter. What number do you roll? "))
    print(choose_clue(number))

    portal = choose_portal()
    laser_maze()
    decryption_puzzle()
    high_speed_chase()
    encounter_enemy()
    print(hacking_method())
    choose_weapon()
    betrayal()
    final_confrontation()
    print_inventory()
