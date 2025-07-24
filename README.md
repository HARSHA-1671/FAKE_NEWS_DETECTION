# FAKE_NEWS_DETECTION

## About the Project

FAKE_NEWS_DETECTION is a machine learning-based project aimed at spotting fake news by classifying articles as either "FAKE" or "TRUE." In today’s fast-paced digital world, misinformation spreads quickly, and this project helps tackle that problem by using natural language processing and machine learning techniques to identify unreliable news content.

## What’s Inside

- Text cleaning and preprocessing to prepare news data.
- Feature extraction using methods like TF-IDF.
- Multiple classification algorithms to find the best fit (e.g., Logistic Regression, Decision Trees, Random Forests, Gradient Boosting).
- Easy-to-use testing functionality for manual input and predictions.

## Project Layout

```
FAKE_NEWS_DETECTION/
├── FND.ipynb            # Jupyter notebook with model building and analysis
├── fnd.py               # Python script with core functions
├── True.zip             # Dataset containing real news samples
├── Fake.zip             # Dataset containing fake news samples
├── manual_testing.csv   # For testing the model with your own news samples
└── README.md            # This file
```

## Datasets

- **True.zip:** Real news articles.
- **Fake.zip:** Fake news articles.
- **manual_testing.csv:** Your custom news for testing model predictions.

## Getting Started

### Hardware & Software

- Minimum 4GB RAM and Intel i3 processor or better.
- Around 500MB of free disk space.
- Python 3 installed (Jupyter Notebook recommended).

### Install Dependencies

Run this command to install necessary packages:

```bash
pip install pandas numpy matplotlib sklearn seaborn
```

## Running the Project

1. Clone the repo:

   ```bash
   git clone https://github.com/HARSHA-1671/FAKE_NEWS_DETECTION.git
   cd FAKE_NEWS_DETECTION
   ```

2. Unzip `True.zip` and `Fake.zip` in the project directory.

3. Launch the Jupyter Notebook:

   ```bash
   jupyter notebook FND.ipynb
   ```

4. Follow the notebook cells to preprocess data, train models, and test the results.

5. To test your own news articles, update `manual_testing.csv` and run the prediction sections.

## How It Works

- Input data is cleaned and prepared for analysis.
- Text data is transformed into numeric features (like TF-IDF vectors).
- Various machine learning models are trained to differentiate fake vs. real news.
- Performance is evaluated to pick the most accurate model.
- You can then test new news articles and get predictions instantly.

## Contributions

Feel free to fork this project, add your improvements, and submit pull requests. Your ideas and enhancements are welcome!

## License

This project is available under the MIT License.

## Credits

Created and maintained by HARSHA-1671.

This project is a straightforward yet effective approach to help reduce the spread of fake news by leveraging popular data science tools and techniques.
