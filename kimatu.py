
import streamlit as st
import speech_recognition as sr
import numpy as np
import pandas as pd
import requests
from PIL import Image
from PIL import ImageDraw
import io



def Hen(x):
    r = sr.Recognizer()
    with sr.AudioFile(x) as source:
        audio = r.record(source)
    try:
      text = r.recognize_google(audio, language="ja-JP")
    except sr.UnknownValueError:
        text = 'エラーです'
    except sr.RequestError as e:
        text = 'エラーです'
    return text

def Bot(txt):
    apikey = "DZZkDKXzZxh6VbuDoILXXEFsdPW0XzJQ"
    talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"
    payload = {"apikey": apikey, "query": txt}
    response = requests.post(talk_url, data=payload)
    try:
        return response.json()["results"][0]["reply"]
    except:
        print(response.json())
        return "ごめんなさい。もう一度教えて下さい。"

Choice = st.sidebar.selectbox('選んでね',('音声', 'チャットボット'))
if Choice == "音声":
    st.title("音声データをテキストに変換")
    Up_file = st.file_uploader("wavファイルアップロード", type='wav')
    if st.button('実行'):
        st.header(Hen(Up_file))
elif Choice == "チャットボット":
    text = st.text_input("文字を入力してお話ししよう！","")
    if st.button("実行"):
        st.write("あなた：{}".format(text))
        resul_t = Bot(text)
        st.write("BOTちゃん:{}".format(resul_t))

        res = requests.post(Face_APi,params=params,headers=headers,data=biny_img)
        results = res.json()
        for result in results:
            rect = result['faceRectangle']
            draw = ImageDraw.Draw(img)
            draw.rectangle([(rect['left'],rect['top']),
                            (rect['left']+rect['width'],
                            rect['top']+rect['hight'])],fill = None,outline='green',width=5)
        st.image(img ,caption='Imege.',use_column_width=True)
