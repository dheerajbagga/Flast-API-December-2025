from flask import Flask, request, jsonify
import pickle
app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "<h1>Welcome to the Loan Management System</h1>"
    
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        loan_request = request.get_json()
        if loan_request['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1
        if loan_request['Married'] == "Unmarried":
            Married = 0
        else:
            Married = 1
        ApplicantIncome = loan_request['ApplicantIncome']
        LoanAmount = loan_request['LoanAmount']
        credit_history = loan_request['Credit_History']

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, credit_history]
        prediction = model.predict([input_data])
        if prediction[0] == 0:
            prediction = 'Rejected'
        else:
            prediction = 'Approved'
        
        return {"The predicted loan status is": prediction}

        #prediction = model.predict(data)
        #return f"The predicted loan status is: {prediction}"
        #return f"The predicted loan status wiill be here"
    return jsonify({
        "message": "Send a POST request to this endpoint with the following JSON format to get a loan prediction:",
        "example_request": {
            "Gender": "Male",
            "Married": "Married",
            "ApplicantIncome": 5000,
            "LoanAmount": 100,
            "Credit_History": 1
        }
    })

if __name__ == '__main__':
    app.run(debug=True)