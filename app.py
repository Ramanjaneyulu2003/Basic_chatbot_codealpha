from flask import Flask, render_template, request, jsonify
from models.chatbot import get_response

app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot conversation
@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.json['message']
    response = get_response(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
