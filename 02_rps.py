# checks users enter yes/no
def yes_no(question):
    """Checks user response to a question is yes ? no (y/n), returns 'yes or 'no"""

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("pick yes / no please")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win
    """)


def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "put in a number more than / equal to 13"

    while True:
        try:
            response = int(input("What is the game goal?"))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

