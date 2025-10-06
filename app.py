from flask import Flask, render_template, request
from feature_engineering import FeatureEngineer
import numpy as np
import pandas as pd 
import joblib

# --- Initialize app ---
app = Flask(__name__)
app.jinja_env.cache = {}


# --- Load your trained model ---
model=joblib.load("model_pipeline.pkl")


# --- Home page route ---
@app.route("/")
def home():
    return render_template("heart6.html")


# --- Predict route ---
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 1. Collect input values from form
        features={
        "age" :float(request.form["age"]),
        "anaemia":int(request.form["anaemia"]),
        "creatinine_phosphokinase":int(request.form["creatinine_phosphokinase"]),
        "diabetes": int(request.form["diabetes"]),
        "ejection_fraction":int(request.form["ejection_fraction"]),
        "high_blood_pressure":int(request.form["high_blood_pressure"]),
        "platelets":float(request.form["platelets"]),
        "serum_creatinine":float(request.form["serum_creatinine"]),
        "serum_sodium":int(request.form["serum_sodium"]),
        "sex" :int(request.form["sex"]),  
        "smoking":int(request.form["smoking"]),
        "time":int(request.form["time"])
        
        } 
        # 2. pandas frame
        X = pd.DataFrame([features])
        print(X.columns)


        # 3. Run model
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]  
        confidence = float(probabilities[prediction])
        confidence_pct = f"{confidence * 100:.1f}%"
        # 4. Format prediction text

        if prediction == 1:
            prediction_text = "High Risk of Death"
            
        else:                                                                                                                                      
            prediction_text = "Low Risk of Death"
            
        # 5. Send result to template
        return render_template("heart6.html",
                               prediction=prediction_text,
                               confidence=confidence_pct)
                                
    except Exception as e:
        return render_template("heart6.html",
                               prediction=f"Error: {str(e)}",
                               confidence=0)

# --- Run the app ---
if __name__ == "__main__":
    app.run(debug=True)