import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.set_page_config(page_title="Campus Placement Prediction", layout="wide")
st.title("🎓 Campus Placement Prediction App")

# Load dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using sample dataset")
    df = pd.read_csv("campus_placement.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

if 'Placed' not in df.columns:
    st.error("❌ Dataset must have a 'Placed' column.")
else:
    X = df.drop("Placed", axis=1)
    y = df["Placed"]

    st.subheader("🔍 Correlation Heatmap")
    fig1, ax1 = plt.subplots(figsize=(8,6))
    sns.heatmap(X.corr(), annot=True, cmap="coolwarm", ax=ax1)
    st.pyplot(fig1)

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    st.subheader("📈 Model Performance")
    st.write(f"**Accuracy:** {acc:.3f}")
    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))

    st.subheader("🧩 Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig2, ax2 = plt.subplots(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax2)
    ax2.set_xlabel("Predicted")
    ax2.set_ylabel("Actual")
    st.pyplot(fig2)

    # Predict new data
    st.subheader("🔮 Predict Placement for New Student")
    input_data = {}
    for col in X.columns:
        min_val, max_val = float(X[col].min()), float(X[col].max())
        default = float(X[col].mean())
        input_data[col] = st.number_input(col, min_val, max_val, default)

    if st.button("Predict"):
        sample = [list(input_data.values())]
        pred = clf.predict(sample)[0]
        st.success(f"🎯 Prediction: **{'Placed' if pred == 1 else 'Not Placed'}**")
