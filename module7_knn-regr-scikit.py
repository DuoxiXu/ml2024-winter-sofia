import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Function to perform k-NN Regression
def k_nn_regression(X_train, y_train, k, X_test):
    # Create k-NN Regressor model
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    # Fit the model
    knn_regressor.fit(X_train, y_train)
    # Predict
    y_pred = knn_regressor.predict(X_test)
    return y_pred

# Read input N
N = int(input("Enter the number of data points (N): "))

# Read input k
k = int(input("Enter the value of k for k-NN Regression: "))

# Initialize arrays to store data points
X = np.zeros(N)
y = np.zeros(N)

# Read N (x, y) points
for i in range(N):
    x_val = float(input(f"Enter x value for point {i+1}: "))
    y_val = float(input(f"Enter y value for point {i+1}: "))
    X[i] = x_val
    y[i] = y_val

# Check if k <= N
if k <= N:
    # Read input X for prediction
    X_pred = np.array([[float(input("Enter x value for prediction: "))]])

    # Perform k-NN Regression
    y_pred = k_nn_regression(X, y, k, X_pred)

    # Output result
    print("Result of k-NN Regression (Y):", y_pred[0])

    # Calculate coefficient of determination (R^2)
    r_squared = r2_score(y, k_nn_regression(X, y, k, X))
    print("Coefficient of determination (R^2):", r_squared)
else:
    print("Error: k should be less than or equal to N.")