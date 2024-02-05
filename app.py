import re
from flask import Flask, request, jsonify
import pytest

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

def sanitize_input(input_string):
    if re.search(r"[\"';\\%&$#*()=+\[\]{}|`<>?@!]", input_string):
        return 'unsanitized'
    else:
        return 'sanitized'

@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sanitization():
    data = request.get_json()
    input_string = data.get('input', '')
    result = sanitize_input(input_string)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)

