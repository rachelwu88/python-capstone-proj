# Rachel Wu
# Flask File to connect to front end
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        Gender = int(request.form.get("Gender"))
        Married = int(request.form.get("Married"))
        Education = int(request.form.get("Education"))
        Self_Employed = int(request.form.get("Self_Employed"))
        ApplicantIncome = float(request.form.get("ApplicantIncome"))
        CoapplicantIncome = float(request.form.get("CoapplicantIncome"))
        LoanAmount = float(request.form.get("LoanAmount"))
        Loan_Amount_Term = float(request.form.get("Loan_Amount_Term"))
        Credit_History = int(request.form.get("Credit_History"))
        Property_Area = int(request.form.get("Property_Area"))

        test_data = [[Gender, Married, Education, Self_Employed, ApplicantIncome,
                      CoapplicantIncome, LoanAmount, Loan_Amount_Term,
                      Credit_History, Property_Area]]

        with open("loan_model.pkl", "rb") as file:
            trained_model = pickle.load(file)
        prediction = trained_model.predict(test_data)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
