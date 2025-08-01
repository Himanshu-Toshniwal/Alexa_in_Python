import speech_recognition as sr  # type: ignore
import pyttsx3  # type: ignore
import pywhatkit  # type: ignore
import datetime
import wikipedia  # type: ignore
import pyjokes  # type: ignore

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""  # Ensure it's initialized
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)  # helps in noisy environments
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Speech Recognition service is unavailable")
    except Exception as e:
        print(f"Error: {e}")
    return command

def run_alexa():
    command = take_command()
    if command:
        print("You said:", command)
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '').strip()
            try:
                about = wikipedia.summary(person, sentences=1)
                talk(about)
                print(about)
            except:
                talk("Sorry, I couldn't find information about that person.")
        elif 'date' in command:
            talk('Why not, let’s go!')
        elif 'are you single' in command:
            talk('I am in a relationship with Python.')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        else:
            talk('Please say that again.')
    else:
        print("No command detected.")

# Continuous loop
while True:
    run_alexa()

    
    

    
    

    
    

    






    