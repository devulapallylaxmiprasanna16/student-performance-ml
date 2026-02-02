import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load cleaned dataset
data_path = "data/processed/student_cleaned.csv"
df = pd.read_csv(data_path)

# 2. Define features (X) and target (y)
X = df[['hours_studied', 'attendance_issues', 'internal_1', 'internal_2']]
y = df['performance']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model training completed")
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 6. Save model
joblib.dump(model, "models/student_performance_model.pkl")
print("✅ Model saved successfully")
