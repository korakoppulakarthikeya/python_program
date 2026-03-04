import random
def dice():
    return random.randint(1,6)
snakes={
    78:69,
    82:45,
    67:14,
    32:9,
    16:4
}
ladders={
    6:64,
    18:37,
    48:76,
    83:99
}

player1= input("enter the name of the first player:").title()
player2 = input("enter player two name:").title()
print("BEST OF LUCK".center(30,'-'))
player1_score ,player2_score = 0,0
while True:
    if player1_score ==100 or player2_score ==100:
        break
    else:
        player1_choice = input("player 1 enter the choice to play(P)/quit(Q)").upper()
        if player1_choice == "P":
                roll = dice()
                
                curr_score1= player1_score+roll
                if  curr_score1<100:
                    if curr_score1 in snakes:
                        cuur_score1 = snakes[curr_score1]
                        print("snake bite🐍")
                        print(curr_score1)
                    elif curr_score1 in ladders:
                        curr_score1 = ladders[curr_score1]
                        print(f"{player1}you have climbed🪜")
                        print(curr_score1)
                    else:
                        curr_score1 = curr_score1
                        print(curr_score1)
                elif curr_score1==100:
                    print(f"The game is ended {player1} win")
                    break
                elif curr_score1 >100:
                    curr_score1 -= roll
        elif player1_choice == "Q":
            print(f"{player2} win the game")
            break
        player2_choice = input("player2 enter the choice to play(P)/quit(Q)").upper()
        if player2_choice == "P":
            roll = dice()
            print("rool:",roll)
            
            curr_score2= player2_score+roll
            if  curr_score2<100:
                if curr_score2 in snakes:
                    cuur_score2 = snakes[curr_score2]
                    print("snake bite🐍")
                    print(curr_score2)
                elif curr_score2 in ladders:
                    curr_score2 = ladders[curr_score2]
                    print(f"{player2}you have climbed🪜")
                    print(curr_score2)
                else:
                    curr_score2 = curr_score2
                    print(curr_score2)
            elif curr_score2==100:
                print(f"The game is ended {player2} win")
                break
            elif curr_score2>100:
                    curr_score1 -=roll
        elif player2_choice == "Q":
            print(f"{player1} win the game")
            break
