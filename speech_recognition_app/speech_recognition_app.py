import speech_recognition as sr


def main():
    print("Say something:", end=' ')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=10)
        try:
            print(r.recognize_google(audio))
        except Exception as error:
            print(error)


if __name__ == '__main__':
    while True:
        main()
