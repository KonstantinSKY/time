#!/bin/pyton

import time
from random import randint,  random, uniform
import keyboard

STOP_KEY = False


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def _return():
    global STOP_KEY
    print("Module stopped")
    STOP_KEY = True
    return


def rnd_sleep(start, finish):
    delay = uniform(start, finish)
    print("Delay for :  ", delay, " sec")

    try:
        print("Push Ctrl + Shift + j  for stop delay and exit function")
        keyboard.add_hotkey("ctrl+shift+j", lambda: _return())
    except Exception:
        print("For STOP_KEY you need to run in root ")

    while delay >= 1:
        if STOP_KEY:
            return
        time.sleep(1)
        delay -= 1
        print(delay, end='\r')


if __name__ == "__main__":
    rnd_sleep(10, 19)

#t = input("Enter the time in seconds: ")

#countdown(int(t))