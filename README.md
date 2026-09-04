# 💰 Salary Prediction using Machine Learning

A full-stack Machine Learning web application that predicts an estimated salary based on job-related information such as experience level, employment type, job title, employee residence, remote work ratio, company location, and company size.

## 🚀 Project Overview

This project uses a Machine Learning model to predict salaries in USD.

Users can enter their job and employment details through a web interface, and the application sends the data to a Flask backend. The backend processes the input using a trained Machine Learning model and returns the predicted salary.

## 🖥️ Features

- Predict estimated salary in USD
- User-friendly web interface
- Flask REST API backend
- Machine Learning model integration
- Data preprocessing pipeline
- Real-time salary predictions
- Responsive UI

## 🛠️ Technologies Used

### Machine Learning
- Python
- Pandas
- Scikit-learn
- Joblib

### Backend
- Flask
- Flask-CORS

### Frontend
- HTML
- CSS
- JavaScript

### Development Tools
- VS Code
- Git
- GitHub

## 📂 Project Structure

```text
Salary_Prediction/
│
├── BackEnd/
│   └── app.py
│
├── Data/
│   └── salary data files
│
├── FrontEnd/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── ML/
│   └── machine learning training files
│
├── Model/
│   ├── salary_model.pkl
│   └── preprocessor.pkl
│
├── .gitignore
├── requirements.txt
└── README.md