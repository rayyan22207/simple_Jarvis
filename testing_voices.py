import pyttsx3

def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")

list_voices()

from google.cloud import texttospeech

# Initialize Google Text-to-Speech client
client = texttospeech.TextToSpeechClient()

def speak(text):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # Specify language
        name="en-US-Wavenet-D"  # Specify voice name
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("Audio content written to file 'output.mp3'")

    # Play the output.mp3 file using an appropriate library or tool
speak('hello')

# was for changing the voice will do later