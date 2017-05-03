import webbrowser
import time
times = 3
count = 0
print("This Program started on " + time.ctime())
while(count < times):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=yT26Vpptl-8")
    count = count + 1
print ("Hi Dude")
