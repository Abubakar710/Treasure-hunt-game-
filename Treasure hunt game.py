print(" WELCOME TO THE GAME ")
name = input(" Please enter the name ")
game_rum_time=1
while(game_rum_time<=2):
    print(" welcome to the game of the teasurehunt lets check how good decision u can make to win the game ")
    print(" where do u want to go right and left ")
    tin = input(" please enter the R for right and L for the left ")
    if tin == "R":
        print(" sorry the game is over ")
    elif tin == "L":
        swim = input(" what would u like to do \n swim=S or wait for a \n while=W \n")
        if swim == "S":
            print(" sorry game is over ")
        elif swim == "W":
            door = input(
                " congro! u are at the last stage now which door u want to take \nRed=R \nGreen=G \nYellow=Y \n ")
            if door == " R ":
                print(" sorry the game is over ")
            elif door == "Y":
                print(" sorry u lost the game ")
            else:
                print(" congratulation u won the game ")
                break
if game_rum_time>2:
    print(" u rae out of the game ")



