import speech_recognition as sr
import pyttsx3
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set the name of the assistant 
ASSISTANT_NAME = "Jarvis"

# OpenWeatherMap API key and endpoint
API_KEY = "a3631ab2a77540c191c205140241409"  # Replace with your actual API key
WEATHER_URL = "http://api.weatherapi.com/v1/current.json"

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Flag to track if the weather question has been asked before
weather_asked = False

# Function to get weather from WeatherAPI
def get_weather(city="Karachi"):
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()
    if response.status_code == 200 and 'current' in data:
        weather_description = data['current']['condition']['text']
        temperature = data['current']['temp_c']
        return f"Current weather in {city}: {weather_description}, temperature is {temperature}°Celsius."
    else:
        return "I could not retrieve the weather information."

# Function to listen for a specific wake word
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)
        print(audio)
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
    speak(f"Hello, I am {ASSISTANT_NAME} the AI assistant from Iron Man. How can I help you today?")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for wake word...")
            audio = recognizer.listen(source, timeout=5)
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
                            # Check if a city name is mentioned in the command
                            words = command.split()
                            city = "Karachi"  # Default city
                            for word in words:
                                if word.capitalize() in ["Karachi", "Lahore", "Islamabad", "New York", "London"]:  # Add more city names as needed
                                    city = word.capitalize()
                                    break
                            weather_info = get_weather(city)
                            speak(f"Okay, if you insist. {weather_info}, happy now? Ugh.")
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
