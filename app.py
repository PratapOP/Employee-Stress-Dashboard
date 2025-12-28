from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from flask import session
from datetime import datetime
import csv
from io import StringIO
from flask import Response



app = Flask(__name__)
app.secret_key = "stress-history-secret"

model = joblib.load("model/stress_model.pkl")

STRESS_LABELS = {
    0: "Low Stress",
    1: "Medium Stress",
    2: "High Stress"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    feature_names = [
        "Sleep Hours",
        "Work Hours",
        "Screen Time",
        "Physical Activity",
        "Social Interaction",
        "Caffeine Intake"
    ]

    features = np.array([[  
        data["sleep_hours"],
        data["work_hours"],
        data["screen_time"],
        data["physical_activity"],
        data["social_interaction"],
        data["caffeine_intake"]
    ]])

    probabilities = model.predict_proba(features)[0]
    prediction_index = probabilities.argmax()
    confidence = round(probabilities[prediction_index] * 100, 2)

    importances = model.feature_importances_
    importance_data = sorted(
        [
            {"feature": f, "importance": round(i * 100, 2)}
            for f, i in zip(feature_names, importances)
        ],
        key=lambda x: x["importance"],
        reverse=True
    )

    recommendations = []

    if data["sleep_hours"] < 7:
        recommendations.append("Increase sleep to at least 7 hours daily.")
    if data["work_hours"] > 9:
        recommendations.append("Reduce work hours to prevent burnout.")
    if data["screen_time"] > 7:
        recommendations.append("Reduce prolonged screen exposure.")
    if data["physical_activity"] == 0:
        recommendations.append("Add at least 30 minutes of physical activity.")
    if data["caffeine_intake"] > 3:
        recommendations.append("Limit caffeine intake.")

    if not recommendations:
        recommendations.append("Your routine looks balanced. Keep it up.")

        # -----------------------------
    # Stress History (Session-based)
    # -----------------------------
    history = session.get("stress_history", [])

    history.append({
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "stress_level": STRESS_LABELS[prediction_index],
        "confidence": confidence
    })

    # Keep only last 7 predictions
    session["stress_history"] = history[-7:]


    return jsonify({
        "stress_level": STRESS_LABELS[prediction_index],
        "confidence": confidence,
        "feature_importance": importance_data,
        "recommendations": recommendations,
        "history": session["stress_history"]
    })
@app.route("/export/csv")
def export_csv():
    history = session.get("stress_history", [])

    if not history:
        return "No data available", 400

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Timestamp", "Stress Level", "Confidence (%)"])

    for entry in history:
        writer.writerow([
            entry["timestamp"],
            entry["stress_level"],
            entry["confidence"]
        ])

    output.seek(0)

    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=stress_report.csv"
        }
    )


if __name__ == "__main__":
    app.run()