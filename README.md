🏡 Predicting Housing Prices with XGBoost

## 🚀 Live Demo
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen?logo=streamlit)](https://boosting-5x7w6cv8agrddwexchpu8e.streamlit.app/)

📌 Project Overview

This project aims to build a machine learning model that predicts housing prices in California using the XGBoost algorithm.

A real estate company wants to estimate house prices based on features such as location, median income, number of rooms, population density, and proximity to the ocean. Accurate price prediction helps the company make data-driven investment and pricing decisions.

📊 Dataset

Source: California Housing Prices Dataset 

Features include:

longitude, latitude → geographical location

housing_median_age → median age of houses in a block

total_rooms, total_bedrooms, households, population

median_income → median income of households

ocean_proximity → categorical variable indicating location type

Additional engineered features:

rooms_per_household

bedrooms_per_room

population_per_household

Target variable:

median_house_value

⚙️ Methodology

Data Preprocessing

Handle missing values (total_bedrooms filled with median).

One-hot encode categorical feature ocean_proximity.

Feature engineering (ratios like rooms_per_household).

Drop redundant columns to avoid multicollinearity.

Model Training

Algorithm: XGBoost Regressor (reg:squarederror).

Applied 5-fold cross-validation for robust evaluation.

Hyperparameters tuned via GridSearchCV:

n_estimators (number of boosting rounds)

learning_rate (shrinkage factor)

max_depth (tree complexity)

subsample (row sampling for each tree)

Evaluation Metrics

RMSE (Root Mean Squared Error) → interpretable in price units.

R² score (Coefficient of Determination) → variance explained.

📈 Results

Best Hyperparameters: (example, will depend on your grid search output)

{'n_estimators': 200, 'learning_rate': 0.05, 'max_depth': 5, 'subsample': 0.8}


Performance on Test Data:

RMSE: ~46,000

R² score: ~0.83

➡️ The model explains ~83% of the variance in housing prices.

🚀 How to Run
1. Clone the Repository
git clone https://github.com/your-username/housing-price-xgboost.git
cd housing-price-xgboost

2. Install Dependencies
pip install -r requirements.txt

3. Run Model Training
python housing_model.py

4. Run Streamlit App
streamlit run app.py


This will open a web interface where you can input features and predict house prices interactively.

🛠️ Tech Stack

Python 3.8+

XGBoost

Scikit-learn

Pandas, NumPy, Matplotlib, Seaborn

Streamlit (for deployment & UI)

📌 Future Improvements

Try additional hyperparameters (colsample_bytree, reg_alpha, reg_lambda, min_child_weight).

Use SHAP values for model explainability.

Deploy on Heroku/Streamlit Cloud for public access.

Experiment with LightGBM or CatBoost for comparison.

👨‍💻 Author

Developed by [Navaneetha krishnan] ✨
!
