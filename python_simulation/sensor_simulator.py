import random
import pandas as pd
import os
from datetime import datetime

os.makedirs("data", exist_ok=True)

csv_file = "data/sensor_data.csv"

soil = random.randint(10,100)
temp = random.randint(20,45)
humidity = random.randint(30,90)
light = random.randint(100,1000)
water = random.randint(10,100)

pump = "OFF"
alerts = []

if soil < 30:
    pump = "ON"
    alerts.append("Low Soil Moisture")

if temp > 40:
    alerts.append("High Temperature")

if water < 20:
    alerts.append("Low Water Level")

if len(alerts) == 0:
    alerts.append("Normal")

row = {
    "Timestamp": datetime.now(),
    "Soil Moisture": soil,
    "Temperature": temp,
    "Humidity": humidity,
    "Light Intensity": light,
    "Water Level": water,
    "Pump Status": pump,
    "Alert": " | ".join(alerts)
}

df = pd.DataFrame([row])

if not os.path.exists(csv_file):
    df.to_csv(csv_file, index=False)
else:
    df.to_csv(csv_file, mode="a", index=False, header=False)

print("\n===== AGRISENSE PRO =====")
print(df)