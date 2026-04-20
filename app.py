import streamlit as st
import pandas as pd
import joblib



# 🎨 BACKGROUND COLOR (ADD HERE)



# Page config

st.set_page_config(page_title="Smart Parking", page_icon="🚗", layout="centered")

# Load model
model = joblib.load("model.pkl")

# Title
st.title("Smart Parking Prediction System")
st.markdown("### Predict parking availability in real-time")

# Divider
st.markdown("---")

# Inputs
col1, col2 = st.columns(2)

with col1:
    hour = st.slider("🕒 Hour of Day", 0, 23)
    day = st.selectbox("📅 Day of Week", 
                       ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
    
with col2:
    entry = st.number_input("🚘 Entry Count", 0, 500)
    exit = st.number_input("🚗 Exit Count", 0, 500)

# Convert day to number
day_map = {
    "Monday":0,"Tuesday":1,"Wednesday":2,
    "Thursday":3,"Friday":4,"Saturday":5,"Sunday":6
}
day = day_map[day]

st.markdown("---")

# Predict button
if st.button("🔍 Predict Parking Status"):

    sample = pd.DataFrame([{
        "hour": hour,
        "day_of_week": day,
        "entry_count": entry,
        "exit_count": exit
    }])

    result = model.predict(sample)[0]

    # Display result nicely
    if result == 1:
        st.error("🚫 Parking is FULL")
        st.metric(label="Availability", value="0%")
    else:
        st.success("✅ Parking is AVAILABLE")
        st.metric(label="Availability", value="High")

# Footer
st.markdown("---")
st.caption("Built using Machine Learning 🚀")