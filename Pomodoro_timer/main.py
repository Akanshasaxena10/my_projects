import time
import os

def convert(t):##function
    return t * 60

def countdown(t,label):##function
    #60
    while t:
        min, sec =divmod(t,60)###builtin function to give minutes and seconds.
        print(f"{label}: {min:02d}:{sec:02d}",end="\r")##t // 60 then t  % 60
        time.sleep(1)
        t -= 1

def pomodoro(work,rest):##function
    ##convert min to seconds
    w = convert(work)
    r = convert(rest)
    countdown(w,"Work-Time")
    os.system("clear")
    countdown(r,"Break-Time")
    os.system("clear")



work = int(input("Enter Work-Time (minutes): "))
rest = int(input("Enter Break-Time(minutes): "))
print(work)
print(rest)
pomodoro(work,rest) 