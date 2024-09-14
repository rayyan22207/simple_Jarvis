import speech_recognition as sr
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set the name of the assistant
ASSISTANT_NAME = "Jarvis"

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Flag to track if the weather question has been asked before
weather_asked = False

# Function to listen for a specific wake word
def listen():
    with sr.Microphone() as source:
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

def main():
    global weather_asked
    speak(f"Hello, I am {ASSISTANT_NAME}. How can I help you today?")
    while True:
        # Detect if there's any voice activity
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for wake word...")
            audio = recognizer.listen(source, timeout=5)  # Adjust timeout as needed
            try:
                text = recognizer.recognize_google(audio)
                if text and ASSISTANT_NAME.lower() in text.lower():
                    command = text.lower().replace(ASSISTANT_NAME.lower(), "").strip()
                    if "hello" in command:
                        speak(f"Hello! How can I assist you?")
                    elif any(word in command for word in ["weather", "temperature", "forecast"]):
                        if not weather_asked:
                            speak("Look outside, you lazy thing!")
                            weather_asked = True
                        else:
                            speak("Okay, if you insist. It's sunny, happy now? Ugh.")
                    elif "exit" in command:
                        speak("Goodbye!")
                        break
                    else:
                        speak(f"You said {command}")
                else:
                    print("Waiting for the wake word...")
            except sr.UnknownValueError:
                print("No recognizable speech detected.")
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                continue

if __name__ == "__main__":
    main()
