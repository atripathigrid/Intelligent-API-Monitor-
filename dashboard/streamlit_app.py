import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Intelligent API Monitor",
    page_icon="📊",
    layout="wide"
)

BASE_URL = "http://127.0.0.1:8000"

# ✅ API KEY (IMPORTANT FIX)
HEADERS = {
    "x-api-key": "test_api_key"
}

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        color: #1f4e79;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="title">📊 Intelligent API Monitor Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Monitor Weather, Finance, Earthquake Data and Detect Anomalies in Real Time</div>',
    unsafe_allow_html=True
)

# Refresh button
if st.button("🔄 Refresh Data"):
    try:
        requests.get(f"{BASE_URL}/api/fetch-live", headers=HEADERS)
        st.success("Latest data fetched successfully")
    except:
        st.error("FastAPI server is not running")

try:
    # ✅ FIX: API KEY ADDED TO ALL REQUESTS
    weather = requests.get(f"{BASE_URL}/api/weather", headers=HEADERS).json()
    finance = requests.get(f"{BASE_URL}/api/finance", headers=HEADERS).json()
    earthquake = requests.get(f"{BASE_URL}/api/earthquake", headers=HEADERS).json()
    anomalies = requests.get(f"{BASE_URL}/api/anomalies", headers=HEADERS).json()

    weather_df = pd.DataFrame(weather)
    finance_df = pd.DataFrame(finance)
    earthquake_df = pd.DataFrame(earthquake)

    # Metrics Row
    st.markdown('<div class="section-title">📌 Latest Metrics</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        latest_temp = weather_df.iloc[-1]["temperature"] if not weather_df.empty else 0
        st.metric("🌡 Temperature", f"{latest_temp} °C")

    with col2:
        latest_usd = finance_df.iloc[-1]["usd_rate"] if not finance_df.empty else 0
        st.metric("💵 USD Rate", latest_usd)

    with col3:
        latest_quake = earthquake_df.iloc[-1]["magnitude"] if not earthquake_df.empty else 0
        st.metric("🌍 Earthquake Magnitude", latest_quake)

    st.divider()

    # Data Tables
    st.markdown('<div class="section-title">📂 API Data</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🌤 Weather", "💰 Finance", "🌎 Earthquake"])

    with tab1:
        st.dataframe(weather_df, use_container_width=True)

    with tab2:
        st.dataframe(finance_df, use_container_width=True)

    with tab3:
        st.dataframe(earthquake_df, use_container_width=True)

    st.divider()

    # Anomalies Section
    st.markdown('<div class="section-title">⚠ Detected Anomalies</div>', unsafe_allow_html=True)

    anomaly_list = anomalies.get("anomalies", [])

    if anomaly_list:
        for anomaly in anomaly_list:
            message = anomaly.get("message", "No message")

            if "temperature" in message.lower():
                st.error(f"🔥 {message}")
            elif "usd" in message.lower():
                st.warning(f"💰 {message}")
            elif "earthquake" in message.lower():
                st.error(f"🌍 {message}")
            else:
                st.warning(f"⚠ {message}")

            st.divider()
    else:
        st.success("No anomalies detected")

    st.divider()

    # Charts
    st.markdown('<div class="section-title">📈 Visual Insights</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if not weather_df.empty:
            st.subheader("Temperature Trend")
            st.line_chart(weather_df["temperature"])

    with col2:
        if not finance_df.empty:
            st.subheader("USD Rate Trend")
            st.line_chart(finance_df["usd_rate"])

    if not earthquake_df.empty:
        st.subheader("Earthquake Magnitude Trend")
        st.bar_chart(earthquake_df["magnitude"])

    st.divider()

    # Download Section
    st.markdown('<div class="section-title">⬇ Download Data</div>', unsafe_allow_html=True)

    export_response = requests.get(
        f"{BASE_URL}/api/export",
        headers=HEADERS
    )

    st.download_button(
        label="Download Exported Data",
        data=export_response.text,
        file_name="exported_data.txt",
        mime="text/plain"
    )

except Exception as e:
    st.error("Could not connect to FastAPI server. Make sure uvicorn is running.")
    st.code(str(e))