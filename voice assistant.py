import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, I couldn't request results. Check your internet connection.")
            return ""

# Function to process the user's command
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "how are you" in command:
        speak("I'm doing well, thank you!")
    elif "what is your name" in command:
        speak("I am a voice assistant.")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)
