import time
from torch import mode
import vlc
import gtts
import os
import google.generativeai as genai
import speech_recognition as sr

key = ""
genai.configure(api_key=key)

def speechreco() -> str:
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        try:
            audio = r.listen(source)
            prompt = r.recognize_google(audio)     # type: ignore
            print("Recognized:", prompt)
        except sr.UnknownValueError:
            prompt = 'bye'
            print("Could not understand audio")
        except sr.RequestError as e:
            prompt = 'bye'
            print("Could not request results from Google; {0}".format(e))
    
    return prompt

def prints(response: str) -> None:
    for i in response:
        print(i, end='')
        time.sleep(0.02)
    print()

def speech(response: str) -> None:
    s = gtts.gTTS(response, lang='en')
    try:
        s.save('res.mp3')
    except:
        os.remove(f'res.mp3')
        s.save('res.mp3')
    p = vlc.MediaPlayer(f'res.mp3')
    p.play()    # type: ignore

def config():
    generation_config = {
        "temperature": 0.05,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro-001",
        generation_config=generation_config, # type: ignore
        safety_settings=safety_settings
    )
    return model

def main():
    model = config()
    chat = model.start_chat()
    chat.send_message("You're an AI bot, your name is Jarvis, and you're here to answer all my questions as a personal assistant. My name is Sajal and I live in Kolkata, India")

    c = int(input('Enter 1 for text and 2 for voice : '))

    while True:
        prompt = ''
        if c == 1:
            prompt = input('User : ')
        
            if 'bye' in prompt.lower():
                response = 'Thank you, Nice talking to you! See you again'
            else:
                try:
                    response = chat.send_message(prompt).text
                
                except:
                    print('Some error Occured')

            print('AI : ', end='')
            prints(response)
        
        elif c == 2:
            prompt = speechreco()

            if 'bye' in prompt.lower():
                response = 'Thank you, Nice talking to you! See you again'
            else:
                try:
                    response = chat.send_message(prompt).text
                
                except:
                    print('Some error Occured')

            print('AI : ', end='')
            speech(response)
        
        else:
            prints(response='Wrong Choice!')
            exit()

        if 'bye' in prompt.lower():
            time.sleep(3)
            break

if __name__ == '__main__':
    main()
