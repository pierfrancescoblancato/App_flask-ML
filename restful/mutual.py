from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

#inizializzazione flask
app = Flask(__name__)

path = "restful/modello_mutuo.joblib"
try:
    # caricamento 
    model = joblib.load(path)
except FileNotFoundError:
    print(f"Error: file {path}'not found.")
    
@app.route('/')
def index():
    return render_template('index.html')
      
@app.route('/predict', methods = ['POST'])
def predict():
    
    if request.method == 'POST':
        try:
            dataclient = {
                'Gender': request.form['gender'],
                'Married': request.form['married'],
                'Dependents': 3 if request.form['dependents'] == "3+" else int(request.form['dependents']),
                'Education': request.form['education'],  
                'Self_Employed': request.form['self_employed'],  
                'ApplicantIncome': float(request.form['applicant_income']), 
                'CoapplicantIncome': float(request.form['coapplicant_income']),  
                'LoanAmount': float(request.form['loan_amount']),  
                'Loan_Amount_Term': float(request.form['loan_amount_term']),  
                'Credit_History': float(request.form['credit_history']),  
                'Property_Area': request.form['property_area'] 
            }
            
        except KeyError as k:
            print(f"Error: empty field: {k}")
            return render_template('index.html') 
        except ValueError as v:
            print(f"Error: Invalid data format: {v}")
            return render_template('index.html')
        try:
            #dataframe con la struttura usata nel training
            df = pd.DataFrame([dataclient])
            
            # esecuzione della predizione.
            result = model.predict(df)[0]
            
            if result == 1:
                return redirect(url_for('success'))
            else:
                return redirect(url_for('fail'))
            
        except Exception as e:
            print(f"Error: {e}")
            return render_template('index.html')

@app.route('/success', methods = ['GET'])
def success():
    return render_template('success.html')

@app.route('/fail', methods = ['GET'])
def fail():
    return render_template('fail.html')
    
# avvio del server web Flask
if __name__ == '__main__':
    app.run(debug=True)
    