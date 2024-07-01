import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import random

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# print(rate)
engine.setProperty('rate',160)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_command(cmd):
    print("You said: " + cmd)
    jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you get if you cross a snowman and a vampire? Frostbite.",
    "Why did the math book look sad? Because it had too many problems."
    ]
    cmd = cmd.lower()

    if 'listen' in cmd:
        speak("Yes, I am listening.")
    elif "open google" in cmd:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open youtube" in cmd:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open facebook" in cmd:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "what time is it" in cmd or "current time" in cmd:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%I:%M %p')}")
    elif "what's your name" in cmd or "what is your name" in cmd:
        speak("I am your assistant. How can I help you?")
    elif "how are you" in cmd:
        speak("I am just a program, but I'm here to assist you!")
    elif "tell me a joke" in cmd:
        joke = random.choice(jokes)
        speak(joke)
    elif "what's the weather" in cmd or "what is the weather" in cmd:
        speak("I can't check the weather right now, but you can open a weather website.")
    elif "open weather" in cmd:
        webbrowser.open("https://www.weather.com")
        speak("Opening weather website.")
    elif "play some music" in cmd:
        speak("Playing some music for you.")
        # You can add code here to play music from a file or an online source.
    elif "what day is it" in cmd:
        today = datetime.datetime.today().strftime('%A')
        speak(f"Today is {today}.")
    elif "thank you" in cmd:
        speak("You're welcome!")
    elif "close" in cmd:
        pass
    else:
        speak("I didn't understand that. Can you please repeat?")


if __name__ == "__main__":
    speak("I m Awake")

    run = True

    while run:
        # Initialize recognizer
        r = sr.Recognizer()

        print("Active")

        try:
            # Use the microphone as the source for input.
            with sr.Microphone() as source:
                print("Listening..")
                # Adjust the recognizer sensitivity to ambient noise
                r.adjust_for_ambient_noise(source)
                # Listen for the first phrase and extract it into audio data
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    # Recognize speech using Google Web Speech API
            text = r.recognize_google(audio)
            if 'close' in text.lower():
                speak("Turning off")
                run = False
            process_command(text)

        except Exception as e:
            print(e)