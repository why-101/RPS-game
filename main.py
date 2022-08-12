# Intro
print("START")
print("use 'R' : rock\nuse 'S' : scissor\nuse 'P' : paper\nin this RPS Game\n")


def ret():
    # taking names from user
    a = input("User 1st please Enter your name: ")
    b = input("User 2nd please Enter your name: ")

    # store their objects with names
    c = str(input("{} please Enter your object: ".format(a)))
    d = str(input("{} please Enter your object: ".format(b)))
    e = str(input("You want result type : 'Y'\nor you want to quit  : 'Q'  \n    Enter            :  "))

    # start or quit
    if e == "y":
        if c == "r" and d == "s":
            print("{} You are the winner\n Congratulations...!".format(a))
        elif c == "s" and d == "p":
            print("{} You are the winner\n Congratulations...!".format(a))
        elif c == "p" and d == "r":
            print("{} You are the winner\n Congratulations...!".format(a))
        elif c == "s" and d == "r":
            print("{} You are the winner\n Congratulations...!".format(b))
        elif c == "p" and d == "s":
            print("{} You are the winner\n Congratulations...!".format(b))
        elif c == "r" and d == "p":
            print("{} You are the winner\n Congratulations...!".format(b))
        else:
            print("Invalid input..")
    elif e == "q":
        quit("Bye bye..")
    else:
        ret()
ret()
