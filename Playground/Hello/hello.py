# # Comment
# * Highlighted comment
# ! Alert/Warning 
# ? Question blue comment
# TODO To do list comment


def main():

    say_hello()


def say_hello():
    name = input("What is your name? ").strip().title()
    if not name:
        name = "User"
        
    print(f"Hello, {name}", end="!")

main()