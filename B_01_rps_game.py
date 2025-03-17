# Check that user have entered a valid
# Option based on a list

def string_checker(question, valid_ans=('yes', 'no')):
    """Checks users enter and answer from a list"""

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does enter something that is valid
        print(error)
        print()


# Displays instructions

def instructions():
    print('''

*** Instructions ***

To begin, choose the number of rounds (or to play infinite mode, press <enter>)

Then play against the computer. You need to choose either R (Rock), P (Paper), or S (Scissors)

The rules are as follows:
Paper beats Rock
Rock beats Scissors
Scissors beats Paper

If, for example, the computer picks Rock, then you pick Paper, the computer wins

Press <xxx> to end the game

Good Luck
''')

def int_check(question):
    """Checks for an integer more than zero / <enter> for infinite"""
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
            # check that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissor", "xxx"]

print()
print("Welcome to the Rock🪨/Paper📃/Scissors✂️ Game")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions?")
print()

# display the instructions if user wants to see them
if want_instructions == "yes":
    instructions()


# Ask user for number of rounds / infinite
num_rounds = int_check("How many rounds would you like? push <enter> for infinite: ")
print()
print(f"you chose: {num_rounds}")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop stats here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print(f"you chose", user_choice)

    # if user choice is exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here


# game history
