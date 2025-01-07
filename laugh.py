import random

def print_welcome():
    print("Welcome to the Hilarious Adventure Game!")
    print("Get ready to laugh your way through a series of zany challenges.\n")

def print_game():
    print("Instructions:")
    print("1. Type the number corresponding to your choice.")
    print("2. Have fun and enjoy the silliness\n")

def get_player():
    choice = input("Choose an option (1 or 2): ")
    while choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        choice = input("Choose an option (1 or 2): ")
    return choice

def cenario_1():
    print("\nYou encounter a dancing banana.")
    print("1. Join the dance.")
    print("2. Eat the banana.")
    choice = get_player()
    if choice == '1':
        print("You join the banana and have the time of your life")
    else:
        print("The banana turns out to be a magician and disappears in a puff of smoke")

def scenario_2():
    print("\nYou find a talking cat.")
    print("1. Have a chat with the cat.")
    print("2. Try to teach the cat to do your homework.")
    choice = get_player()
    if choice == '1':
        print("The cat tells you jokes that have you in stitches")
    else:
        print("The cat gives you a high-five and does your homework perfectl")

def play_game():
    print_welcome()
    print_game()
    scenarios = [cenario_1, scenario_2]
    random.choice(scenarios)()

play_game()
