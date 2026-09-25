"""
Spam Email Detector
====================
A Gradio web application that uses a trained Machine Learning model
to classify an email as SPAM or NOT SPAM.

Model:
- TF-IDF text features
- Linear SVM classifier
- Trained on the Apache SpamAssassin public email corpus
"""

import os
import joblib
import gradio as gr
# --------------------------------------------------
# Load trained model
# --------------------------------------------------

MODEL_PATH = "spam_classifier.pkl"

pipeline = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict_email(email_text):
    # Check if the user entered anything
    if not email_text or not email_text.strip():
        return "⚠️ Please paste an email first.", ""

    # Make prediction
    prediction = pipeline.predict([email_text])[0]

    # Convert prediction into human-readable result
    if prediction == 1:
        result = "🔴 SPAM"
        details = "The model classified this email as spam."
    else:
        result = "🟢 NOT SPAM"
        details = "The model classified this email as a legitimate email."

    return result, details


# --------------------------------------------------
# Create Gradio interface
# --------------------------------------------------

with gr.Blocks(title="Spam Email Detector") as demo:

    gr.Markdown(
        """
        # 📧 Spam Email Detector

        Paste an email below and the Machine Learning model will
        predict whether it is **SPAM** or **NOT SPAM**.

        **Model:** TF-IDF + Linear SVM  
        **Dataset:** Apache SpamAssassin Public Email Corpus
        """
    )

    email_input = gr.Textbox(
        label="Email Content",
        placeholder="Paste the email text here...",
        lines=12
    )

    check_button = gr.Button(
        "🔍 Check Email",
        variant="primary"
    )

    result_output = gr.Textbox(
        label="Prediction",
        interactive=False
    )

    details_output = gr.Textbox(
        label="Details",
        interactive=False
    )

    check_button.click(
        fn=predict_email,
        inputs=email_input,
        outputs=[result_output, details_output]
    )

    gr.Markdown(
        """
        ---
        **Note:** This is a student Machine Learning project.
        The model was trained using the Apache SpamAssassin public
        email corpus.
        """
    )


# --------------------------------------------------
# Run application
# --------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    demo.launch(server_name="0.0.0.0", server_port=port)