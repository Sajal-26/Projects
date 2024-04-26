import time, requests, json, gtts, vlc, os

city = input("Enter the name of the city : ")
url = f"http://api.weatherapi.com/v1/current.json?key=08d6230a657040cc870162209233112&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
try:
    t = wdic["current"]["temp_c"]
    if t == int(t):
        t = int(t)
except:
    print("Wrong City!")
    exit()
    
print("Region         : ",wdic["location"]["region"])
print("Country        : ",wdic["location"]["country"])
print("Time           : ",wdic["location"]["localtime"])
print("Temperature(C) : ",wdic["current"]["temp_c"],"C")
print("Temperature(F) : ",wdic["current"]["temp_f"],"F")
print('Wind speed     : ',wdic['current']['wind_kph'],"Kmph")
print('Precipitation  : ',wdic['current']['precip_mm'],'mm')
print('Humidity       : ',wdic['current']['humidity'],'%')
uv = wdic['current']['uv']
print('UV             : ','Low' if 0 <= uv <=2 else 'Moderate' if 2 < uv < 6 else 'High' if 5 < uv < 8 else 'Very high' if 7 < uv < 11 else 'Extreme', f'({uv})')

speech = gtts.gTTS(f"The current weather in {city} is {t} degrees celsius", lang="en")
speech.save("try.mp3")
player = vlc.MediaPlayer('try.mp3')
player.play()  # type:ignore 

time.sleep(7)
os.system("del try.mp3")