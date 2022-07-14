import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformate ='{:02d}:{:02d}'.format(mins, secs)
        print(timeformate, end='\r')
        time.sleep(1)
        time_sec -=1
    print("stop")
print(countdown(10))
