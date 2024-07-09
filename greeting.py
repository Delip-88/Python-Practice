from datetime import datetime
import  pyttsx3


engine = pyttsx3.init()
v =engine.getProperty('voices')
engine.setProperty('voice',v[1].id)


# Get the current date and time
now = datetime.now()

# Format the current time to only show hours and minutes
current_time = now.strftime("%H:%M")

# Convert the formatted current time string back to a time object
current_time_obj = datetime.strptime(current_time, "%H:%M").time()

# Print the formatted current time
print("Current Time:", current_time)

# Determine the appropriate greeting based on the current time
if current_time_obj < datetime.strptime("12:00", "%H:%M").time():
    txt = "Good Morning"
    engine.say(txt)
    engine.runAndWait()
elif datetime.strptime("12:00", "%H:%M").time() <= current_time_obj < datetime.strptime("18:00", "%H:%M").time():
    txt = "Good Afternoon"
    engine.say(txt)
    engine.runAndWait()
elif datetime.strptime("18:00", "%H:%M").time() <= current_time_obj < datetime.strptime("21:00", "%H:%M").time():
    txt = "Good Evening"
    engine.say(txt)
    engine.runAndWait()
else:
    txt = "Good Night"
    engine.say(txt)
    engine.runAndWait()
