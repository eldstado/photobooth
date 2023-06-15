from datetime import datetime
import sys
import os
import json
import random
import time


dir_path = r'/home/pi/script/vitser/'
vitser = os.listdir(dir_path)
vitser_path = '/home/pi/script/vitser/'


def write_json(action):
    with open('/home/pi/script/photobooth.json', 'r') as json_file:
        data = json.load(json_file)

    if action == "event_start":
        data["event_start"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["taking_picture"] = "True"
    elif action == "event_stop":
        data["taking_picture"] = "False"
    with open('/home/pi/script/photobooth.json', 'w') as file:
        json.dump(data, file)


if len(sys.argv) > 1:
    arg1 = str(sys.argv[1])
else:
    arg1 = "lol"

print(len(sys.argv))
print(arg1)
# os.system('/usr/bin/mpg123 photobooth_motion.mp3 &')

# order jokes

# f = open("/tmp/motion.txt", "a")
if arg1 == "event_start":
    write_json("event_start");
    print("play audio")
    os.system('/usr/bin/mpg123 /home/pi/script/motion_detected.mp3')
    # play joke...
    os.system('/usr/bin/mpg123 ' + vitser_path + vitser[random.randint(0, 23)])
    os.system('/usr/bin/mpg123 /home/pi/script/321.mp3')
    os.system('/usr/bin/irsend send_once Nikon2 shutter &')
    time.sleep(4)
    os.system('/usr/bin/mpg123 /home/pi/script/10_sekunder.mp3')
    write_json("event_stop")
elif arg1 == "event_stop":
    write_json("event_stop")