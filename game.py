####### Rock Paper Siccors #######
####### by WasHeisstKnock #######
#######       v1.0       #######
###############################

import random

wanna_play = input("Hi, would you like to play the guessing game? (Enter Y/N) ")

while wanna_play == "Y":

    if wanna_play == "N":
        print("Have a nice Day")
        break
    choosed = input("Choose [R]ock [P]aper [S]iccors: ")
    choosed_game = random.choices(["Rock", "Paper", "Siccors"])
    ## ROCK
    if choosed == "Rock" and choosed_game[0][0] == "Paper":
        print("You lost :(")
        wanna_play = input("Wanna play again? Y/N")
        break
    elif choosed == "Rock" and choosed_game[0] == "Rock":
        print("Tied!")
        wanna_play = input("Wanna play again? Y/N")
        break
    elif choosed == "Rock" and choosed_game[0] == "Siccors":
        print("You won :)")
        wanna_play = input("Wanna play again? Y/N")
    
    ## PAPER
    if choosed == "Paper" and choosed_game[0] == "Paper":
        print("Tied!")
        wanna_play = input("Wanna play again? Y/N")
        break
    elif choosed == "Paper" and choosed_game[0] == "Rock":
        print("You won :)")
        wanna_play = input("Wanna play again? Y/N")
    elif choosed == "Paper" and choosed_game[0] == "Siccors":
        print("You lost :(")
        wanna_play = input("Wanna play again? Y/N")
        break
    
    ## SICCORS
    if choosed == "Siccors" and choosed_game[0] == "Paper":
        print("You won :)")
        wanna_play = input("Wanna play again? Y/N")
    elif choosed == "Siccors" and choosed_game[0] == "Rock":
        print("You lost :(")
        wanna_play = input("Wanna play again? Y/N")
        break
        
    elif choosed == "Siccors" and choosed_game[0] == "Siccors":
        print("Tied!")
        wanna_play = input("Wanna play again? Y/N")
        break

