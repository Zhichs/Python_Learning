def main():
    user_input = int(input("What is the number? "))
    # If user_input after the operation in `def is_even()` returns True, then print "Even"is_even
    if is_even(user_input):
        print("Even")
    # Else print Odd
    else:
        print("Odd")
    
def is_even(n):
    
# * Retrun True if remainder of N is equal to 0 else return False
    return True if n % 2 == 0 else False

main()