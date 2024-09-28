import random
import time
import smtplib
from playsound import playsound

# Define safe ranges for earth resistance and leakage current
EARTH_RESISTANCE_THRESHOLD = 5  # in ohms
LEAKAGE_CURRENT_THRESHOLD = 30  # in milliamps


def send_alert(message):
    """Function to send an alert via email"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password")  # Your email credentials
        server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", message)
        server.quit()
        print("Alert email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def sound_alarm():
    """Function to play sound in case of a failure"""
    playsound("alarm_sound.mp3")  # Path to alarm sound file
    print("Alarm triggered!")


def monitor_system():
    """Function to continuously monitor the system"""
    while True:
        # Simulated sensor values (replace these with real sensor readings)
        earth_resistance = random.uniform(1, 10)  # Simulate earth resistance value in ohms
        leakage_current = random.uniform(10, 50)  # Simulate leakage current in mA

        print(f"Earth Resistance: {earth_resistance} ohms, Leakage Current: {leakage_current} mA")

        # Check for deviations
        if earth_resistance > EARTH_RESISTANCE_THRESHOLD:
            print("Warning: Earth resistance is above safe limits!")
            send_alert(f"Earth resistance is high: {earth_resistance} ohms")
            sound_alarm()

        if leakage_current > LEAKAGE_CURRENT_THRESHOLD:
            print("Warning: Leakage current is above safe limits!")
            send_alert(f"Leakage current is high: {leakage_current} mA")
            sound_alarm()

        time.sleep(5)  # Monitor every 5 seconds (adjust as necessary)


if __name__ == "__main__":
    monitor_system()
