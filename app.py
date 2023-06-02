from flask import Flask, jsonify, request
from googletrans import Translator
translator = Translator()
  
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/translate', methods=['POST'])
def translate():
    translation = translator.translate(request.form['content'], dest=request.form['language'])
    return jsonify({'convertedText':translation.text})


if __name__ == '__main__':
    app.run(debug=True)