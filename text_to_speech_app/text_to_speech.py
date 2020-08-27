"""Text to speech def's"""

import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def speak_ru(text):
    tts = gTTS(text=text, lang="ru")
    filename = "voice_ru.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def speak_from_file():
    """Reads and pronounces the file."""
    file = open("text.txt", "r")
    text = file.read().replace("\n", " ")
    tts = gTTS(text=text, lang="en")
    filename = "voice_from_file.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    file.close()


def speak_from_file_ru():
    """Reads and pronounces the file."""
    file = open("text.txt", "r")
    text = file.read().replace("\n", " ")
    tts = gTTS(text=text, lang="ru")
    filename = "voice_from_file_ru.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    file.close()


speak("Hello tim.")
speak_ru("Привет, как дела?")
speak_from_file()
speak_from_file_ru()
