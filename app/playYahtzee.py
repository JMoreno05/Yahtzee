import random as rand
import sys
sys.path.append("..//classes")
from YahtzeeClass import scoreCard

def printWelcome():
    print("\t\tLets Play Yahtzee!")
    player1 = input("Enter a name for Player1: ")
    #player2 = input("Enter a name for Player2: ")
    
    print("Ready...GO!")
    return player1

def roll(dice):
    for i in range(0,5):
        dice.append(rand.randint(1,6))
def main():
    player1 = scoreCard(printWelcome())
    dice = []
    response='p'
    while response != 'q':
        player1.printScoreCard()
        response = input("Ready to Roll?? [y=yes q = quit]")
        if response.lower == "q":
            continue 
        roll(dice)
        dice.sort()
        print("You Rolled,", dice)
        player1.confirmStraight(dice)
        #type = input("Choose where to record your score (type text inside[]):")
        response = input("Ready to Roll?? [y=yes q = quit]")
        dice =[]
    
    player1.recordUpper(type, dice)
    print(player1.upper)
    player1.printScoreCard()

if __name__ == "__main__":
    main()