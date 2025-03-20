#speech recognition
#use google API to recognize the voice

#目前進度: 1.可以辨識語音 2.可以將語音記錄下來 3.可以將語音記錄下來的資料存成excel檔 4.可以查詢語音記錄下來的資料

#待解決:1.將語音紀錄成xlsx,目前檔案內為空的 2.將資料分類成不同欄位,目前只有一個欄位,且判斷語音是問句還是陳述句
#      3.不需要再輸出端每次顯示if you want to stop, say 'stop' or '停止' ...等等,只需第一次顯示即可

# 如無法解決,可考慮將資料存成txt檔,並將資料分類成不同欄位

import speech_recognition as sr
import pandas as pd #pandas 是一個用於數據處理和數據分析的函式庫
import datetime
import os

memory_list = []

def judge_speech(text):
    if '?' or '嗎' in text:
        return 'Question'
    else:
        return 'Statement'

def speech_recognition():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Say something :", "if you want to stop, say 'stop' or '停止'","and if you want to ask, say 'i want to ask' or '我想查詢'")
            audio = r.listen(source)
        try:

            text = r.recognize_google(audio, language="zh-tw,en-US" )
            print("You said: " + text)

            if text.lower() == "stop" or text == "停止":
                print("Stopping speech recognition...")
                break

            if text == "i want to ask" or text == "我想查詢":
                print("Triggering query mode...")
                repeat_user_input()
                continue

            speech_type = judge_speech(text)

            memory_data = {
                'timestamp': datetime.datetime.now(),
                'speech':text,
                'type': speech_type
            }

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def save_to_file():
    file_name = "speech_memory.xlsx"

    if os.path.exists(file_name): #path.exists() 用於判斷文件是否存在
        df_existing = pd.read_excel(file_name)
        df_new = pd.DataFrame(memory_list)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True) #df_combined是合併後的dataframe ; ignore_index=True是忽略原本的index
    else:
        df_combined = pd.DataFrame(memory_list)

    df_combined.to_excel(file_name, index=False)

def repeat_user_input():
    try:
        with open("speech_memory.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print("No speech memory found.")
            return

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("what do you want to ask?")
            audio = r.listen(source)

        try:
            question = r.recognize_google(audio, language="zh-tw" "en-US")
            print("You said: " + question)

            for line in lines:
                if question.strip() in line:
                    print("response: ", line)
                    return

            print("No response found.")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) #format(e) 意思是把e的值放到{}裡面

    except FileNotFoundError:
        print("No speech memory found., please run speech_recognition() first.")

if __name__ == "__main__":
    speech_recognition()
    save_to_file()
    repeat_user_input()
