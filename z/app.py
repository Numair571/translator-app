from flask import Flask,render_template,request
from googletrans import Translator , LANGUAGES

app= Flask(__name__)

@app.route('/')
def home(): 
    language = list(LANGUAGES.values())
    print(language)
    return render_template('home.html',data=language)

@app.route('/translate', methods=['get','post'])
def translate():
    inp=request.form['inp']
    src =request.form['src']
    dest=request.form['dest']
    language = list(LANGUAGES.values())
    translator=Translator()
    data=translator.translate(text=inp,src=src,dest=dest)
    return render_template('home.html',output=data.text,data=language)

if __name__=="__main__":
    app.run()