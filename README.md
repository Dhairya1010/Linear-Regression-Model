# 🏠 California Housing Price Prediction using Linear Regression

## 📌 Project Overview
This project applies **Linear Regression** to predict median house values using the California Housing dataset.  
The focus is not only on prediction accuracy, but on **understanding when linear regression works, when it fails, and why**.

The project follows a structured machine learning workflow:
- Feature selection
- Model training
- Evaluation
- Diagnostic analysis

---

## 🎯 Objective
- Predict `median_house_value`
- Use Linear Regression as a **baseline model**
- Evaluate performance using MAE and R²
- Diagnose underfitting and feature limitations

---

## 📂 Dataset
- **Dataset:** California Housing
- **Target Variable:** `median_house_value`
- **Missing values:** Removed using `.dropna()`

---

## 🧪 Methodology

### 1️⃣ Feature Selection (Final Model)
The final model uses the following features:

- `housing_median_age`
- `total_rooms`
- `median_income`
- `latitude`
- `longitude`

These were selected incrementally to observe how model performance changes and to identify key predictors.

---

### 2️⃣ Train / Test Split
The dataset is split into training and validation sets:

- **Training set:** 80%
- **Validation set:** 20%
- **Random state:** 21 (for reproducibility)

---

### 3️⃣ Model Training
A standard **Linear Regression** model from `scikit-learn` is trained on the selected features.

---

### 4️⃣ Evaluation Metrics
The model is evaluated using:
- **Mean Absolute Error (MAE)**
- **R² Score**

---

## 📊 Results

| Metric | Value |
|------|------|
| MAE | ~$53,784 |
| R² Score | ~0.60 |

### Interpretation:
- The model explains approximately **60% of the variance** in house prices.
- Predictions are off by **~$54k on average**.
- This performance is considered **strong for a basic linear regression model**.

---

## 🔍 Coefficient Interpretation (Key Insights)

- **Median Income:**  
  Strongest positive predictor of house prices.

- **Latitude & Longitude:**  
  Capture spatial effects such as proximity to high-value coastal areas.

- **Housing Median Age:**  
  Acts as a proxy for location; its influence decreases once spatial features are included.

- **Total Rooms:**  
  Has limited impact due to lack of scaling and feature engineering.

---

## ❗ Model Diagnosis

### ✅ Strengths
- Simple and interpretable
- Clear feature impact
- Strong baseline performance

### ❌ Limitations
- Underfits complex, non-linear relationships
- Cannot model feature interactions
- Performance plateaus despite adding features

➡️ **Linear Regression reaches its natural limit on this problem**

---

## 🧠 Key Takeaways
- Linear Regression is best used as a **baseline model**
- Feature selection matters more than model complexity
- Location and income dominate housing prices
- More complex models are required for higher accuracy

---

## 🚀 Future Improvements
- Apply **Decision Tree Regression**
- Compare with **Random Forest**
- Perform feature engineering (e.g., rooms per household)
- Handle non-linear relationships explicitly

---

## 🏁 Conclusion
Linear Regression provides a solid and interpretable baseline for housing price prediction, but it underfits the complex and non-linear nature of real estate data. More advanced models are required for improved predictive performance.
