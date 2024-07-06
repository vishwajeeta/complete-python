import pyttsx3
import random

a=["master","vishwa","boss"]

user=random.choice(a)

engine=pyttsx3.init()
engine.say(f"hello {user} , hope you have a good day.")

engine.runAndWait()

user_input=input("what you want to listen:")
engine.say(user_input)
engine.runAndWait()