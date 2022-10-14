import random
import serial
import time
import cv2
import speech_recognition as sr

Nomal = cv2.imread("tanuki.png")
Rough  = cv2.imread("tanuki_smile.png")
Sleep = cv2.imread("tanuki_sleep.png")
while True:
			cv2.imshow("picture", Sleep)
			cv2.waitKey(0)
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
			elif "聞いて" in text2:
							rand = random.random() * 10
							print(rand)
							if rand < 5:
									from playsound import playsound
									playsound("voicesample3.wav")
							else:
									from playsound import playsound
									playsound("voicesample3.wav")
			elif text2 == "おやすみ":
					from playsound import playsound
					playsound("voiceOya.wav")
					cv2.destroyAllWindows()
					break
			else:
					cv2.imshow("picture", Rough)
					from playsound import playsound
					playsound("voiceAi.wav")
			cv2.waitKey(10)
#ser.close()