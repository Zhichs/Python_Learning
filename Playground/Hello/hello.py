def ask_name():
    name = input("What's your name? ").strip().title()
    print(f"Hello, {name}", end="!")

def main():

    ask_name()

main()