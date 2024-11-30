Rachel Wu -- Pseudocode

JUPYTER NOTEBOOK PSEUDOCODE:
Import Libraries
    numpy, pandas for data processing
    matplotlib, seaborn for visualization
    scikit-learn, xgboost for Machine learning
    pickle to save and load the finished model

Load and Inspect Dataset (pandas)
    Display dataset shape, description, and information.
    Check for missing values in the dataset.

Prepare Dataset for model
    Drop irrelevant columns
    Fill missing values
    Make sure there are no missing values after filling them 

Visualization
    Plot bar charts for categorical variables grouped by loan approval status

Encode Categorical Variables
    Convert categorical data into numerical values
    Convert the encoded columns to integer type

Split Dataset into Training and Testing Sets
    Split into training and testing sets 
        
Train Models and Evaluate Performance

    Naive Bayes Classifier:
        Train the GaussianNB model 
            ->make predictions
        Calculate and display precision and accuracy
    Support Vector Machine:
        Tune hyperparameters
        Train for the best SVM model 
        evaluate
    XGBoost:
        Train an XGBClassifier with specified parameters.
        Evaluate model performance.
    Decision Tree Classifier
        Tune hyperparameters
        Train and evaluate the best decision tree model
    Random Forest Classifier
        Perform hyperparameter tuning using RandomizedSearchCV.
        Train and evaluate the model.
    Pick the best model

Save and Load Final Model:
    Save the trained best model into a file
    Load the saved model 
    Predictions on the test set


FLASK FILE:
Import Flask 
Import pickle

Initialize Flask App
Define Routes and Logic:
    Define a route "/" 
    Route function:
    Set prediction to None.
    Retrieve form data for the input features
    Convert input data to appropriate data types
    Arrange input data into a list to match the model's expected format
    Open and load the loan_model.pkl
    Use the trained model's predict method on the list
    Save the model's prediction result.
Render the index.html template
Pass the prediction result to it
Run the Application

HTML FILE: 
Set up the document
Create the head and included styling choices

Create the body and container for the form
Create the form with input fields for the input features

Set up conditional block to dynamically load result
