#!/bin/pyton

import time
from random import randint, random, uniform
import keyboard_events as ke


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def rnd_sleep(start, finish):
    delay = uniform(start, finish)
    print("Delay for :  ", delay, " sec")
    ke.activate_stop_key()
    while delay >= 1:
        if ke.STOP_KEY:
            return
        time.sleep(1)
        delay -= 1
        print(" ", delay, end='\r')


if __name__ == "__main__":
    rnd_sleep(10, 19)

#t = input("Enter the time in seconds: ")

#countdown(int(t))