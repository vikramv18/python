import os
import time
a=1
b=1
while (a<5):
    os.system("fswebcam -F 5 --fps 20 -r 1200x800 /home/pi/vvv/8" +str(b)+".jpg")
    time.sleep(1)
    print("pic taken",str(b))
    a=a+1
    b=b+1
