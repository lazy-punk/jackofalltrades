from src.Models import LinearRegression
import pandas as pd
import numpy as np
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