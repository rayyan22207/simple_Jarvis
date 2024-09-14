import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

def main():
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        text = listen()
        if text:
            if "hello" in text.lower():
                speak("Hello! How can I assist you?")
            elif "exit" in text.lower():
                speak("Goodbye!")
                break
            else:
                speak(f"You said {text}")

if __name__ == "__main__":
    main()
