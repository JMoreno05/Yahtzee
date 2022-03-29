from _ast import Pass
from pylint.extensions.check_elif import ElseifUsedChecker
class scoreCard:
    """
    Records Yahtzee scores based off of choices and list of dice
    """
    def __init__(self, player):
        self.name = player
        self.upper=[0,0,0,0,0,0,0]
        self.lower=[0,0,0,0,0,0,0,0]
        self.totalUpper =0
        self.totalLower =0
        
    def printScoreCard(self):
        print("Next Player:", self.name,"\n")
        
        print("Upper Section")
        print("[1]s:", self.upper[0], "\t[2]s:", self.upper[1],
              "\t[3]s:", self.upper[2], "\t[4]s:", self.upper[3],
              "\t[5]s:", self.upper[4], "\t[6]s:", self.upper[5])
        upperScore = 0
        for i in self.upper:
            upperScore += i
        if self.upper[6] ==0 and upperScore >=63:
            self.upper[6] = 35
            upperScore +=35
        if self.upper[6] == 0:
            msg = str(63-upperScore) + "points until Upper Bonus"
        else:
            msg = "You have the Upper Bonus"
        print("Total Upper Score:", upperScore,"\t"+msg+"\n")
        
        print("Lower Section")
        print("[3k] 3 of a kind:", self.lower[0],"\t[4k] 4 of a kind:", self.lower[1])
        print("[S]mall Straight:", self.lower[2], "\t[L]arge Straight:", self.lower[3])
        print("[F]ull House:", self.lower[4], "\t[C]hance:", self.lower[5])
        print("Yaht[z]ee:", self.lower[6])
        print("Yahtzee [B]onus:", self.lower[7], "x 100 =", self.lower[7]*100)
        
        lowerScore = 0
        for i in self.lower:
            lowerScore += i
        print("Total Lower Score:", lowerScore)
        print("---------------------------------------------")
        print("Grand Total Score:", lowerScore + upperScore)    
      
    def confirmStraight(self,roll):       
        roll.sort()
        i=0
        count =0
        initialVal = roll[0]
        while i < len(roll):
            if roll[i] == initialVal:  
                print("same", roll[i])
                pass
            elif roll[i] ==initialVal+1:
                count +=1
                print("next in seq", initialVal, roll[i])
                initialVal = roll[i]                
            elif count <4:
                count = 0
                initialVal = roll[i]  
                print("not in seq")
            else:
                pass
            i+=1
        return (count+1)          
            
    def confirmYahtzee(self,roll):
        if roll.count(roll[0]) == 5:
            #confirmed
            if self.lower[5] == 0:
                self.lower[5] = 50
                print("You Scored your first Yahtzee!")
            else:
                print("Your scored a bonus Yahtzee!")
                self.lower[7]+=1
        else:
            print("That is not a Yahtzee.")
        
    def recordUpper(self, type, roll):
        """
        takes type (ones, twos, etc) and list of values rolled
        and records in correct spot
        """
        print(type)
        if self.upper[int(type)-1] == 0:
            value = int(type) * roll.count(int(type))
            self.upper[int(type)-1] = value
        else:
            print("Invalid option")
            
    def totalAllDice(self,roll):
        total = 0
        for die in roll:
            total += int(die)
        return total
    
            
    def recordScore(self, type, roll):
        type = type.lower()
        if int(type) < 7:
            print(type)
            if self.upper[int(type)-1] == 0:
                value = int(type) * roll.count(int(type))
                self.upper[int(type)-1] = value
            else:
                print("Invalid option")
                               
        else:
            if(type == '3k'):
                pass
            elif type == '4k':
                pass
            elif type == 'f':
                pass
            elif type =='s':
                if self.lower[2] !=0:
                    print("Small Straight is already recorded.")
                elif self.confirmStraight(roll) == 4:
                    self.lower[2] = 30
                    print("Scored a Small Straight:", self.lower[2])
            elif type =='l':
                pass 
            elif type == 'z':
                self.confirmYahtzee(roll) 
            elif type == 'c':
                if self.loer[6] != 0:
                    print("Chance Score already recorded")
                else
                    self.lower[6] = totalAllDice(roll)
                    print("Scored Chance:", self.lower[6])
            elif type =='b':
                self.confirmYahtzee(roll)
            
                
                
                
                
                