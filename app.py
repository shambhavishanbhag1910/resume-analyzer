from flask import Flask, request, jsonify
from model import predict_role, extract_skills

app = Flask(__name__)

@app.route('/')
def home():
    return "Resume Analyzer API Running"


@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    resume = data['resume']

    role = predict_role(resume)

    skills = extract_skills(resume)

    return jsonify({
        "predicted_role": role,
        "skills_found": skills
    })


if __name__ == '__main__':
    app.run(debug=True)