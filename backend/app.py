from flask import Flask, request, jsonify
from ai_model import generate_response

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
  data = request.get_json()
  user_message = data['message']
  ai_response = generate_response(user_message)
  return jsonify({'response': ai_response})

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')