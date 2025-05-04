git branch -M mainname= input("What is your name = ")
height= int(input("What is your height = "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age = "))
    if age <= 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets is $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Do you want to take any photo? Type y for Yes and n for No = ")
    if photo == "y":
        #Add #3 to their bill
        bill2 = bill + 3

    print(f"Your final bill is ${bill2}")

else:
    print("You cannot ride the rollercoaster.")