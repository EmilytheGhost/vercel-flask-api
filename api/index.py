from flask import Flask, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)

def compare_texts(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    similarity = compare_texts(text1, text2)
    return jsonify({'similarity': similarity})

def handler(event, context):
    return app(event, context)
