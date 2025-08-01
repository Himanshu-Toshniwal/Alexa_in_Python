# 🎙️ Python Voice Assistant - Alexa Clone

This is a simple voice-controlled assistant built in Python that can listen to your commands and respond using text-to-speech. It can play YouTube songs, tell you the current time, fetch Wikipedia summaries, tell jokes, and more!

## 🚀 Features

- 🎧 Listens to your voice using a microphone
- 🔊 Speaks responses using text-to-speech
- 🎵 Plays songs on YouTube
- ⏰ Tells the current time
- 🧠 Gives brief Wikipedia summaries
- 😂 Tells random programming jokes
- 💬 Works in a continuous listening loop

## 🛠️ Technologies Used

- `speech_recognition`: For converting speech to text
- `pyttsx3`: For text-to-speech (offline)
- `pywhatkit`: For playing YouTube videos
- `datetime`: To fetch system time
- `wikipedia`: To get short summaries of people or topics
- `pyjokes`: For jokes


## 🧠 How It Works

1. The assistant starts in an infinite loop and keeps listening for voice commands.
2. Once the user says **"Alexa"**, followed by a command, the assistant:
   - Plays a song if the command contains “play”
   - Tells time if the command includes “time”
   - Fetches Wikipedia info if the user asks “who the heck is ...”
   - Tells jokes and responds to casual conversations

## 🧑‍💻 Setup Instructions

### ✅ Prerequisites
- Python 3.x installed
- Microphone enabled and working



```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
