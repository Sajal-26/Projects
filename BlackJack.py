import random, time

points = {'A' : [1, 11], 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, 'J' : 10, 'Q' : 10, 'K' : 10}

cards = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]


def distributed() -> bool:
    ''''
        Check if all the cards are distributed or not
                '''
    for i in cards:
        if i != 0:
            return False
    return True

def distribute(n : int) -> list:
    '''
        Distribute the n number of cards to the player
    '''

    if n > 52 or n <= 0:            # Check if the input of n is withing the range of number of cards or not
        print('Invalid Amount Of Cards')
        return []

    if distributed():
        print('All Cards Have Been Distributed!')
        return []

    c = []      # List of distributed cards

    # Check the picked card and edit the deck by removing the picked card from the deck
    while len(c) < n:
        cr = random.choice(list(points))

        if isinstance(cr, str):

            if cr == 'A' and cards[0] > 0:
                c.append(cr)
                cards[0] -= 1

            elif cr == 'J' and cards[10] > 0:
                c.append(cr)
                cards[10] -= 1

            elif cr == 'Q' and cards[11] > 0:
                c.append(cr)
                cards[11] -= 1

            elif cr == 'K' and cards[12] > 0:
                c.append(cr)
                cards[12] -= 1

        elif isinstance(cr, int):

            if cards[cr - 1] > 0:
                c.append(cr)
                cards[cr - 1] -= 1
                
    return c 

def details(players : list, dealer = True) -> None:
    '''
        Print the cards and points of the players. If the dealer value is True, it will print all the cards of the dealer and if it is false, then it will print only the first card of the dealer
    '''
    print('Cards : ', end='')

    if not dealer:
        print(players[0][0])
        return
    
    for i in players[0]:
        print(i, end='   ')
    
    print()
    print('Points : ', players[1])

def calpoints(cards : list) -> int:
    '''
        Calculates the points based on the cards the player have, if they're having A, the points will be skipped and later asked by the user that if they want 11 or 1
    '''
    sum = 0
    for i in cards:
        if i != 'A':
            sum += points[i]
    return sum

def play(players : dict, player : int, a : int, dealer = False, point = []):
    '''
        Asks the user for their choice (H / S / A)
        The Dealer will automitically run their turn
    '''
    # If the points are already 21 or more, no need to play anymore
    if players[player][1] >= 21:
        return
    
    # if the points of the player is 10 and they are having A, A will atomatically by considered as 11
    if players[player][1] == 10 and 'A' in players[player][0]:
        players[player][1] += 11
        if player == 0:
            print(f'Dealer : ')
        else:
            print(f'Player {player} : ')
        print('A set to 11')
        details(players[player])
        return
    
    choice = ''
    while True:
        # If the choice is S (stand) or if the points of the player exceeds 21, it will terminate the player by checking if the player has any A or not, and if the player has A, 1 point will be added to the player's point
        if choice == 'S'or choice == 's' or players[player][1] >= 21:
            while a > 0:
                players[player][1] += 1
                a -= 1
                print('A : +1')
            details(players[player])
            break
        
        if player == 0:
            print('\nDealer : ')
        else:
            print(f'\nPlayer {player} : ')

        # Displaying the details of the player and ask for their choice
        details(players[player])

        # Dealer automatic play
        if player == 0:
            print("\nHit (H) / Stand (S) / Set A (A) : ", end='')
            if len(point) == 1 and point[0] == players[player][1] and players[player][1] < 17:
                choice = 'H'
            
            elif not dealer or ishighest(point, players[0][1]):
                choice = 'S'

            else:
                if players[player][1] < 17:
                    if 'A' in players[player][0] and players[player][1] < 11 and players[player][1] > 7 and a > 0:
                        choice = 'A'
                    else:
                        choice = 'H'
                
                else:
                    if 'A' in players[player][0] and a > 0:
                        choice = 'A'

                    elif players[player][1] == 20 and not ishighest(point, players[player][1]):
                        choice = 'S'
                        
                    else:
                        if len(point) == 1:
                            if not ishighest(point, players[0][1]):
                                if a > 0:
                                    choice = 'A'
                                else:
                                    choice = 'H'

                            else:
                                choice = 'S'
                        
                        else:
                            if ishighest(point, players[player][1]):
                                choice = 'S'

                            elif islowest(point, players[player][1]):
                                choice = 'H'

                            else:
                                choice = random.choice(['H', 'S'])

            time.sleep(4)  
            print(choice)
            time.sleep(2)

        else:
            choice = input("\nHit (H) / Stand (S) / Set A (A) : ")
            time.sleep(2)
        
        if choice == 'S' or choice == 's':
            while a > 0:
                players[player][1] += 1
                a -= 1
                print('A : +1')
            details(players[player])
            break

        elif (choice == 'A' or choice == 'a') and 'A' in players[player][0] and a > 0:
            a -= 1
            while True:
                if player == 0:
                    print('Enter the value of A (1/11) : ', end='')
                    if players[player][1] < 11:
                        n = 11
                    else:
                        n = 1
                    time.sleep(4)
                    print(n)
                    time.sleep(2)

                else:
                    n = int(input('Enter the value of A (1/11) : '))
                    time.sleep(2)

                if n == 1:
                    players[player][1] += 1
                    break
                elif n == 11:
                    players[player][1] += 11
                    break
                else:
                    print('Please Enter the correct value of A')

        elif (choice == 'A' or choice == 'a') and 'A' in players[player][0] and a == 0:
            print('You\'ve already set the value of A')
        
        elif (choice == 'A' or choice == 'a') and 'A' not in players[player][0]:
            print('You don\'t have A')

        elif choice == 'H' or choice == 'h':
            newcard = distribute(1)[0]
            if newcard == 'A':
                a += 1
                players[player][0].append(newcard)
            else:
                players[player][0].append(newcard)
                players[player][1] += points[newcard]
        
        else:
            print('Wrong choice!')

def shouldplay(point : list, p : int) -> bool:
    '''
        Check if the dealer should hit or not
    '''
    for i in point:
        if i < 22 and i > p:
            return True
    return False

def ishighest(point : list, dealer : int) -> bool:
    '''
        Check if the dealer has the highest points
    '''
    for i in point:
        if dealer < i and i < 22:
            return False
    return True

def islowest(point : list, dealer : int) -> bool:
    '''
        Check if the dealer has the lowest points
    '''
    for i in point:
        if dealer > i:
            return False
    return True


def start(n : int, p : list) -> None:
    '''
        Distributes the equal number of cards to the players and the dealer
        Input n = 2
        players = {
                      0 (Dealer) : [['A', 'J'] (Cards), [21] (Points)],
                      1 (Player 1) : [[9, 5] (Cards) , [14] (Points)],
                      2 (Player 2) : [['Q', 2] (Cards), [12] (Points)]
                  }
    '''

    players = {}

    # Distributes 2 cards at the starting and to each player
    for i in range(n+1):
        players[i] = [distribute(2)]
        point = [calpoints(players[i][0])]
        players[i].extend(point)

    # Display all the cards with points of each player and shows only one card of the dealer
    for i in range(n+1):
        print()
        if i == 0:
            print('Dealer : ')
            details(players[i], False)   

        else:
            print(f'Player {i} : ')
            details(players[i])
        
    print('__________________________')
    

    point = []

    # Turns of each player except the dealer
    for i in range(1, len(players)):
        a = 0
        
        for j in players[i][0]:
            if j == 'A':
                a += 1

        play(players, i, a)
        point.append(players[i][1])
        print('__________________________')

    # Turn of the dealer
    a = 0
    for i in players[0][0]:
        if i == 'A':
            a += 1
    chkval = shouldplay(point, players[0][1])
    play(players, 0, a, chkval, point)
    point.insert(0, players[0][1])

    print('__________________________')
    print(point)
    print('__________________________')

    p = calculate_points(point, p)

def calculate_points(point, p):
    '''
        Calculate the points after each match 
    '''
    dealer_score = point[0]

    for i in range(1, len(point)):
        player_score = point[i]

        if dealer_score > 21:
            p[i] += 1
            p[0] -= 1

        elif player_score > 21:
            p[i] -= 1
            p[0] += 1

        elif dealer_score > player_score: 
            p[i] -= 1
            p[0] += 1

        elif player_score > dealer_score: 
            p[i] += 1
            p[0] -= 1 

        else:  
            continue

    return p

def main():
    '''
        Main function of the game
    '''
    try:
        n = int(input('Enter the number of players : '))

    except(Exception):
        print('You Entered a wrong input!\nPlease try again later!')
        exit()

    if n > 6:
        print('Too Many Players!')
        exit()

    elif n < 1:
        print('Too Less Player!')
        exit()
    
    try:
        i = int(input('Enter the numeber of matches you want to play : '))

    except(Exception):
        print('You Entered a wrong input!\nPlease try again later!')
        exit()
        
    p = [0] * (n + 1) 

    for i in range(i):
        print(f'Round {i+1}')
        start(n, p)

        global cards;
        cards = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        print('Points : ')
        for i in range(len(p)):
            if i == 0:
                print('Dealer : ', p[i])
                continue

            print(f'Player {i} : ', p[i])

        print('______________________________')

    for i in range(1, len(p)):
        if p[i] > p[0] or p[i] < p[0]:
            break

        else:
            print('Draw')
            exit()
    
    for i in range(len(p)):
        if p[i] == max(p):
            if i == 0:
                print('Dealer Won')
                continue

            print(f'Player {i} Won')

if __name__ == '__main__':
    main()