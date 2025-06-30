number = int(input("Enter a number: "))

if number > 50:
    print("The number is greater than 50")
    if number % 2 == 0:
        print("It's an even number")
    else:
        print("It's a odd number")
else:
    print("number is lesser than 50")