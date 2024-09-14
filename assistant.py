from text_to_speech import speak
from speech_recognition import listen
from weather import get_weather

# Set the name of the assistant
ASSISTANT_NAME = "Jarvis"

# Flag to track if the weather question has been asked before
weather_asked = False

def main():
    global weather_asked
    speak(f"Hello, I am {ASSISTANT_NAME}. How can I help you today?")
    while True:
        # Detect if there's any voice activity
        print("Listening for wake word...")
        text = listen()
        if text and ASSISTANT_NAME.lower() in text.lower():
            command = text.lower().replace(ASSISTANT_NAME.lower(), "").strip()
            if "hello" in command:
                speak(f"Hello! How can I assist you?")
            elif any(word in command for word in ["weather", "temperature", "forecast"]):
                if not weather_asked:
                    speak("Look outside, you lazy thing!")
                    weather_asked = True
                else:
                    weather_info = get_weather()
                    speak(f"Okay, if you insist. {weather_info}, happy now? Ugh.")
            elif "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak(f"You said {command}")
        else:
            print("Waiting for the wake word...")

if __name__ == "__main__":
    main()
