# ch-en-translate
中英文翻譯工具
# 介紹
這是一個中英文翻譯程式，
第一個輸入格輸入en/ch來決定我們需要輸入中文還英文，
接著第二行寫出您需要翻譯的東西，
接著送出過後我們就會將我們的東西輸出，
輸出第一格放翻譯後的字，
第二格放翻譯後的音檔。
# 執行我們的程式
在上面我們有附上檔案，
如果想要省麻煩就用python放入您電腦，
接著去終端機import gradio,googletrans,gTTS,
也可以透過我們放在colab的網址進去https://colab.research.google.com/drive/1Xm8OWPBINvGmloIx7PAGZhdOBviR9p5z?usp=sharing。（進去後生成的網址可以複製下來，他可以用一段時間）
# 上面的檔案
app.py是python的檔案，
如果使用這個需要自行安裝上面說的東西，
另一個是我們直接從colab下載下來的。
# 程式介紹
我們要先匯入gradio,gTTS等模組，接著寫著gradio的模板，以及判斷第一次輸入什麼然後翻譯什麼語言，再去做翻譯（用google的翻譯模組），接著生成語音（靠gTTS)。
# 公開網站...
希望可以找人陪我們將我們的網站放上hugging face，
近期還在研究error中。
# 下次更新內容
下次我們希望可以更新也可以讓大家語音輸入,或者是也可以支援日語（這個應該會先出）。
# 執行圖片
<img width="1236" alt="截圖 2024-07-02 下午11 00 30" src="https://github.com/hackeryu314159/ch-en-translate/assets/125031865/1e96d72d-5003-46a0-9f5c-896d6b5d1687">;
# 引用內容
googletrans,gTTS,gradio。
# 特別感謝
Jimmy876135
,hackeryu314159

