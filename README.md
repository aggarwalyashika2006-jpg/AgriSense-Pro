# 🌱 AgriSense Pro - IoT Smart Agriculture Monitoring Platform

## 📌 Overview

AgriSense Pro is an IoT-inspired Smart Agriculture Monitoring Platform designed to monitor environmental conditions and assist in intelligent irrigation decisions.

The platform simulates agricultural sensor data, analyzes farm conditions, generates alerts, logs historical data, and visualizes key metrics through an interactive Streamlit dashboard.

This project demonstrates concepts used in:

* Internet of Things (IoT)
* Smart Farming
* Precision Agriculture
* Sensor Data Monitoring
* Automation Systems
* Data Analytics
* Dashboard Development

---

## 🎯 Problem Statement

Traditional farming often relies on manual observation and fixed irrigation schedules.

This can lead to:

* Water wastage
* Over-irrigation
* Under-irrigation
* Delayed response to environmental changes
* Reduced crop productivity

AgriSense Pro addresses these challenges by monitoring simulated sensor data and providing intelligent irrigation recommendations.

---

## 🚀 Features

### Smart Monitoring

* Soil Moisture Monitoring
* Temperature Monitoring
* Humidity Monitoring
* Light Intensity Monitoring
* Water Level Monitoring

### Automation

* Automatic Pump ON/OFF Logic
* Smart Irrigation Recommendation
* Alert Generation

### Analytics

* Farm Health Score
* Historical Sensor Tracking
* Trend Analysis
* Interactive Visualizations

### Dashboard

* Real-Time Dashboard
* KPI Cards
* Gauge Charts
* Interactive Graphs
* Alert Panel

---

## 🏗 System Architecture

```text
Sensors
│
├── Soil Moisture Sensor
├── Temperature Sensor
├── Humidity Sensor
├── Light Sensor
└── Water Level Sensor
        │
        ▼
Data Collection Layer
        │
        ▼
Processing Engine
        │
        ├── Threshold Analysis
        ├── Pump Control Logic
        ├── Alert Generation
        └── Farm Health Score
        │
        ▼
Data Storage (CSV)
        │
        ▼
Streamlit Dashboard
        │
        ▼
Farmer / User
```

---

## 🔄 Workflow

```text
Sensor Data
     │
     ▼
Data Processing
     │
     ▼
Threshold Checking
     │
     ▼
Alert Generation
     │
     ▼
Pump Control Decision
     │
     ▼
Dashboard Visualization
```

---

## 🛠 Technologies Used

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Visualization

* Streamlit
* Plotly

### Storage

* CSV Files

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
AgriSense-Pro/
│
├── dashboard/
│   └── app.py
│
├── python_simulation/
│   └── sensor_simulator.py
│
├── data/
│   └── sensor_data.csv
│
├── outputs/
│
├── images/
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

### Generate Sensor Data

```bash
python python_simulation/sensor_simulator.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Dashboard Components

### KPI Metrics

* Soil Moisture
* Temperature
* Humidity
* Water Level
* Light Intensity
* Pump Status
* Farm Health Score

### Visualizations

* Soil Moisture Gauge
* Water Level Gauge
* Temperature Trend
* Soil Moisture Trend
* Humidity Trend
* Water Level Trend

### Alerts

* Low Soil Moisture Alert
* High Temperature Alert
* Low Water Level Alert

---

## 🤖 Smart Irrigation Logic

```python
if soil_moisture < 30:
    pump = "ON"
else:
    pump = "OFF"
```

### Recommendation Engine

```text
Low Soil Moisture
→ Start Irrigation

Normal Moisture
→ No Irrigation Required
```

---

## 🎯 Farm Health Score

Farm Health Score is calculated based on:

* Soil Moisture
* Temperature
* Water Level

Score Range:

```text
100 = Excellent

80–99 = Good

60–79 = Moderate

Below 60 = Needs Attention
```

---

## 📈 Future Enhancements

* SQLite Database Integration
* PDF Report Generation
* Email Alerts
* Weather API Integration
* MQTT Communication
* ThingSpeak Cloud Dashboard
* ESP32 Integration
* Mobile Notifications
* AI-Based Irrigation Prediction

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* IoT System Design
* Sensor Data Processing
* Automation Logic
* Dashboard Development
* Data Visualization
* Python Programming
* Version Control using Git
* GitHub Project Management

---

## 💼 Skills Demonstrated

* Python
* Streamlit
* Plotly
* Pandas
* IoT Concepts
* Smart Agriculture
* Data Analytics
* Dashboard Development
* Automation Systems
* Git & GitHub

---

## 👨‍💻 Author

YASHIKA

Link=https://agrisense-pro-hpzwtn8dqxqfwchvfjgvqy.streamlit.app/

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
