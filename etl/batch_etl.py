import pandas as pd
from datetime import datetime

RAW_FILE = "../generator/sensor_log.csv"
CLEAN_FILE = "cleaned_sensor_data.csv"

def clean_data():
    df = pd.read_csv(
        RAW_FILE,
        header=None,
        names=["timestamp", "temperature", "humidity", "air_quality"]
    )

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df.dropna(subset=["timestamp"], inplace=True)

    # Convert numbers
    df["temperature"] = df["temperature"].astype(float)
    df["humidity"] = df["humidity"].astype(float)
    df["air_quality"] = df["air_quality"].astype(int)

    # Remove unrealistic values
    df = df[
        (df["temperature"] > -20) & (df["temperature"] < 50) &
        (df["humidity"] >= 0) & (df["humidity"] <= 100) &
        (df["air_quality"] >= 0) & (df["air_quality"] <= 500)
    ]

    df.to_csv(CLEAN_FILE, index=False)
    print("ETL complete! Cleaned file saved as:", CLEAN_FILE)

if __name__ == "__main__":
    clean_data()
