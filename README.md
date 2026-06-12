🌱 AgriSense Pro - IoT Smart Agriculture Monitoring System
📌 Project Overview

AgriSense Pro is an IoT-based Smart Agriculture Monitoring System designed to monitor critical environmental conditions affecting crop growth. The system collects data from multiple sensors such as soil moisture, temperature, humidity, water level, and light intensity, analyzes the data, and provides intelligent irrigation recommendations.

This project demonstrates the application of IoT, Embedded Systems, Automation, and Data Analytics in modern agriculture to improve productivity, reduce water wastage, and support smart farming practices.

🎯 Problem Statement

Traditional farming methods often depend on manual monitoring of environmental conditions, leading to:

Water wastage
Delayed irrigation decisions
Reduced crop yield
Inefficient resource utilization
Increased operational costs

AgriSense Pro addresses these challenges by providing real-time monitoring, automated decision-making, and visual analytics for farm management.

🚀 Key Features
🌱 Environmental Monitoring
Soil Moisture Monitoring
Temperature Monitoring
Humidity Monitoring
Water Level Monitoring
Light Intensity Monitoring
🤖 Smart Automation
Automatic Irrigation Recommendation
Pump ON/OFF Control Simulation
Threshold-Based Alert System
📊 Data Analytics
Farm Health Score
Historical Data Analysis
Trend Visualization
Sensor Data Logging
📈 Dashboard
Interactive Streamlit Dashboard
Real-Time Sensor Metrics
Plotly Charts & Gauges
Smart Alerts Panel
🔧 IoT Simulation
Arduino UNO Simulation
Wokwi Circuit Design
Virtual Sensor Data Generation
Serial Monitor Output
🏗 System Architecture
Sensors
│
├── Soil Moisture Sensor
├── DHT22 Temperature Sensor
├── DHT22 Humidity Sensor
├── LDR Light Sensor
└── Water Level Sensor
        │
        ▼
Arduino UNO
        │
        ▼
Data Processing Layer
        │
        ├── Threshold Analysis
        ├── Alert Generation
        ├── Pump Control Logic
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
🔄 Workflow
Sensor Readings
      │
      ▼
Arduino Processing
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
Data Logging
      │
      ▼
Dashboard Visualization
🛠 Tech Stack
Hardware / Simulation
Arduino UNO
DHT22 Sensor
Soil Moisture Sensor
Water Level Sensor
LDR Sensor
LED (Pump Indicator)
Wokwi Simulator
Software
Python
Streamlit
Plotly
Pandas
NumPy
Tools
Git
GitHub
VS Code
📂 Project Structure
AgriSense-Pro/
│
├── arduino_code/
│   └── smart_agriculture.ino
│
├── python_simulation/
│   └── sensor_simulator.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── sensor_data.csv
│
├── images/
│   ├── circuit_diagram.png
│   ├── dashboard.png
│   ├── serial_monitor.png
│   ├── pump_on.png
│   └── alerts.png
│
├── outputs/
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
⚙ Installation
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
▶ Running the Project
Generate Sensor Data
python python_simulation/sensor_simulator.py
Run Dashboard
streamlit run dashboard/app.py
🔌 Arduino Circuit Components
Component	Purpose
Arduino UNO	Main Controller
DHT22	Temperature & Humidity
Soil Moisture Sensor	Soil Condition Monitoring
Water Level Sensor	Tank Monitoring
LDR Sensor	Light Intensity Detection
LED	Pump Simulation
🚨 Alert Conditions
Low Soil Moisture
Soil Moisture < 30%

Action:

Pump ON
Start Irrigation
High Temperature
Temperature > 40°C

Action:

High Temperature Alert
Low Water Level
Water Level < 20%

Action:

Low Water Level Alert
🎯 Farm Health Score

The Farm Health Score evaluates overall farm conditions using:

Soil Moisture
Temperature
Water Level
Score Range
Score	Status
90-100	Excellent
70-89	Good
50-69	Average
Below 50	Needs Attention
📊 Dashboard Features
KPI Cards
Soil Moisture
Temperature
Humidity
Water Level
Light Intensity
Pump Status
Farm Health Score
Charts
Temperature Trend
Humidity Trend
Soil Moisture Trend
Water Level Trend
Gauges
Soil Moisture Gauge
Water Level Gauge
📚 Learning Outcomes

Through this project, I learned:

Internet of Things (IoT)
Sensor Integration
Embedded Systems
Automation Logic
Smart Agriculture Concepts
Python Programming
Dashboard Development
Data Visualization
Git & GitHub
🔮 Future Enhancements
ESP32 Integration
MQTT Communication
Cloud Deployment
SQLite Database
Weather API Integration
Email Notifications
SMS Alerts
AI-Based Irrigation Prediction
Mobile Application
💼 Skills Demonstrated
IoT Development
Embedded Systems
Python Programming
Data Analytics
Automation Systems
Streamlit Development
Plotly Visualization
Arduino Programming
Git Version Control
GitHub Project Management
👨‍💻 Author

Yashika Aggarwal
Link-https://agrisense-pro-hpzwtn8dqxqfwchvfjgvqy.streamlit.app/
