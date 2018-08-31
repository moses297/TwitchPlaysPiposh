import psutil
from time import sleep
from os import system

is_running = False

while True:
    is_running = False
    for p in psutil.process_iter():
        if "piposh" in p.name().lower():
            is_running = True
    if not is_running:
        print "starting Piposh"
        system("piposh.exe")
    sleep(30)