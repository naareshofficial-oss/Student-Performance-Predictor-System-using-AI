import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------------------------------------------------
# Page Settings
# ---------------------------------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------
# Dark Theme Styling
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    text-align: center;
    color: white;
}

.metric-box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.markdown("# 🎓 Student Performance Predictor")
st.markdown("### Artificial Intelligence System for Academic Prediction")

st.markdown("---")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_student_data.csv")
    return df

df = load_data()

# Target
X = df.drop("pass", axis=1)
y = df["pass"]

# ---------------------------------------------------
# Train-Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------
# Train Models
# ---------------------------------------------------

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Predictions
y_pred_log = log_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

# Accuracy
log_acc = accuracy_score(y_test, y_pred_log)
rf_acc = accuracy_score(y_test, y_pred_rf)

best_model = log_model if log_acc > rf_acc else rf_model

# ---------------------------------------------------
# Model Performance Section
# ---------------------------------------------------

st.subheader("Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("Logistic Regression Accuracy", f"{round(log_acc*100,2)} %")

with col2:
    st.metric("Random Forest Accuracy", f"{round(rf_acc*100,2)} %")

if log_acc > rf_acc:
    st.success("Best Model Selected: Logistic Regression")
else:
    st.success("Best Model Selected: Random Forest")

st.markdown("---")

# ---------------------------------------------------
# Sidebar Input (Different Design)
# ---------------------------------------------------

st.sidebar.header("Enter Student Information")

input_values = []

for col in X.columns:
    val = st.sidebar.number_input(col, value=0)
    input_values.append(val)

predict_button = st.sidebar.button("Predict Performance")

# ---------------------------------------------------
# Prediction Section
# ---------------------------------------------------

if predict_button:

    input_data = pd.DataFrame([input_values], columns=X.columns)

    prediction = best_model.predict(input_data)
    probability = best_model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("The student is likely to PASS")
    else:
        st.error("The student is likely to FAIL")

    st.subheader("Probability of Passing")

    st.progress(float(probability))

    st.write(f"Prediction Confidence: **{round(probability*100,2)}%**")

st.markdown("---")

# ---------------------------------------------------
# Confusion Matrix
# ---------------------------------------------------

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, best_model.predict(X_test))

cm_df = pd.DataFrame(
    cm,
    columns=["Predicted Fail","Predicted Pass"],
    index=["Actual Fail","Actual Pass"]
)

st.dataframe(cm_df)

# ---------------------------------------------------
# Classification Report
# ---------------------------------------------------

st.subheader("Classification Report")

report = classification_report(
    y_test,
    best_model.predict(X_test),
    output_dict=True
)

st.dataframe(pd.DataFrame(report).transpose())

st.markdown("---")

st.markdown("### AI-Based Student Performance Prediction System")