# https://youtu.be/PmlyJWTkULg?si=ztYyPDCsQtlbh0M4

import gtts, playsound, os
while(True):
    txt = input("Enter the txt : ")
    if txt == "q" or txt == "Q":
        gtts.gTTS("h, bye bye friend!", lang="en").save("try.mp3")
        playsound.playsound("try.mp3")
        os.system("del try.mp3")
        break
    gtts.gTTS("h,"+txt, lang="en").save("try.mp3")
    playsound.playsound("try.mp3")
    os.system("del try.mp3")