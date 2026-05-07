from flask import Flask, request, jsonify
from model import predict_role

app = Flask(__name__)

@app.route('/')
def home():
    return "Resume Analyzer API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    resume = data['resume']

    role = predict_role(resume)

    return jsonify({
        "predicted_role": role
    })

if __name__ == '__main__':
    app.run(debug=True)