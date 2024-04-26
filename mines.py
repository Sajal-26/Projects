import random

li = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]

def display():
    for i in li:
        for j in i:
            print(j, end='  ')
        print()

def edit(c, C):
    for i in li:
        if c in i:
            i[i.index(c)] = C
            break

def mine(m):
    l = []
    while len(l) < m:
        r = random.randint(1,25)
        if r not in l:
            l.append(r)
    l.sort()
    return l

def mines(amt, m):
    a = amt
    l = mine(m)
    points = [1.1, 1.3, 1.5, 1.7, 2, 2.4, 2.9, 3.8, 4.6, 5.5, 6.2, 7, 7.8, 9, 10.2, 11.4, 12.7, 14, 17.3, 19.2, 20.8, 22, 23.6, 25]
    i = m - 1
    chance = 0
    display()
    while(True):
        if chance + m == 25:
            break
        chance += 1;
        c = int(input('Enter your choice : '))
        if c in l:
            for i in l:
                edit(i, 'B')
            print('0x')
            amt *= 0
            display()
            break
        if c == 0:
            for i in l:
                edit(i, 'B')
            display()
            break
        edit(c, 'M')
        amt = a
        amt *= points[i];
        i += 1 if i < len(points) else 0
        print('Amount : ',amt, ' - ', points[i-1],'x')
        display()
    return amt

if __name__ == '__main__':
    am = int(input('Enter your amount : '))
    m = int(input('Enter the number of mines : '))
    if 0 > m or m > 24:
        print('Out of bound')
        exit()
    a = mines(am, m)
    print('Final Amount : ', a)
    if am != 0 or a != 0:
        print(a/am, 'x') 