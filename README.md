# 🧠 Employee Stress Analytics Dashboard

A production-ready **Machine Learning powered web application** that analyzes daily routine data to predict employee stress levels, explain contributing factors, and generate actionable wellness recommendations.

🌐 **Live Demo:**  
https://employee-stress-dashboard.onrender.com/

---

## 📌 Problem Statement

Employee stress and burnout are major challenges in modern workplaces.  
This project aims to provide a **data-driven approach** to assess stress levels based on daily habits and routines, enabling early intervention and informed decision-making.

---

## 🚀 Key Features

### 🧠 Machine Learning & Intelligence
- Stress Level Prediction (**Low / Medium / High**)
- Prediction Confidence Score (%)
- Explainable AI using **Feature Importance**
- Personalized Wellness Recommendations

### 📊 Analytics & Tracking
- Session-based **Stress History Timeline (Table View)**
- Time-stamped prediction tracking
- HR-ready data representation

### 📤 Reporting
- **CSV Export** of stress history for analysis and reporting

### 🎨 User Experience
- Professional SaaS-style UI
- Optimized input intake (number inputs & dropdowns)
- Clean layout with smooth animations
- Mobile-friendly responsive design

---

## 🛠️ Tech Stack

**Backend:** Python, Flask, Scikit-learn, Joblib  
**Frontend:** HTML5, CSS3, Vanilla JavaScript  
**ML Model:** Decision Tree Classifier  
**Deployment:** Render, Gunicorn  

---

## 🧪 How It Works

1. User enters daily routine data (sleep, work hours, screen time, etc.)
2. The ML model predicts stress level with confidence score
3. Feature importance explains contributing factors
4. Personalized recommendations are generated
5. Predictions are stored in a session-based history
6. Stress history can be exported as a CSV report

---

## 📂 Project Structure

```
employee-stress-dashboard/
├── app.py
├── train_model.py
├── model/
│   └── stress_model.pkl
├── templates/
│   └── index.html
├── static/
│   ├── css/style.css
│   └── js/script.js
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/employee-stress-dashboard.git
cd employee-stress-dashboard
pip install -r requirements.txt
python app.py
```

Open in browser: `http://127.0.0.1:5000/`

---

## 📈 Future Enhancements

- Weekly stress trend visualization
- HR dashboard with aggregated insights
- Burnout risk detection
- Role-based views (Employee / HR)
- PDF report export
- Database-backed persistent storage

---

## 🎯 Why This Project Matters

- End-to-end ML application development
- Explainable AI principles
- Clean backend–frontend integration
- Production deployment experience
- Product-oriented problem solving

---

## 📬 Feedback & Suggestions

Feedback and ideas are welcome. This project is actively evolving as part of a long-term learning roadmap.

---

**Author:** Abhiuday Pratap Singh
