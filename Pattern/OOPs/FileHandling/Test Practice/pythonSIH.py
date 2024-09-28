import random
import time
import smtplib
from playsound import playsound

# Thresholds
EARTH_RESISTANCE_THRESHOLD = 5  # in ohms
LEAKAGE_CURRENT_THRESHOLD = 30  # in milliamps

# Email credentials (These should ideally be stored in environment variables or a secure vault)
EMAIL = 'sonamjuda@gmail.com'
PASSWORD = 'Ramesh@2004!@#'
RECIPIENT_EMAIL = "viprameshkumar8085.com"  # Set the recipient's email here

def send_alert(message):
    """Function to send an email alert."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, RECIPIENT_EMAIL, message)
        server.quit()
        print("Alert email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def sound_alarm():
    """Function to play sound in case of an alert."""
    try:
        playsound("C:\python29\Pattern\OOPs\FileHandling\Test Practice\alarm_sound.mp3.mp3")   # Full or correct path to the sound file
        print("Alarm triggered!")
    except Exception as e:
        print(f"Failed to play sound: {e}")

def monitor_system():
    """Function to monitor the system."""
    while True:
        earth_resistance = random.uniform(1, 10)  # Simulate earth resistance
        leakage_current = random.uniform(10, 50)  # Simulate leakage current
        
        print(f"Earth Resistance: {earth_resistance} ohms, Leakage Current: {leakage_current} mA")
        
        if earth_resistance > EARTH_RESISTANCE_THRESHOLD:
            print("Warning: Earth resistance is above safe limits!")
            send_alert(f"Earth resistance is high: {earth_resistance} ohms")
            sound_alarm()
        
        if leakage_current > LEAKAGE_CURRENT_THRESHOLD:
            print("Warning: Leakage current is above safe limits!")
            send_alert(f"Leakage current is high: {leakage_current} mA")
            sound_alarm()
        
        time.sleep(5)  # Adjust monitoring interval as needed

if __name__ == "__main__":
    monitor_system()
