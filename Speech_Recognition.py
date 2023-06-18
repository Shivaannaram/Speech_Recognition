import speech_recognition as sr
def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please Say Something")
        audio=r.listen(source)
        print("Recognizing now...")
        try:
            print("You Said:\n",r.recognize_google(audio))
            print("Audio Recorded Successfully ")
        except Exception as e:
            print("Error :",str(e))

        with open("recorded.wav","wb") as f:
            f.write(audio.get_wav_data())
main()
# if __name__=="__main__":
#     main()