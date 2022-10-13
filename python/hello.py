import speech_recognition as sr
import cv2

r = sr.Recognizer()
 
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("何か話しかけてください")
    text = r.listen(source)
    print("[o] ===> オーディオGET")
    print("=== 音声解析中 ===")
    text2 = r.recognize_google(text,language="ja-JP")
    print("You said : " + text2)
if text2 == "おはよう":
    from playsound import playsound
    playsound("voiceOha.wav")
    img = cv2.imread('picOhayo.png')
    cv2.imshow('sample', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    