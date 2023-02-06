#!/bin/python
import keyboard

STOP_KEY = False


def _return():
    global STOP_KEY
    print("Module stopped")
    STOP_KEY = True
    print("!!", STOP_KEY)
    return


def activate_stop_key():
    try:
        print("Push Ctrl + Shift + j  for stop this module or function")
        keyboard.add_hotkey("ctrl+shift+j", lambda: _return())

    except Exception:
        print("For STOP_KEY you need to run in root ")

