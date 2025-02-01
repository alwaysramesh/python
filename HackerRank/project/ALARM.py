import datetime
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting....")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if current_time == alarm_time:
            print("Wake up! It's time!")
            end_time = time.time() + 10  
            
            while time.time() < end_time:
                engine.say("Wake up! It's time!")
                engine.runAndWait() 
            
            break  
            
        time.sleep(1)

alarm_time = "21:38"  
alarm_clock(alarm_time)
