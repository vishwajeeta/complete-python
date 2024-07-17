import time
import pyttsx3

now=time.strftime("%H")
now=int(now)

if(now <12 and now >1):
    wish="good morning boss"
    print(wish)

elif(now >=12 and now <18):
    wish="good afternoon boss"
    print(wish)

elif(now >=18 and now <=23):
    wish="good night boss"
    print(wish)

else:
    wish="good day boss"
    print(wish)

engine=pyttsx3.init()

engine.say(wish)
engine.runAndWait()