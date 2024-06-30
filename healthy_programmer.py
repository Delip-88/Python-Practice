import time
import threading
import pyttsx3
from datetime import datetime, time as dtime

START_TIME = datetime.strptime("09:00:00", "%H:%M:%S").time()
END_TIME = datetime.strptime("17:00:00", "%H:%M:%S").time()

def text_to_speech(text, stop_event):
    engine = pyttsx3.init()
    while not stop_event.is_set():
        engine.say(text)
        engine.runAndWait()
        time.sleep(3)

def drink_water():
    ans = ''
    stop_event = threading.Event()
    speech_thread = threading.Thread(target=text_to_speech, args=("It's time to drink water", stop_event))
    speech_thread.start()
    
    while ans != 'drank':
        ans = input("If done, type 'drank': ")
    
    stop_event.set()
    speech_thread.join()
    print("Stopping text-to-speech...")
    print("_________________________")

def eye_exercise():
    ans = ''
    stop_event = threading.Event()
    speech_thread = threading.Thread(target=text_to_speech, args=("Do some eye exercise", stop_event))
    speech_thread.start()
    
    while ans != 'done':
        ans = input("If done, type 'done': ")
    
    stop_event.set()
    speech_thread.join()
    print("Stopping text-to-speech...")
    print("_________________________")

def physical_exercises():
    ans = ''
    stop_event = threading.Event()
    speech_thread = threading.Thread(target=text_to_speech, args=("Do some physical exercise", stop_event))
    speech_thread.start()
    
    while ans != 'ex done':
        ans = input("If done, type 'ex done': ")
    
    stop_event.set()
    speech_thread.join()
    print("Stopping text-to-speech...")
    print("_________________________")

if __name__ == "__main__":
    while True:
        now = datetime.now().time()
        if START_TIME < now < END_TIME:
            print(now.strftime("%H:%M:%S"))
            time.sleep(3)
            drink_water()
            time.sleep(5)
            eye_exercise()
            time.sleep(3)
            physical_exercises()
        else:
            print("Outside working hours. Waiting until next period...")
            time.sleep(60)
