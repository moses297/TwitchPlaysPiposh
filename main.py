import twitch
import keypresser
import time
import os
import atexit
import json
run_time = time.time()
t = twitch.Twitch()
k = keypresser.Keypresser()

if not os.path.exists("creds.txt"):
    print   """
            Please create a json file with the following:
            {"username": "TWITCH_USERNAME", "oauth": "TWITCH_TOKEN"}
            """
    exit(-1)

def rerun():
    os.system("python main.py")
atexit.register(rerun)

#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/

with open("creds.txt", "r") as f:
    data = json.loads(f.read())
    twitch_username = data["username"]
    key = data["oauth"]
t.twitch_connect(twitch_username, key)
dictionary = {"settings":(50,5), "suitcase":(100,5),
              "exitsuitcase":(600,470),"fritzdoor": (130,250),
              "talk1": (569,463), "talk2": (570,425),
             "talk3": (570,390), "talk4": (570,360),
             "talk5": (570,325), "talk6": (570,294),
              "left": (10,420), "right":(630,420)
              }
#The main loop

while True:
    try:
        if (run_time + 900) < time.time():
            print run_time + 900
            print time.time()
            print "timed out"
            os.system("python main.py")
            exit(-1)
        #Check for new mesasages
        try:
            new_messages = t.twitch_recieve_messages()
        except Exception as e:
            print e
            print "Got IO error in internal exception"
            os.system("python main.py")
            exit(-1)
            continue

        if not new_messages:
            #No new messages...
            continue
        else:
            try:
                for message in new_messages:
                    #Wuhu we got a message. Let's extract some details from it
                    msg = message['message'].lower()
                    username = message['username'].lower()
                    print(username + ": " + msg)

                    if msg.startswith("!"):
                        if msg.startswith("!oc"):
                            x, y = msg.split("!oc")[1].split(",")
                            k.one_mouse_click((x, y))
                        elif msg.startswith("!dc"):
                            x, y = msg.split("!dc")[1].split(",")
                            k.two_mouse_click((x, y))
                        elif msg.startswith("endday"):
                            print "doing enday"
                            k.triple_click_300()
                    elif msg == "endday":
                        print "doing enday"
                        k.triple_click_300()
                    elif msg in dictionary.keys():
                        k.one_mouse_click(dictionary[msg])
                    elif msg == "click":
                        k.click()
                    elif msg == "mright":
                        k.mright()
                    elif msg == "mleft":
                        k.mright()
                    elif msg == "mup":
                        k.mup()
                    elif msg == "mdown":
                        k.mrimdownght()
                    elif "," in msg:
                        if msg.endswith("*2"):
                            x, y = msg.replace("*2","").split(",")
                            k.one_mouse_click((x, y))
                        else:
                            x, y = msg.split(",")
                            k.one_mouse_click((x, y))             
            except Exception:
                continue
    except Exception as e:
        print e
        print "Got iOS error"
        os.system("python main.py")
        exit(-1)
        continue


