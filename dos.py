#!/usr/bin/env python
# copy this script into the same directory as https://github.com/ECTO-1A/AppleJuice/
# more info: mobile.hacker.com

import subprocess as sp
import time

def runApp(number):
    extProc = sp.Popen(['python3', 'app.py', '-d', number])
    time.sleep(6)
    sp.Popen.terminate(extProc)

if __name__ == "__main__":
    app_numbers = list(map(str, range(1, 30)))  # Numbers 1 to 29
    for number in app_numbers:
        runApp(number)

"""
    1: "Airpods",
    2: "Airpods Pro",
    3: "Airpods Max",
    4: "Airpods Gen 2",
    5: "Airpods Gen 3",
    6: "Airpods Pro Gen 2",
    7: "PowerBeats",
    8: "PowerBeats Pro",
    9: "Beats Solo Pro",
    10: "Beats Studio Buds",
    11: "Beats Flex",
    12: "BeatsX",
    13: "Beats Solo3",
    14: "Beats Studio3",
    15: "Beats Studio Pro",
    16: "Beats Fit Pro",
    17: "Beats Studio Buds+",
    18: "AppleTV Setup",
    19: "AppleTV Pair",
    20: "AppleTV New User",
    21: "AppleTV AppleID Setup",
    22: "AppleTV Wireless Audio Sync",
    23: "AppleTV Homekit Setup",
    24: "AppleTV Keyboard",
    25: "AppleTV 'Connecting to Network'",
    26: "Homepod Setup",
    27: "Setup New Phone",
    28: "Transfer Number to New Phone",
    29: "TV Color Balance"
"""
