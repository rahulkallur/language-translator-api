from flask import Flask, jsonify, request
from googletrans import Translator
translator = Translator()
  
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/translate', methods=['POST'])
def translate():
    content=request.form['content']
    language=request.form['language']
    translation = translator.translate(content, dest=language)
    return jsonify({'convertedText':translation.text})
