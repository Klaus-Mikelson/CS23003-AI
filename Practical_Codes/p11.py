import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [35, 40, 50, 55, 65, 70, 75, 85]
}

df = pd.DataFrame(data)

df

X = df[['Hours']]
y = df['Marks']

# 3. Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create Linear Regression model
model = LinearRegression()

# 5. Train the model using training data
model.fit(X_train, y_train)

# 6. Predict output using test data
y_pred = model.predict(X_test)

print("Model trained successfully.")

# 7. Evaluate model using error metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = model.score(X, y)

print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'R-squared Score: {r2:.2f}')

# 8. Visualize results
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Hours vs Marks (Linear Regression)')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.legend()
plt.grid(True)
plt.show()

# Predict new values
new_hours = np.array([[9], [10]])
predictions = model.predict(new_hours)

for hour, pred in zip(new_hours.flatten(), predictions):
    print(f'Predicted marks for {hour} hours: {pred:.2f}')

"""### Interpretation of Results
- **Regression Line:** The red line shows a clear positive correlation between hours studied and marks obtained.
- **Error Metrics:** The MSE and MAE indicate how close the predictions are to the actual values. A lower value signifies a better fit.
- **Trend:** As 'Hours' increase, 'Marks' tend to increase linearly, suggesting that the model successfully captured the trend in the provided dataset.
"""

