
def script():
    # Function for running calculator
    def print_factors(x):
        print("The factors of", x, "are:")
        for i in range(1, x + 1):
            if x % i == 0:
                print(i)

    num_input = input('What number would you like to factor? ')
    num_input_converted = (int(num_input))
    print_factors(num_input_converted)

    # Restart Switch
    restart = input("Would you like to restart this program? ")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Thank you for using my calculator, goodbye!")
script()
