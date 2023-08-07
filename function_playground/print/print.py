# len() test
sentence = ("I hope you are having a great day learning Python")

print(len(sentence))

# Multi line test
multi_line_string = """Holly molly guackamole
Bila je velika vrucina
Sparina je bila
Nije se moglo igrat""".title().swapcase()

print(multi_line_string)

# strip(), capitalize() test
"""first_name = input("What is your first name? ").strip().capitalize()
last_name = input("What is your last name? ").strip().capitalize()
divider = " "
full_name = (first_name + divider + last_name)

print(full_name)
"""

# split() test

first_name, last_name = input("what is your name? ").capitalize().split(" ")


print("Hello", first_name)
