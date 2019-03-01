from flask import Flask, request, jsonify
import json
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/', methods=['POST'])
def index():
    print(json.loads(request.get_data()))
    return jsonify(
        status=200,
        replies=[{
            'type': 'text',
            'content': 'Roger that',
        }],
        conversation={
            'memory': {'key': 'value'}
        }
    )


@app.route('/errors', methods=['POST'])
def errors():
    print(json.loads(request.get_data()))
    return jsonify(status=200)

if __name__ == '__main__':
    app.run()