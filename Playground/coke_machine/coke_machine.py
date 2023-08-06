# This function simulates a single transaction with the vending machine.
# It takes the number of drinks left in the machine and the leftover change from the last transaction as input.
def coke_machine(drinks_left, left_over_change):
    # If there are no drinks left, print a message and return zeroes.
    if drinks_left == 0:
        print("Sorry, the machine is out of drinks!")
        return 0, drinks_left
    else:
        # Set the amount due to be 50 minus the leftover change from the last transaction.
        amount_due = 50 - left_over_change
        print("Amount Due: ", amount_due)

        # Continue asking for coins until the amount due is paid.
        while amount_due > 0:
            coins_in = int(input("Insert Coin: "))
            if coins_in in [25, 10, 5]:  # If the coin is a valid denomination,
                amount_due -= coins_in  # subtract its value from the amount due,
                print("Amount Due: ", max(0, amount_due))  # and print the new amount due.
            else:  # If the coin is not a valid denomination,
                print("Invalid coin. Try again.")  # print an error message.

        # If the customer has overpaid, calculate how much change they're owed.
        change_owed = -amount_due
        if change_owed > 0:
            print("Change Owed: ", change_owed)
            while True:
                took_change = input("Press 'Y' to take your change, 'N' to leave it: ")
                if took_change.lower() in ['y', 'n']:  # If the customer has made a valid choice,
                    if took_change.lower() == 'y':  # and they choose to take their change,
                        left_over_change = 0  # no change is left over.
                    else:  # If they choose not to take their change,
                        left_over_change = change_owed  # the change owed is left over for the next customer.
                    break  # Break out of the loop asking if the customer wants their change.
                else:  # If the customer has not made a valid choice,
                    print("Invalid input. Please press 'Y' or 'N'.")  # print an error message.

        # Subtract one from the number of drinks left in the machine, since the customer has just bought a drink.
        drinks_left -= 1
        return left_over_change, drinks_left

# This is the main function, which controls the entire program.
def main():
    drinks_left = 4  # Set the initial number of drinks in the machine to 5.
    left_over_change = 0  # Set the initial amount of change left in the machine to 0.

    # Continue vending drinks until there are none left.
    while drinks_left > 0:
        # Perform a transaction and update the amount of change left over and the number of drinks left.
        left_over_change, drinks_left = coke_machine(drinks_left, left_over_change)
        # Print the amount of change left over and the number of drinks left.
        print("Change left over by previous customer: ", left_over_change)
        print("Drinks left: ", drinks_left)

# Call the main function to start the program.
main()
