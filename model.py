import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

housing = pd.read_csv("housing.csv").dropna()

y = housing.median_house_value

features = ["housing_median_age", "total_rooms", "median_income", "longitude", "latitude"]
X = housing[features]

trainX, valX, trainy, valy = train_test_split(X, y, test_size=0.2, random_state=21)

house_model = LinearRegression()
house_model.fit(trainX, trainy)

prediction = house_model.predict(valX)
print("Linear Regression: ",mean_absolute_error(valy, prediction))
print("Model Coefficient: ", house_model.coef_)
print("Model Intercept: ", house_model.intercept_)
print("R2 score: ", r2_score(valy,prediction))
