small_pizza = input("What size pizza do you want? Enter S for Small, M for Medium, L for Large: ")
small_pepporoni = input("Do you want to add Pepporoni to your pizza? PLease enter Y for Yes and N for No? ")
cheese = input("Do you want to add extra cheese for any size pizza? PLease enter Y for Yes and N for No? ")

bill = 0
if small_pizza == "S":
    bill += 15
elif small_pizza == "M":
    bill += 20
elif small_pizza == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

if small_pepporoni == "Y":
    if small_pizza == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your bill is: {bill}")

