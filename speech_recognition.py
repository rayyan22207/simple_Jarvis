import speech_recognition as sr

# Initialize speech recognizer
recognizer = sr.Recognizer()

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
