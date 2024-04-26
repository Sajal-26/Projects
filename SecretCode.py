import random

rnd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./?@#$%&!"

def encode(c):
    c = c.split(" ")
    encoded = ""
    for i in c:
        if len(i) < 3:
            encoded += i[::-1] + " "
        else:
            encoded += "".join(random.choice(rnd) for _ in range(3)) + i[1:] + i[0] + "".join(random.choice(rnd) for _ in range(3)) + " "
    return encoded

def decode(c):
    c = c.split()
    decoded = ""
    for i in c:
        if len(i) < 3:
            decoded += i[::-1] + " "
        else:
            decoded += i[-4] + i[3:-4] +  " "
    return decoded

def main(chs):
    ch = input("Enter : ")
    match chs : 
        case 1:
            return encode(ch)
        case 2:
            return decode(ch)
        case _:
            return "xyz"

if __name__ == "__main__":
    print("1. Encoding\n2. Decoding")
    ch = int(input("Enter your choice : "))
    result = main(ch)
    print("Wrong Choice!") if result == "xyz" else print("Result : ", result)