from random import randint

a = ["Rock", "Paper", "Scissors"]
machine = a[randint(0, 2)]

champion = False

while champion == False:
    champion = input("Rock, Paper, Scissors : ")
    if champion == machine:
        print("Match draw!")
    elif champion == "Rock":
        if machine == "Paper":
            print("Sorry!..Better luck next time", machine, "Winner is ", champion)
        else:
            print("Congratulations...You won!", machine, "You busted ", machine)
    elif champion == "Paper":
        if machine == "Scissors":
            print("Sorry!..Better luck next time", machine, champion, " is Celebrating")
        else:
            print("Congratulations...You won!", champion, "Winner is ", machine)
    elif champion == "Scissors":
        if machine == "Rock":
            print("Sorry!..Better luck next time", machine, "You lose ", champion)
        else:
            print("You win!", champion, "Ooops ", machine, " is feeling sad!!")
    else:
        print("An error occured!.....Try again")

    champion = False
    machine = a[randint(0, 2)]