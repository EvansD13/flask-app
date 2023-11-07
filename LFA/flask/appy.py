from termcolor import colored
import sys
import time
import application

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()





"""
while 1:
    sys.stdout.write(colored(next(spinner), "yellow"))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
"""

## Create the Server
## Add a listener
## Run the server