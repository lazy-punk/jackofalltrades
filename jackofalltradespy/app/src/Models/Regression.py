import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from tqdm import tqdm as tqdm

import sklearn.metrics as metrics

# Class for implementing Linear Regression
class LinearRegression:
      def __init__(self, X: pd.DataFrame , y: pd.Series, learning_rate : float = 0.03, epochs : int = 10000) -> None:
            """
            Initialize the LinearRegression object.

            Parameters:
            - X: Input features as a pandas DataFrame.
            - y: Target variable as a pandas Series.
            - learning_rate: Learning rate for gradient descent (default = 0.03).
            - epochs: Number of training iterations (default = 10000).
            """
            try:
                  self.X, self.y = np.array(X, dtype= np.float32), np.array(y, dtype = np.float32)
                  self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X / np.max(self.X), self.y, test_size=0.2, random_state=42)
                  self.learning_rate = learning_rate
                  self.epochs = epochs
            except Exception as e:
                  print("An error occurred during initialization:", str(e))

      def fit(self) -> None:
            """
            Train the linear regression model using gradient descent.
            """
            try:
                  self.m, self.n = self.X_train.shape
                  self.w = np.zeros(self.n)
                  self.b = 0
                  y_pred = np.dot(self.X_train, self.w) + self.b
                  self.cost = []
                  self.epoch = []
                  description = tqdm(range(self.epochs))
                  for i in description:
                        y_pred = np.dot(self.X_train, self.w) + self.b
                        dw = (1/self.m) * np.dot(self.X_train.T, (y_pred - self.y_train))
                        db = (1/self.m) * np.sum(y_pred - self.y_train)
                        self.w -= self.learning_rate * dw
                        self.b -= self.learning_rate * db
                        self.cost.append(np.mean(np.square(y_pred - self.y_train)))
                        self.epoch.append(i)
                        description.set_description(f"Cost: {self.cost[-1]}")

            except Exception as e:
                  print("An error occurred during fitting:", str(e))

      def predict(self, X_test: pd.DataFrame) -> np.ndarray:
            """
            Predict the target variable for the given input features.

            Parameters:
            - X_test: Input features for prediction as a pandas DataFrame.

            Returns:
            - Predicted target variable as a numpy array.
            """
            return np.dot(np.array(X_test , dtype = np.float32) / np.max(self.X), self.w) + self.b

      def plot_cost(self) -> None:
            """
            Plot the cost function over training iterations.
            """
            plt.plot(self.cost ,self.epoch)
            plt.show()

      def evaluate(self, X_test : np.ndarray, y_test : np.ndarray) -> None:
            """
            Evaluate the model using the R-squared metric.

            Parameters:
            - X_test: Test input features as a numpy array.
            - y_test: Test target variable as a numpy array.
            """
            print(metrics.r2_score(y_test, X_test))


"""
def main():
      # Create a pandas DataFrame with 3 features and a result
      data = {
            'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'Feature2': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
            'Feature3': [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
            'Result': [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
      }

      df = pd.DataFrame(data)

      # Create an instance of LinearRegression
      regression = LinearRegression(df[['Feature1', 'Feature2', 'Feature3']], df['Result'])

      # Fit the model
      regression.fit()

      # Predict using the test data
      X_test = pd.DataFrame({
            'Feature1': [21, 22, 23, 24, 25],
            'Feature2': [41, 42, 43, 44, 45],
            'Feature3': [61, 62, 63, 64, 65]
      })
      y_test = pd.DataFrame([81, 82, 83, 84, 85], dtype = np.float32)

      predictions = regression.predict(X_test)
      print(predictions)
      regression.evaluate(y_test, predictions)
      regression.plot_cost()


main()
"""

