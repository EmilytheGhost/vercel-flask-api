from flask import Flask, request, jsonify
from difflib import SequenceMatcher
from flask_cors import CORS  # 如果需要处理跨域请求

app = Flask(__name__)
CORS(app)  # 启用 CORS

def compare_texts(text1, text2):
    """比较两个文本的相似度，返回相似度比例"""
    return SequenceMatcher(None, text1, text2).ratio()

@app.route('/compare', methods=['POST'])
def compare():
    """处理文本比较请求"""
    data = request.json
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')

    # 检查是否提供了必要的文本
    if not text1 or not text2:
        return jsonify({'error': 'Both text1 and text2 are required'}), 400

    similarity = compare_texts(text1, text2)
    return jsonify({'similarity': similarity})

# 如果你需要与 AWS Lambda 集成，可以使用以下代码
# from awsgi import response as awsgi_response
# def handler(event, context):
#     return awsgi_response(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)
