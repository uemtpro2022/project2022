import random
import serial
import time
import cv2
import speech_recognition as sr

ser=serial.Serial('COM7', 9600, timeout=1)
#ser.readline()
#not_used = ser.readline()
time.sleep(1)
print(ser)
print("START")
"""
line = ser.readline()   # 行終端まで読み込む
line = line.rstrip()
print("START")
print(line)
ser.close()
exit()
"""
Nomal = cv2.imread("tanuki.png")
Rough  = cv2.imread("tanuki_smile.png")
Sleep = cv2.imread("tanuki_sleep.png")
while True:
    #count_arduino = ser.readline()
    # val_decoded = float(repr(val_arduino.decode())[1:-5])
    #count_decoded = count_arduino
    line = ser.readline()   # 行終端まで読み込む
    line = line.rstrip()
    #print(count_decoded)
    print(line)
    if int(line) > 520:
        cv2.imshow("picture", Sleep)
        cv2.waitKey(10)
    else:
        cv2.imshow("picture", Nomal)
        cv2.waitKey(10)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            from playsound import playsound
            playsound("voiceDo.wav")
            r.adjust_for_ambient_noise(source)
            print("何か話しかけてください")
            text = r.listen(source)
            print("[o] ===> オーディオGET")
            print("=== 音声解析中 ===")
            text2 = r.recognize_google(text,language="ja-JP")
            print("You said : " + text2)
        if text2 == "おはよう":
            cv2.imshow("picture", Rough)
            cv2.waitKey(10)
            from playsound import playsound
            playsound("voiceOha.wav")
        elif text2 == "こんにちは":
                from playsound import playsound
                playsound("voicesample2.wav")
        elif "聞いてよ" in text2:
                rand = random.random() * 10
                print(rand)
                if rand < 5:
                    from playsound import playsound
                    playsound("voiceRand.wav")
                else:
                    from playsound import playsound
                    playsound("voiceRand2.wav")
        elif text2 == "おやすみ":
            from playsound import playsound
            playsound("voiceOya.wav")
            cv2.destroyAllWindows()
            break
        else:
            cv2.imshow("picture", Rough)
        cv2.waitKey(10)
#ser.close()