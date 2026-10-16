# Loan Approval Predictor: Flask + Machine Learning

A web application that integrates a trained **scikit-learn** model into a **Flask** app. Users fill in a loan application form, and the app predicts whether the mortgage would be **approved or rejected** in real time.

Built as a final project for my Programming 2 course, it shows how to take a Machine Learning model from a notebook to a working web service.

## How It Works

1. The user opens the home page and fills in the application form
2. Flask collects the data and converts it to the correct types
3. The data is arranged in a **pandas DataFrame** with the columns the model expects
4. The pre-trained model (`.joblib`) returns a prediction
5. The user is redirected to an **approval** or **rejection** page

## The Model

The exported `modello_mutuo.joblib` is a complete **scikit-learn `Pipeline`**, so the app doesn't need to apply any preprocessing manually:

| Step | Details |
|---|---|
| Numeric features | Median imputation → `StandardScaler` |
| Categorical features | Most-frequent imputation → `OneHotEncoder` (unknown values ignored) |
| Classifier | `LogisticRegression` |

**Input features:** gender, marital status, dependents, education, self-employment, applicant income, co-applicant income, loan amount, loan term, credit history, property area.

The app only builds the DataFrame and calls `predict()`. Because the whole pipeline is a single artifact, training and serving can't drift apart.

## Tech Stack

- **Python 3**
- **Flask**: routing and request handling
- **scikit-learn**: the trained model (loaded via `joblib`)
- **pandas**: building the model input
- **Jinja2 / HTML**: templates

## Architecture (MVT)

- **Model**: loading of the `.joblib` pipeline and the prediction logic
- **View**: Flask routes (`/`, `/predict`, `/success`, `/fail`)
- **Template**: `index.html` (form), `success.html`, `fail.html`

## What This Project Demonstrates

- Deploying a **trained ML pipeline** inside a web application
- Mapping HTML form fields to the **exact feature schema** the model expects, with type conversion (e.g. `"3+"` dependents → `3`)
- Using the **Post/Redirect/Get** pattern for prediction results
- **Error handling** for missing model files, missing fields and invalid input
- Clean separation between model loading, prediction, HTTP handling and rendering

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the app
python mutual.py
```

Then open **http://127.0.0.1:5000**.

> The model is loaded from `restful/modello_mutuo.joblib`. Make sure the file is in that folder, or update the `path` variable in `mutual.py`.

## Project Structure

```
├── mutual.py                 # Flask app: model loading, routes, prediction
├── requirements.txt
├── restful/
│   └── modello_mutuo.joblib  # Pre-trained scikit-learn pipeline
└── templates/
    ├── index.html            # Application form
    ├── success.html          # Loan approved
    └── fail.html             # Loan rejected
```

## Possible Improvements

- Show the prediction probability, not only approved/rejected
- Show an error message on the form when the input is invalid
- Add CSS styling and client-side validation
- Add unit tests for the prediction logic
- Containerize with Docker and deploy online

## Disclaimer

This is an educational project. The model is not intended for real credit decisions.

## About Me

I'm a developer focused on Python, web development and Machine Learning, open to internships and junior roles.

📧 pblancato@stevejobs.academy
