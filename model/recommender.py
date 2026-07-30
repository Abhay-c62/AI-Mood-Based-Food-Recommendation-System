import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "dataset", "food_dataset.csv")

data = pd.read_csv(csv_path)

def recommend_food(mood):
    result = data[data["Mood"] == mood]
    return result.to_dict(orient="records")