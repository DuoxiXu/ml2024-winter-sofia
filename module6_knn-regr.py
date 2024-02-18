import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        distances = np.sqrt(np.sum((self.X_train - X_test)**2, axis=1))
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_labels = self.y_train[nearest_indices]
        return np.mean(nearest_labels)

def get_points(N):
    points = []
    for i in range(N):
        x = float(input("Enter x coordinate for point {}: ".format(i + 1)))
        y = float(input("Enter y coordinate for point {}: ".format(i + 1)))
        points.append((x, y))
    return points

def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k should be less than or equal to N.")
        return

    points = get_points(N)
    X_train = np.array([point[0] for point in points])
    y_train = np.array([point[1] for point in points])

    knn_regressor = KNNRegression(k)
    knn_regressor.fit(X_train, y_train)

    X_test = float(input("Enter the value of X for prediction: "))
    y_pred = knn_regressor.predict(X_test)
    print("Predicted Y value:", y_pred)

if __name__ == "__main__":
    main()