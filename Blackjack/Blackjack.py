import random


def main ():

    print("Welcome to the game of blackjack. Goal is to beat the dealer.\nIf your total is above 21 - you lose. If dealer has closer score to 21 - you lose.\n")

    play = True
    legitScore = True
    firstDecision = True
    splitMade = False
    handOne_tooMany = False
    handTwo_tooMany = False
    dealer_tooMany = False
    endOfGame = False
    tooMany = False
    dealer_bj = False
    player_bj = False

    cardDeck.shuffle()


    player = Hand(0, False,[])
    dealer = Hand(0, False,[])
    #cardDeck.deck[0] = 'A spades'
    #cardDeck.deck[2] = 'J spades'

    dealInitials(dealer, player)

    #player.total = 20
    #player.nominals = ['K hearts', 'J spades']
    print(player.nominals)

    print("Your score is " + str(player.total))

    
    while play:

        if player.total == 21:
            player_bj = True
            player.total == 22
            print('\nYou got a BlackJack!!!')
        if dealer.total == 21:
            dealer.total == 22
            dealer_bj = True

        if player_bj == False:
            while legitScore:
                if firstDecision:
                    if canSplit(player):
                        decision = input("\nWhat is your decision? (stand, hit or split)\n")
                        firstDecision = False
                    else:
                        decision = input("\nWhat is your decision? (stand or hit)\n")
                        firstDecision = False
                else:
                    decision = input("\nWhat is your decision? (stand or hit)\n")

                if decision == "hit":
                    player.hit()
                    print('\nYour hand: ' + str(player.nominals))

                    if player.total > 21:
                        tooMany = True
                        print("You lose(score > 21).")
                        legitScore = False
                    elif player.total == 21:
                        legitScore = False
                    else:
                        print("Your score is " + str(player.total))

                elif decision == 'stand':
                    legitScore = False
                    dealDealers(dealer)
                    endOfGame = True
                    #dealer.total = 22
                    if dealer.total > 21:
                        print('\nDealer busts.\n\n$$$$$$$$$$ Player wins with score of ' + str(player.total)  + ' $$$$$$$$$$')

                elif decision == 'split':

                    splitMade = True
                    legitScore = False
                    player2 = Hand(0,False,[])
                    player2.total = int(player.total / 2)
                    player2.nominals.append(player.nominals[1])
                    player.split()
                    player.hit()
                    player2.hit()
                    print('\nYou got two hands now')
                    doSplit(player,player2)
                    if player.total > 21:
                        handOne_tooMany = True
                    if player2.total > 21:
                       handTwo_tooMany = True
        
        if player.total == 21 and splitMade == False:
            dealDealers(dealer)
            endOfGame = True
            #dealer.total = 22
            if dealer.total > 21:
                dealer_tooMany = True
                print('\nDealer Busts.')
        if splitMade:
            if handOne_tooMany == False and handTwo_tooMany == False:
                dealDealers(dealer)
                endOfGame = True
                #dealer.total = 22
            if dealer.total > 21:
                dealer_tooMany = True
                print('\nDealer Busts.')

            if (handOne_tooMany and handTwo_tooMany):
                print('Dealer Wins')
            elif dealer_tooMany and handOne_tooMany == False and handTwo_tooMany == False:
                print('\n$$$$$$$$$$ Player wins with scores of ' + str(player.total)  + ' and ' + str(player2.total) + ' $$$$$$$$$$')

            elif dealer_tooMany and handOne_tooMany == False and handOne_tooMany:
                print('It is a push. Nobody winds. You get your money back.')

            elif dealer_tooMany and handOne_tooMany and handOne_tooMany == False:
                print('It is a push. Nobody winds. You get your money back.')

            elif player.total > dealer.total and player2.total > dealer.total:
                print('\n$$$$$$$$$$ Player wins with scores of ' + str(player.total)  + ' and ' + str(player2.total) + ' $$$$$$$$$$')

            elif player.total < dealer.total and player2.total > dealer.total:
                print('It is a push. Nobody winds. You get your money back.')

            elif player.total > dealer.total and player2.total < dealer.total:
                print('It is a push. Nobody winds. You get your money back.')

            elif player.total < dealer.total and player2.total < dealer.total:
                print('Dealer Wins')

        if player_bj:
            if player.total > dealer.total:
                print('\nYou won with blackjack. Congrulations!!')
            elif player.total == dealer.total:
                print('\nDealer hot blackjack as well. It is a push.')
        else:
            if dealer_bj:
                print('\nDealers hand: ' + str(dealer.nominals))
                print('Dealer wins with Blackjack')
            elif endOfGame and dealer.total > player.total:
                print('Dealer wins.')
            elif tooMany == False and endOfGame and player.total > dealer.total:
                print('\n$$$$$$$$$$ Player wins with score of ' + str(player.total) + ' $$$$$$$$$$')
            elif endOfGame and player.total == dealer.total:
                print('It is a push. Nobody wins. You get your money back.')


        yorn = input("\nTry again?(y or n) ")
        if yorn == "y":
           print('-------------------------------------------------')
           del dealer
           del player
           if splitMade:
            del player2
           firstDecision = True
           legitScore = True
           splitMade = False
           dealer_bj = False
           player_bj = False
           player = Hand(0, False,[])
           dealer = Hand(0, False,[])
           restart(dealer,player)
           
        else: 
             print('\nThank you for playing. Hope you had fun. See you next time. Goodbye!')
             play = False


def doSplit(player, player2):
    twoHands = True
    handOne = True
    handTwo = True
    handOne_tooMany = False

    while twoHands:
       print('Hand one: ' + str(player.nominals) + ' With score ' + str(player.total))
       print('Hand two: ' + str(player2.nominals) + ' With score ' + str(player2.total))

       while handOne:
           if player.total != 21:
            decision = input('\nWhat to do on hand one? (hit or stand) ')
            if decision == 'hit':
                player.hit()
                print('\nHand one: ' + str(player.nominals), end="")
                if player.total <= 21:
                    print(' With score ' + str(player.total))
                print('\nHand two: ' + str(player2.nominals) + ' With score ' + str(player2.total))
            elif decision == 'stand':
               handOne = False
           if player.total > 21:
               handOne_tooMany = True
               print('------------------')
               print('Hand one busts')
               print('------------------')
               handOne = False
           elif player.total == 21:
               handOne = False

       while handTwo:
           if player2.total != 21:
            decision = input('\nWhat to do on hand two? (hit or stand)')
            if decision == 'hit':

                player2.hit()
                print('\nHand one: ' + str(player.nominals), end = "")
                if handOne_tooMany == False:
                    print('With score ' + str(player.total))
                else:
                    print(' too many')
                print('\nHand two: ' + str(player2.nominals), end = "")
                if player2.total <= 21:
                    print(' With score ' + str(player2.total))

            elif decision == 'stand':
                handTwo = False
                twoHands = False
            if player2.total > 21:
                handTwo_tooMany = True
                print('\n------------------')
                print('Hand two busts')
                print('------------------\n')
                handTwo = False
                twoHands = False
            elif player.total == 21:
                handTwo = False
                twoHands = False

def restart(dealer,player):
    cardDeck.step = 0
    cardDeck.shuffle()
    dealInitials(dealer, player)
    print("Your score is " + str(player.total))

def dealDealers(dealer):

    needMore = False
    i = 1

    print('\nDealers hidden card is ' + str(dealer.nominals[1]))
    print('Dealers score is ' + str(dealer.total))

    if dealer.total < 17:
        needMore = True

    while needMore:
        dealer.hit()
        input('\n/Press any key to continue/\n')
        print('Dealer hits with ' + dealer.nominals[i+1])
        if dealer.total < 17:
            print('Dealers score is ' + str(dealer.total))
        i += 1
        if dealer.total >= 17 and dealer.total <= 21:
            needMore = False
            print('\nDealer stands on score of ' + str(dealer.total))
        elif dealer.total > 21:
            needMore = False


def canSplit(player):
    sep = " "
    card1 = player.nominals[0].split(sep, 1)[0]
    if card1 == 'J' or card1 == 'Q' or card1 == 'K' or card1 == 'A':
        card1 = 10
    card2 = player.nominals[1].split(sep, 1)[0]
    if card2 == 'J' or card2 == 'Q' or card2 == 'K' or card2 == 'A':
        card2 = 10

    if int(card1) == int(card2):
        return True
    else: 
        return False

    print(card1, card2)


def dealInitials(dealer, player):

    player.hit()
    dealer.hit()
    print("\nDealers open card is " + cardDeck.deck[cardDeck.step-1] + "\n")
    player.hit()
    dealer.hit()
    print("You got " + player.nominals[0] + " and " + player.nominals[1])


class cardDeck:

    step = 0
    deck = ["2 spades","2 clubs","2 hearts","2 diamonds",
            "3 spades","3 clubs","3 hearts","3 diamonds",
            "4 spades","4 clubs","4 hearts","4 diamonds",
            "5 spades","5 clubs","5 hearts","5 diamonds",
            "6 spades","6 clubs","6 hearts","6 diamonds",
            "7 spades","7 clubs","7 hearts","7 diamonds",
            "8 spades","8 clubs","8 hearts","8 diamonds",
            "9 spades","9 clubs","9 hearts","9 diamonds",
            "10 spades","10 clubs","10 hearts","10 diamonds",
            "J spades","J clubs","J hearts","J diamonds",
            "Q spades","Q clubs","Q hearts","Q diamonds",
            "K spades","K clubs","K hearts","K diamonds",
            "A spades","A clubs","A hearts","A diamonds"]

    def shuffle():
        random.shuffle(cardDeck.deck)

    def drawCard(step):

        sep = " "
        value = cardDeck.deck[step].split(sep, 1)[0]

        if value == "K" or value == "Q" or value == "J":
            value = 10
        elif value == "A":
            value = 11
        else: value = int(value)

        cardDeck.step = step + 1
        return value



class Hand:

    def __init__(self, total, hasAce, nominals):
        self.total = total
        self.hasAce = False
        self.nominals = []

    def hit(self):
        latestCard = cardDeck.drawCard(cardDeck.step)
        self.nominals.append(cardDeck.deck[cardDeck.step-1])
        if latestCard == 11:
            self.hasAce = True
        self.total = self.total + latestCard
        if self.total > 21 and self.hasAce:
            self.total = self.total - 10
            self.hasAce = False

    def split(self):
        self. total = int(self.total / 2)
        self.nominals.pop()


    









if __name__ == "__main__":
    main()