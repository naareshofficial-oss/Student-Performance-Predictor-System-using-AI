# 🎓 Student Performance Predictor

## Project Overview

The **Student Performance Predictor** is an AI-based machine learning
application developed using Python. It predicts whether a student is
likely to pass or fail based on academic, personal, family, and
school-related information.

The application uses a Streamlit web interface so users can enter
student information and view prediction results interactively.

## Objectives

-   Predict student academic outcomes (pass or fail).
-   Apply and compare two machine learning classification algorithms.
-   Display model evaluation results.
-   Provide an interactive interface for entering student information.

## Technologies Used

  Technology                 Purpose
  -------------------------- ------------------------------------------------
  Python                     Main programming language
  Streamlit                  Web application interface
  Pandas                     Dataset loading and data manipulation
  Scikit-learn               Machine learning model training and evaluation
  Logistic Regression        Classification algorithm
  Random Forest Classifier   Classification algorithm

## Machine Learning Algorithms

### 1. Logistic Regression

A classification algorithm used to estimate whether a student is likely
to pass or fail.

### 2. Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees to
classify student performance.

The application trains both models, compares their accuracy on a test
dataset, and selects the model with the higher accuracy for making
predictions.

## Main Features

-   Interactive student information input.
-   Student pass/fail prediction.
-   Prediction confidence / probability of passing.
-   Logistic Regression accuracy display.
-   Random Forest accuracy display.
-   Automatic selection of the model with higher test accuracy.
-   Confusion matrix.
-   Classification report.

## Project Structure

``` text
STUDENT PERFORMANCE PREDICTOR/
│
├── app.py
├── cleaned_student_data.csv
└── README.md
```

The project ZIP contains the Python script and CSV dataset. The
filenames should be adjusted as described below before running the
application.

## Dataset

The application uses `cleaned_student_data.csv`.

The dataset contains student-related attributes such as:

-   School and demographic information
-   Family and parental education information
-   Study time and travel time
-   Previous failures and absences
-   First, second, and final period grades (`G1`, `G2`, `G3`)
-   Target column: `pass`

The `pass` column is the value the machine learning models learn to
predict. The other columns are used as input features.

**Note:** The dataset contains encoded categorical values. The
application currently uses numeric input fields for all features, so
enter values using the dataset's encoding and value ranges.

## How to Run the Project (Windows)

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

During installation, select **Add Python to PATH**.

### Step 2: Extract the Project

Extract the ZIP file to a location on your computer.

For example:

``` text
C:\Users\YourName\Desktop\STUDENT PERFORMANCE PREDICTOR
```

### Step 3: Check the Files

Make sure the name of the Python file and dataset is similar.
Make sure both files are in the same project folder.

### Step 4: Open the Project in VS Code

1.  Open Visual Studio Code.
2.  Select **File → Open Folder**.
3.  Select the `STUDENT PERFORMANCE PREDICTOR` folder.
4.  Open the VS Code terminal using **Terminal → New Terminal**.

### Step 5: Install the Required Libraries

Run this command in the terminal:

``` bash
python -m pip install streamlit pandas scikit-learn
```

If your computer uses the `py` command instead, run:

``` bash
py -m pip install streamlit pandas scikit-learn
```

### Step 6: Run the Application

In the terminal, make sure you are inside the project folder, then run:

``` bash
python -m streamlit run app.py
```

Alternatively:

``` bash
py -m streamlit run app.py
```

### Step 7: Open the Application

Streamlit should open the application in your browser automatically.

If it does not, open this address manually:

``` text
http://localhost:8501
```

### Step 8: Make a Prediction

1.  Look at the sidebar on the left.
2.  Enter the student information in the input fields.
3.  Click **Predict Performance**.
4.  View the prediction result:
    -   Likely to PASS
    -   Likely to FAIL
5.  Review the probability of passing and the model evaluation results.

## Model Evaluation

The application displays the following evaluation metrics:

-   **Accuracy:** The proportion of test predictions that are correct.
-   **Confusion Matrix:** Compares actual outcomes with predicted
    outcomes.
-   **Classification Report:** Displays precision, recall, F1-score, and
    support for each class.

The displayed results are calculated when the application runs using the
supplied dataset and the configured train-test split. Actual accuracy
may vary if the dataset or model settings change.

## Important Notes

-   Keep `app.py` and `cleaned_student_data.csv` in the same folder.
-   The dataset must contain a column named `pass`.
-   The application requires Python and the listed Python libraries.
-   The application trains the models when it runs; it does not require
    a separately saved model file.
-   The prediction is a machine learning estimate, not a guarantee of a
    student's actual academic result.
-   The current application uses all columns other than `pass` as input
    features, including `G3` (final grade). If the aim is to predict
    performance before the final grade is known, review the features and
    remove `G3` to avoid using information that would not yet be
    available.

## Author

**Project Name:** Student Performance Predictor\
**Project Type:** Artificial Intelligence / Machine Learning\
**Application:** Streamlit Web Application
