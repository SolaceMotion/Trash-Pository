import random

isRunning = True

while isRunning == True:
    print("")
    print("Type the number that represents the hand you wish to play")
    print("Type 'q' to quit")
    print("----------------")
    print("1. rock")
    print("2. paper")
    print("3. scissors")

    rps_items = ["rock", "paper", "scissors"]

    choice = input()
    randomized = random.choice(rps_items)

    if choice == "1":
        print("you chose rock")
        print("the computer chose", randomized)
        
        if randomized == "rock":
            print("tie")
        elif randomized == "paper":
            print("the computer won the round")
        elif randomized == "scissors":
            print("you won the round")

    if choice == "2":
        print("you chose paper")
        print("the computer chose", randomized)
        
        if randomized == "paper":
            print("tie")
        elif randomized == "scissors":
            print("the computer won the round")
        elif randomized == "rock":
            print("you won the round")
    
    if choice == "3":
        print("you chose scissors")
        print("the computer chose", randomized)
        
        if randomized == "scissors":
            print("tie")
        elif randomized == "rock":
            print("the computer won the round")
        elif randomized == "paper":
            print("you won the round")

    
    elif choice != "1" and choice != "2" and choice != "3" and choice != "q":
        print("Input wasn't valid")

    elif choice == "q":
        isRunning = False # break
