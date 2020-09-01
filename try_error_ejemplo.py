print("how many cats do you have")
numCats = input()
try:
    if int(numCats) < 0:
        print("error: you enter a negative number")
    else:
        if int(numCats) >=4:
            print("that a lot of cats.")
        else:
            print("that is not that many cats.")
except ValueError:
    print("you didnt enter a number.")



    
