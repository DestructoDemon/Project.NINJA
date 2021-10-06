import random
ans = "y"
usercount = 0
compcount = 0
while ans == "y":
    userchoice = input("Stone, Paper or Scissors? : ").lower()
    compchoice = ["stone","paper","scissors"]
    x = random.choice(compchoice)
    print("")
    print("You chose: ",userchoice)
    print("")
    print("computer chose: ",x)
    if (userchoice == "stone"):
        if (x == "scissors"):
            usercount += 1
            print("You WON!")
            print("")
        elif (x == "stone"):
            print("Its a TIE!")
            print("")
        else:
            compcount += 1
            print("You LOSE!")
            print("")
    elif (userchoice == "paper"):
        if (x == "stone"):
            usercount += 1
            print("You WON!")
            print("")
        elif (x == "paper"):
            print("Its a TIE!")
            print("")
        else:
            compcount += 1
            print("You LOSE!")
            print("")
    else:
        if (x == "paper"):
            usercount += 1
            print("You WON!")
            print("")
        elif (x == "scissors"):
            print("Its a TIE!")
            print("")
        else:
            compcount += 1
            print("You LOSE!")
            print("")
    ans = input("Do you want to play again? (y/n): ")
else:
    print("")
    print("Your score ",usercount," Computer score ",compcount, end = ",")
