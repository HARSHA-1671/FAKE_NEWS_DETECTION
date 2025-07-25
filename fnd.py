# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import string
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

# Step 2: Load the datasets
data_fake = pd.read_csv('/content/Fake.csv', on_bad_lines='skip', engine='python')
data_true = pd.read_csv('/content/True.csv')
print("Datasets loaded successfully.")

# Step 3: Add class labels
data_fake["class"] = 0
data_true['class'] = 1
print("Class labels added.")

# Step 4: Manually test the last 10 rows and remove them from the main dataframes
data_fake_manual_testing = data_fake.tail(10)
data_fake = data_fake[:-10] # More robust way to remove tail
data_true_manual_testing = data_true.tail(10)
data_true = data_true[:-10] # More robust way to remove tail

data_fake_manual_testing['class'] = 0
data_true_manual_testing['class'] = 1
print("Manual testing data separated.")

# Step 5: Merge the datasets
data_merge = pd.concat([data_fake, data_true], axis=0)
print("Datasets merged.")
display(data_merge.head())

# Step 6: Drop unnecessary columns
data = data_merge.drop(['title', 'subject', 'date'], axis=1)
print("Unnecessary columns dropped.")
print("Missing values:", data.isnull().sum().sum()) # Check for any missing values

# Step 7: Shuffle the data and reset index
data = data.sample(frac=1).reset_index(drop=True)
print("Data shuffled and index reset.")
display(data.head())

# Step 8: Define text preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', b'', text) # Removed b'' from here as it's not needed for string
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

print("Preprocessing function defined.")

# Step 9: Apply preprocessing to the text column
data['text'] = data['text'].apply(wordopt)
print("Text data preprocessed.")
display(data.head())

# Step 10: Split data into training and testing sets
x = data['text']
y = data['class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42) # Added random_state for reproducibility
print("Data split into training and testing sets.")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Step 11: Vectorize the text data using TfidfVectorizer
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)
print("Text data vectorized using TF-IDF.")

# Step 12: Train the models
print("Training models...")

LR = LogisticRegression()
LR.fit(xv_train, y_train)
print("Logistic Regression model trained.")

DT = DecisionTreeClassifier(random_state=42) # Added random_state
DT.fit(xv_train, y_train)
print("Decision Tree model trained.")

GB = GradientBoostingClassifier(random_state=42) # Added random_state
GB.fit(xv_train, y_train)
print("Gradient Boosting model trained.")

RF = RandomForestClassifier(random_state=42) # Added random_state
RF.fit(xv_train, y_train)
print("Random Forest model trained.")

# Step 13: Evaluate the models (Optional, already done in original notebook)
print("\nModel Evaluation:")
print("Logistic Regression Score:", LR.score(xv_test, y_test))
print("Decision Tree Score:", DT.score(xv_test, y_test))
print("Gradient Boosting Score:", GB.score(xv_test, y_test))
print("Random Forest Score:", RF.score(xv_test, y_test))

# Step 14: Save the models and vectorizer
joblib.dump(LR, 'logistic_regression_model.pkl')
joblib.dump(DT, 'decision_tree_model.pkl')
joblib.dump(GB, 'gradient_boosting_model.pkl')
joblib.dump(RF, 'random_forest_model.pkl')
joblib.dump(vectorization, 'tfidf_vectorizer.pkl')
print("\nModels and vectorizer saved successfully as .pkl files.")

# Step 15: Load the models and vectorizer in a new environment
# This part simulates loading in a new script or notebook
print("\nLoading models and vectorizer in a simulated new environment...")
try:
    loaded_lr_model = joblib.load('logistic_regression_model.pkl')
    loaded_dt_model = joblib.load('decision_tree_model.pkl')
    loaded_gb_model = joblib.load('gradient_boosting_model.pkl')
    loaded_rf_model = joblib.load('random_forest_model.pkl')
    loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')
    print("Models and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Make sure the .pkl model and vectorizer files are in the correct directory.")
    # Handle this error appropriately
    # exit()

# Step 16: Define functions for prediction with loaded models

def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

def manual_testing_loaded(news, vectorizer, lr_model, dt_model, gb_model, rf_model):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test['text'] = new_def_test["text"].apply(wordopt) # Use the same wordopt function
    new_x_test = new_def_test["text"]
    new_xv_test = vectorizer.transform(new_x_test) # Use the loaded vectorizer

    pred_LR = lr_model.predict(new_xv_test)
    pred_DT = dt_model.predict(new_xv_test)
    pred_GB = gb_model.predict(new_xv_test)
    pred_RF = rf_model.predict(new_xv_test)

    print("\nLR Predicition: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction:{}".format(output_lable(pred_LR[0]),
                                                                                                             output_lable(pred_DT[0]),
                                                                                                             output_lable(pred_GB[0]),
                                                                                                             output_lable(pred_RF[0])))
    return pred_LR[0], pred_DT[0], pred_GB[0], pred_RF[0]

def final_verdict_loaded(pred_lr, pred_dt, pred_gb, pred_rf):
    predictions = [pred_lr, pred_dt, pred_gb, pred_rf]
    counts = {0: 0, 1: 0}
    for pred in predictions:
        counts[pred] += 1

    if counts[0] > counts[1]:
        return "Final Verdict: Fake News"
    else:
        return "Final Verdict: Not A Fake News"

print("Prediction functions defined.")

# Step 17: Test with new news article using loaded models
if 'loaded_vectorizer' in locals() and 'loaded_lr_model' in locals(): # Check if models were loaded
    news_article = str(input("Enter the news article you want to test with loaded models: "))
    lr_pred, dt_pred, gb_pred, rf_pred = manual_testing_loaded(news_article, loaded_vectorizer, loaded_lr_model, loaded_dt_model, loaded_gb_model, loaded_rf_model)
    final_result = final_verdict_loaded(lr_pred, dt_pred, gb_pred, rf_pred)
    print(final_result)
else:
    print("Models and vectorizer were not loaded. Please run the loading cell.")
