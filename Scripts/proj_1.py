from os import path
import pandas as pd
import pprint as pp
import requests
import numpy as np

# This script is for data exploration and preprocessing for the late food delivery order prediction project.
def get_data():
    path = r'input/level2_food_delivery_late_prediction_project.xlsx'
    #get file data and at sheet name "llll" Scoring_Orders
    tdata = pd.read_excel(path, sheet_name="Train_Orders")
    return tdata


# Main function to run the data exploration and preprocessing steps.
def main():
    print("Getting data...")
    data = get_data()
    print("Data loaded successfully!")
    print(data.head())
    print(data.info())
    print(data.describe())
    #check for null values
    print(data.isnull().sum())
    #check for duplicates
    print(data.duplicated().sum())
    #check for unique values in each column
    for col in data.columns:
        print(f"{col}: {data[col].nunique()} unique values")