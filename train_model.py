import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

# -----------------------------
# 1. Create Synthetic Dataset
# -----------------------------
np.random.seed(42)

data_size = 1000

data = {
    "sleep_hours": np.random.randint(4, 9, data_size),
    "work_hours": np.random.randint(6, 13, data_size),
    "screen_time": np.random.randint(2, 10, data_size),
    "physical_activity": np.random.randint(0, 3, data_size),
    "social_interaction": np.random.randint(0, 4, data_size),
    "caffeine_intake": np.random.randint(0, 6, data_size),
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Stress Label Logic
# -----------------------------
def stress_label(row):
    if (
        row["sleep_hours"] < 6
        or row["work_hours"] > 10
        or row["screen_time"] > 8
        or row["physical_activity"] == 0
    ):
        return 2  # High Stress
    elif row["sleep_hours"] < 7 or row["work_hours"] > 8:
        return 1  # Medium Stress
    else:
        return 0  # Low Stress

df["stress_level"] = df.apply(stress_label, axis=1)

# -----------------------------
# 3. Train Model
# -----------------------------
X = df.drop("stress_level", axis=1)
y = df["stress_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 4. Save Model
# -----------------------------
joblib.dump(model, "model/stress_model.pkl")

print("✅ Stress Prediction Model trained and saved successfully.")
