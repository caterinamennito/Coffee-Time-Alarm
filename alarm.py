
import datetime
import os
import vlc

sound_file = vlc.MediaPlayer("/home/user123/Bureau/gong.mp3")
stop = False
alarms = [{"start":"16:04", "end": "16:05"}, {"start":"16:07", "end": "16:08"}, {"start":"16:10", "end": "16:11"}]


    # print(alarms[counter])
    # counter +=1

while stop == False:
    rn = str(datetime.datetime.now().strftime("%H:%M"))
    print(rn)

    for alarm in alarms:
        if rn >= alarm['start'] and rn < alarm['end']:
            sound_file.play()
            continue
