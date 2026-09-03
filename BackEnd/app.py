from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os


app = Flask(__name__)
CORS(app)

# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the trained model
model_path = os.path.join(BASE_DIR, "Model", "salary_model.pkl")
model = joblib.load(model_path)

# Load the preprocessor
preprocessor_path = os.path.join(BASE_DIR, "Model", "preprocessor.pkl")
preprocessor = joblib.load(preprocessor_path)


@app.route("/")
def home():
    return jsonify({
        "message": "Salary Prediction API is running!"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    # Convert user input into a DataFrame
    input_data = pd.DataFrame([{
        "work_year": data["work_year"],
        "experience_level": data["experience_level"],
        "employment_type": data["employment_type"],
        "job_title": data["job_title"],
        "employee_residence": data["employee_residence"],
        "remote_ratio": data["remote_ratio"],
        "company_location": data["company_location"],
        "company_size": data["company_size"]
    }])

    # Preprocess the input
    processed_data = preprocessor.transform(input_data)

    # Make prediction
    prediction = model.predict(processed_data)[0]

    return jsonify({
        "predicted_salary_usd": round(float(prediction), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)