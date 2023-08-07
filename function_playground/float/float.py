# Float test

x = float(input("What's X? "))
y = float(input("What's Y? "))

# , 4 rounds to the 4th decimal point
result = round(x / y, 4)

# f string needs to be used if we want to add a separator on the 1,000 number, float dot is not affected
print(f"{result:,}")
