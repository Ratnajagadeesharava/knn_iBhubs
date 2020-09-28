import numpy as np
import csv
import sys
import train
from validate import validate

"""
Predicts the target values for data in the file at 'test_X_file_path'.
Writes the predicted values to the file named "predicted_test_Y_knn.csv". It should be created in the same directory where this code file is present.
This code is provided to help you get started and is NOT a complete implementation. Modify it based on the requirements of the project.
"""

def import_data(test_X_file_path):
    test_X = np.genfromtxt(test_X_file_path, delimiter=',', dtype=np.float64, skip_header=1)
    return test_X


def predict_target_values(train_y,train_x):
    n=3
    k = train.predict_k_value(train_x,train_y,0.2,n)
    print(k)
    # predicted_y = train.classify_test_set(train_x,train_y,test_X,k,n)
    # print(predicted_y)
    # Write your code to Predict Target Variables
    # HINT: You can use other functions which you've already implemented in coding assignments.
    

def write_to_csv_file(pred_Y, predicted_Y_file_name):
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    with open(predicted_Y_file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()


def predict():
    # test_X = import_data()
    train_x  = import_data("train_X_knn.csv")
    train_x = train_x[1:]
    train_y = import_data("train_Y_knn.csv")
    # pred_Y = predict_target_values(train_y,train_x)
    predict_target_values(train_y, train_x)
    # write_to_csv_file(pred_Y, "predicted_test_Y_knn.csv")


if __name__ == "__main__":
    # test_X_file_path = sys.argv[1]
    predict()
    # predict(test_X_file_path)
    # Uncomment to test on the training data
    # validate(test_X_file_path, actual_test_Y_file_path="train_Y_knn.csv") 