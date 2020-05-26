# coding: utf-8

import os
import time
import pyttsx3 as psx3
import speech_recognition as sr

# Вывод списка устройств
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# Проверка работы микрофона
r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print("Скажи что-нибудь")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("Сказал " + query.lower())

engine = psx3.init()
engine.say("Тест 1")
engine.runAndWait()