from random import randint
class card_game:
    DEBUG = True
    def __init__(self):
        self.pcards = 0
        self.cards = []
        self.type1 = "A"
        self.type2 = "8"
        self.hand1 = []
        self.hand2 = []
        self.hand3 = []
        self.playercount = 3
        self.card_count = 8
        self.opt1 = None
        self.opt2 = None
        self.opt3 = None
    def set_dif(self):
        dif = input("What difficulty would you like to select?")
        if dif == "e":
            self.pcards = 1
            self.card_count = 4
        if dif == "h":
            self.pcards = 2
            self.card_count = 8
    def set_suit(self):
        type1 = input("Enter the card you want to use: ")
        self.type1 = type1[0]
        type2 = input("Enter the card you want to use: ")
        self.type2 = type2[0]
    def play_game(self):
        self.set_dif()
        opta = input("Would you like to change the card type (y/n)? ")
        if opta == "y":
            self.set_suit()
        for i in range(self.card_count//2):
            self.cards.append(self.type1)
            self.cards.append(self.type2)
        print("Deck Created: ",self.cards)
        self.deal_cards()
        while self.hand1 != [] and self.hand2 != [] and self.hand3 != []:
            self.plrlogic()
        print("Game Over!")
    def deal_cards(self):
        for i in range(1,self.playercount+1):
            for j in range(self.pcards):
                cardindex = randint(0,len(self.cards)-1)
                hand = getattr(self,("hand"+str(i)))
                hand.append(self.cards[cardindex])
                self.cards.remove(self.cards[cardindex])
                if card_game.DEBUG: print(self.cards)
        print("Player 2s hand:",self.hand2,"\nPlayer 3s hand:",self.hand3)
    def plrlogic(self):
        opt = input("Pass or Name a card: (P,N): ").upper()
        if opt == "P":
            print("P1 - I'm going to pass,")
            self.opt1 = "P"
        else:
            print("Do not guess unless you know for certain")
            a = input('List one of your cards: ("XX" to pass)')
            if a == str(self.type1) or a == str(self.type2):
                if a == self.hand1[0] or a == self.hand1[1]:
                    if a == self.type1:
                        b = "1"
                    else:
                        b = "2"
                    print(f"P1 - I have an {a}")
                    self.hand1.remove(a)
                    self.opt1 = b
                    if self.hand1 == []:
                        return
            elif a == "XX":
                self.opt1 = "P"
                print("P1 - I'm going to pass,")
        if self.pcards == 1:
            self.ecpulogic(2)
            self.ecpulogic(3)
        elif self.pcards == 2:
            self.hcpulogic(2)
            self.hcpulogic(3)
    def hcpulogic(self,player):
        #Player 2, can view hand1 and 3.
        if player == 2:
            if self.hand1[0] == self.type1 and self.hand3[0] == self.type1 and (self.hand1[1] or self.hand3[1]) == self.type1: #
                if self.hand1[0] == self.type1 and self.hand3[0] == self.type1 and (self.hand1[1] and self.hand3[1]) == self.type1: #all 4 cards seen are A
                    print(f"P2 - I have 2 {self.type2}s!")
                    self.hand2 = []
                else:
                    print(f"P2 - I have a {self.type2}!") #3 A's seen, one must be an 8
                    self.hand2.remove(self.type2)
                    self.opt2 = "2"
            elif self.hand1[0] == self.type2 and self.hand3[0] == self.type2 and self.hand1[1] == self.type2 or self.hand3[1] == self.type2:
                if self.hand1[0] == self.type2 and self.hand3[0] == self.type2 and (self.hand1[1] == self.type1 and self.hand3[1]) == self.type2: #all 4 cards seen are 8
                    print(f"P2 - I have 2 {self.type1}s!")
                    self.hand2 = []
                else:
                    print(f"P2 - I have a {self.type1}!") #3 8's seen, one must be an A
                    self.hand2.remove(self.type1)
                    self.opt2 = "1"
            else:
                print("P2 - I'm going to pass")
    def ecpulogic(self,player):
        if player == 2:
            if self.hand1[0] == self.type1 and self.hand3[0] == self.type1:
                print(f"P2 - I have a {self.type2}!")
                self.hand2 = []
            elif self.hand1[0] == self.type2 and self.hand3[0] == self.type2:
                print(f"P2 - I have a {self.type1}!")
                self.hand2 = []
            elif self.hand3[0] == self.type1 and self.opt1 == "P":
                print(f"P2 - I have a {self.type2}!")
                self.hand2 = []
            elif self.hand3[0] == self.type2 and self.opt1 == "P":
                print(f"P2 - I have a {self.type1}!")
                self.hand2 = []
            else:
                print("P2 - I'm going to pass")
        if player == 3:
            if self.hand1[0] == self.type1 and self.hand2[0] == self.type1:
                print(f"P3 - I have a {self.type2}!")
                self.hand3 = []
            elif self.hand1[0] == self.type2 and self.hand2[0] == self.type2:
                print(f"P3 - I have a {self.type1}!")
                self.hand3 = []
            elif self.hand2[0] == self.type1 and self.opt1 == "P":
                print(f"P3 - I have a {self.type2}!")
                self.hand3 = []
            elif self.hand2[0] == self.type2 and self.opt1 == "P":
                print(f"P3 - I have a {self.type1}!")
                self.hand3 = []
            else:
                print("P3 - I'm going to pass")
def main():
    e = card_game()
    e.play_game()
main()