n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not prime.")
else:
    test = 2
    while test * test <= n:
        if n % test == 0:
            print(f"{n} is not prime.")
            break
        test += 1
    else:
        print(f"{n} is prime.")
