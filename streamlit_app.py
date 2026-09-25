import streamlit as st
import joblib

# Load trained model
model = joblib.load("spam_classifier.pkl")

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧"
)

st.title("📧 Spam Email Detector")
st.write("Paste an email below and the Machine Learning model will classify it.")

email = st.text_area(
    "Email Content",
    height=250,
    placeholder="Paste your email here..."
)

if st.button("🔍 Check Email"):

    if not email.strip():
        st.warning("Please paste an email first.")

    else:
        prediction = model.predict([email])[0]

        if prediction == 1:
            st.error("🔴 SPAM")
            st.write("The model classified this email as spam.")
        else:
            st.success("🟢 NOT SPAM")
            st.write("The model classified this email as a legitimate email.")

st.markdown("---")
st.caption(
    "Student Machine Learning project using TF-IDF + Linear SVM."
)