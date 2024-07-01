import gradio as gr
from googletrans import Translator
from gtts import gTTS
translator=Translator()
def do(language,text):
  if language == 'en':
    translation = translator.translate(text, dest='zh-tw')
    tts = gTTS(translation.text, lang='zh-tw')
    tts.save('output.mp3')
    return translation.text,'output.mp3'
  elif language == 'ch':
    translation = translator.translate(text, dest='en')
    tts = gTTS(translation.text, lang='en')
    tts.save('output.mp3')
    return translation.text,'output.mp3'
  
iface=gr.Interface(fn=do,title='中英翻譯器',description='第一格輸入en執行英翻中,輸入ch執行中翻英,第二格輸入要翻譯的內容。',inputs=['text','text'],outputs=["text",'audio'])
iface.launch(share=True)
