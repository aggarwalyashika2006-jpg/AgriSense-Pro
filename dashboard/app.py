import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="AgriSense Pro",
    page_icon="🌱",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}
.metric-container {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 AgriSense Pro")
st.caption("Premium IoT Smart Agriculture Monitoring Platform")

try:
    df = pd.read_csv("data/sensor_data.csv")

    latest = df.iloc[-1]

    soil = latest["Soil Moisture"]
    temp = latest["Temperature"]
    humidity = latest["Humidity"]
    water = latest["Water Level"]
    light = latest["Light Intensity"]

    # Farm Health Score
    health_score = 100

    if soil < 30:
        health_score -= 25

    if temp > 40:
        health_score -= 20

    if water < 20:
        health_score -= 25

    health_score = max(0, health_score)

    st.subheader("📊 Live Farm Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🌱 Soil Moisture", f"{soil}%")
    c2.metric("🌡 Temperature", f"{temp}°C")
    c3.metric("💧 Humidity", f"{humidity}%")
    c4.metric("🚰 Water Level", f"{water}%")

    c5, c6, c7 = st.columns(3)

    c5.metric("☀ Light Intensity", light)
    c6.metric("⚡ Pump Status", latest["Pump Status"])
    c7.metric("🎯 Farm Health", f"{health_score}/100")

    st.divider()

    left, right = st.columns(2)

    with left:

        fig_soil = go.Figure(go.Indicator(
            mode="gauge+number",
            value=soil,
            title={"text":"Soil Moisture"},
            gauge={"axis":{"range":[0,100]}}
        ))

        st.plotly_chart(fig_soil, use_container_width=True)

    with right:

        fig_water = go.Figure(go.Indicator(
            mode="gauge+number",
            value=water,
            title={"text":"Water Level"},
            gauge={"axis":{"range":[0,100]}}
        ))

        st.plotly_chart(fig_water, use_container_width=True)

    st.subheader("🚨 Smart Alerts")

    if soil < 30:
        st.error("Low Soil Moisture Detected")

    if temp > 40:
        st.warning("High Temperature Detected")

    if water < 20:
        st.error("Critical Water Level")

    if soil >= 30 and temp <= 40 and water >= 20:
        st.success("All Parameters Normal")

    st.divider()

    st.subheader("🤖 Smart Irrigation Recommendation")

    if soil < 30:
        st.error("START IRRIGATION IMMEDIATELY")
    else:
        st.success("No Irrigation Required")

    st.divider()

    st.subheader("📈 Sensor Trends")

    fig1 = px.line(df, y="Temperature", title="Temperature Trend")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(df, y="Soil Moisture", title="Soil Moisture Trend")
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.line(df, y="Humidity", title="Humidity Trend")
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.line(df, y="Water Level", title="Water Level Trend")
    st.plotly_chart(fig4, use_container_width=True)

    st.divider()

    st.subheader("📋 Historical Sensor Records")

    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Dashboard Error: {e}")