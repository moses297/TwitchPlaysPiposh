import twitch
import keypresser
t = twitch.Twitch()
k = keypresser.Keypresser()

#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
username = ""
key = ""
t.twitch_connect(username, key)

#The main loop

while True:
    #Check for new mesasages
    try:
        new_messages = t.twitch_recieve_messages()
    except Exception:
        t.twitch_connect(username, key)
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
                print(username + ": " + msg);

                if msg.startswith("!"):
                    if msg.startswith("!oc"):
                        x, y = msg.split("!oc")[1].split(",")
                        k.one_mouse_click((x, y))
                    elif msg.startswith("!dc"):
                        x, y = msg.split("!oc")[1].split(",")
                        k.two_mouse_click((x, y))
        except Exception:
            continue
