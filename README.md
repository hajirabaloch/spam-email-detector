📧 Spam Email Detector

A Machine Learning-based web application that classifies emails as SPAM or NOT SPAM using Natural Language Processing (NLP) and supervised Machine Learning algorithms.

The project includes model training, evaluation, and a web-based interface where users can paste an email and receive a prediction.

---

📌 Project Overview

Email spam is a common problem where unwanted or fraudulent messages can reach users' inboxes.

This project uses Machine Learning and text classification techniques to automatically identify whether an email is SPAM or NOT SPAM.

The trained model is integrated into a web application using Flask, allowing users to test email messages through a simple interface.

---

🎯 Objectives

- Build a Machine Learning model for spam email classification.
- Convert email text into numerical features using TF-IDF.
- Compare multiple Machine Learning algorithms.
- Evaluate models using standard classification metrics.
- Save the best-performing trained pipeline.
- Deploy the trained model as a web application.
- Allow users to enter email text and receive a prediction.

---

🧠 Machine Learning Workflow

The project follows this workflow:

Email Dataset
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Train Multiple ML Models
     ↓
Model Evaluation
     ↓
Select Best Model
     ↓
Save Trained Pipeline
     ↓
Flask Web Application
     ↓
SPAM / NOT SPAM Prediction

---

📊 Dataset

The final training run used:

- Total samples: 2,956
- Ham (Not Spam): 2,473
- Spam: 483

The dataset contains email messages labeled as either spam or non-spam.

---

🔤 Feature Extraction

TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) was used to convert email text into numerical features that Machine Learning algorithms can process.

TF-IDF gives higher importance to words that are useful for distinguishing between different documents while reducing the importance of very common words.

---

🤖 Machine Learning Algorithms

Three classification algorithms were compared:

1. Logistic Regression

A linear classification algorithm commonly used for binary classification problems.

2. Naive Bayes

A probabilistic classification algorithm that is commonly used for text classification.

3. Linear SVM

A Support Vector Machine classifier that finds a decision boundary for separating different classes.

---

📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

Results

Model| Accuracy| Precision| Recall| F1-score
Logistic Regression| 0.9797| 1.0000| 0.8763| 0.9341
Naive Bayes| 0.9172| 1.0000| 0.4948| 0.6621
Linear SVM| 0.9831| 1.0000| 0.8969| 0.9457

The Linear SVM model achieved an F1-score of 0.9457 in the final evaluation and was selected for the deployed application.

---

💾 Saved Model

The complete trained pipeline was saved as:

spam_classifier.pkl

The saved pipeline contains the text feature transformation and trained classifier required to make predictions on new email text.

---

🌐 Web Application

The Machine Learning model was integrated into a Flask web application.

Users can:

1. Open the web application.
2. Paste an email message.
3. Click Check Email.
4. Receive a prediction:

🔴 SPAM

or

🟢 NOT SPAM

Live Demo

The current demo is hosted on PythonAnywhere:

https://hajirarahimbakhsh.pythonanywhere.com

«Hosting note: The current demo uses PythonAnywhere's free hosting and is available for one month.»

---

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- TF-IDF
- Logistic Regression
- Naive Bayes
- Linear SVM
- Flask
- HTML/CSS
- GitHub

---

📂 Project Structure

spam-email-detector/
│
├── app.py
├── flask_app.py
├── spam_classifier.pkl
├── requirements.txt
├── README.md
└── .gitignore

File Description

File| Description
"app.py"| Original Gradio-based application
"flask_app.py"| Flask web application used for deployment
"spam_classifier.pkl"| Saved trained Machine Learning pipeline
"requirements.txt"| Python dependencies
"README.md"| Project documentation
".gitignore"| Files excluded from Git

---

🚀 Installation

Clone the repository:

git clone https://github.com/hajirabaloch/spam-email-detector.git

Move into the project directory:

cd spam-email-detector

Install the required packages:

pip install -r requirements.txt

---

▶️ Running the Application

Run the Flask application:

python flask_app.py

Then open the local address provided by Flask in your browser.

---

🧪 Example

Spam Email

CONGRATULATIONS! You have been selected to receive a $1,000 cash prize!
Claim your FREE reward now before it expires.

Prediction:

🔴 SPAM

Normal Email

Hi Sarah,

I hope you are doing well.
Please send me the meeting notes when you get a chance.

Thank you.

Prediction:

🟢 NOT SPAM

---

⚠️ Limitations

- The model's predictions depend on the patterns present in the training dataset.
- Some unusual or ambiguous emails may be misclassified.
- The current live demo has a temporary one-month hosting period.
- The model is designed as an educational Machine Learning project and should not be treated as a complete production-grade email security system.

---

🔮 Future Improvements

Possible improvements include:

- Increasing the size and diversity of the dataset.
- Adding more advanced text preprocessing.
- Testing additional Machine Learning algorithms.
- Exploring Deep Learning and Transformer-based models.
- Improving the web interface.
- Adding prediction confidence and explanation features.
- Deploying the application on a long-term hosting platform.

---

👩‍💻 Author

Hajira Baloch

BS Data Science Student

University of Gwadar

---

📜 Project Purpose

This project was developed as a Machine Learning mini project to gain practical experience in:

- Natural Language Processing
- Text classification
- Machine Learning model training
- Model evaluation
- Flask application development
- Model deployment
- GitHub project documentation
