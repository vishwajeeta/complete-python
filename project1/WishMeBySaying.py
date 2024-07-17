import time

now=time.strftime("%H")
now=int(now)
now=24
if(now <12 and now >1):
    print("good morning boss")
elif(now >=12 and now <18):
    print("good afternoon boss")
elif(now >=18 and now <=23):
    print("good night boss")
else:
    print("good day boss")