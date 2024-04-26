def printBoard(x, o):
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (9):
        c[i] = 'X' if x[i] else 'O' if o[i] else '_' # type: ignore
    print(f" {c[0]} | {c[1]} | {c[2]}")
    print(f"---|---|--")
    print(f" {c[3]} | {c[4]} | {c[5]}")
    print(f"---|---|--")
    print(f" {c[6]} | {c[7]} | {c[8]}")

sum = lambda a, b, c : a + b + c

def chkwin(x, o):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(x[win[0]], x[win[1]], x[win[2]]) == 3):
            print("X won!")
            return 1
        if(sum(o[win[0]], o[win[1]], o[win[2]]) == 3):
            print("O won!")
            return 0
    return -1 

def isDraw(x, o):
    for i in range(9):
        if x[i] == o[i]:
            return False
    return True

if __name__ == "__main__":
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = True
    print("-------Welcome To Tik Tak Toe Game-------")
    printBoard(x, o)
    while True:
        if turn:
            c = int(input("X's Turn : "))
            if not o[c-1]:
                x[c-1] = 1
            else:
                print("That's the position of \'O\'.....Try Again!")
                continue
        else:
            c = int(input("O's Turn :"))
            if not x[c-1]:
                o[c-1] = 1
            else:
                print("That's the position of \'X\'.....Try Again!")
                continue
        if chkwin(x, o) != -1:
            print("Match Over!")
            break;
        if isDraw(x, o):
            print("Draw!")
            break
        turn = not turn
        printBoard(x, o)
        print()
        