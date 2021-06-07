import win32com.client
import pyttsx3
engine = pyttsx3.init()
#print(engine.setProperty('rat'))  #获取当前说话率的详细信息

voices = engine.getProperty('voices')  #获取当前语音的详细信息
# print(voices)
for voice in voices:
    engine.setProperty("voice",voice.id)

# engine.setProperty('voice',voices.id)#changing索引，更改声音。o男
# #engine.setProperty('voice',voices[1].id)#changing索引，改变声音。女用1件
# engine.say('富强，民主，文明，和谐')
# engine.runAndWait()