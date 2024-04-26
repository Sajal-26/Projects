import random

player = computer = 0

l = ['rock', 'paper', 'ssr']

while player + computer != 10:
    cmp = "".join(random.choice(l))
    ch = input("Choose from 'rock' 'paper' or 'ssr' : ")
    if ch == cmp:
        print("Same")
    elif (ch == 'rock' and cmp == 'paper') or (ch == 'paper' and cmp == 'ssr') or (ch == 'ssr' and cmp == 'rock'):
        computer += 1
        print(f"Computer choosed {cmp}")
        print(f"Computer : {computer}")
        print(f"Player   : {player}")
    elif (cmp == 'rock' and ch == 'paper') or (cmp == 'paper' and ch == 'ssr') or (cmp == 'ssr' and ch == 'rock'):
        player += 1
        print(f"Computer choosed \'{cmp}\'")
        print(f"Computer : {computer}")
        print(f"Player   : {player}")
    else:
        print("Wrong Choice!")
    
print("Final points : ")
print(f"Computer : {computer}")
print(f"Player   : {player}")
print("Player won!") if player > computer else print("Draw!") if player == computer else print ("Computer won!")