import requests, random

class Hungman:

    def __init__(self):
        word = requests.get("https://randomwordgenerator.com/json/words.json").json()["data"][random.randint(0, 3253)]["word"]
        try:
            hint = [requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()[0]['meanings'][0]['definitions'][0]['definition'], requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()[0]['meanings'][0]['definitions'][1]['definition'], requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()[0]['meanings'][0]['definitions'][2]['definition']]
        except:
            print('Some error occured!')
            exit()
        self.new = {word : hint}
        self.display = "_"*len(word)
        self.hint = []
    
    def chk(self,st):
        if st in self.hint:
            return False
        self.hint.append(st)
        return True

    def game(self, n = 3):
        w = next(iter(self.new))
        h = list(self.new[w])

        if not '_' in self.display:
            print("Word : ", self.display)
            print("Congratulations! You guessed the word!")
            exit()
        
        if self.chk(h[n-1]):
            print("Hint : ", h[n-1])

        t = n
        print("Word : ", self.display)
        l = (input("Enter a guess : ")).lower()

        if l in w:
            for i, c in enumerate(w):
                if c == l:
                    self.display = self.display[:i] + l + self.display[i+1:]
            self.game(t)

        else:
            if n == 1:
                print("Oops! You can't guess the correct word!\nThe correct word was :", w)
                exit()
            
            ch = ''
            while ch != 'y' or 'n':
                ch = input("Do you want the next hint?(y/n) : ")
                if ch == 'y':
                    t -= 1
                    self.game(t)
                elif ch == 'n':
                    self.game(t)
                else:
                    print("You entered the wrong option!")

if __name__ == "__main__":
    Hungman().game()