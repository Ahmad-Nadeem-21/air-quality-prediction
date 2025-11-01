import streamlit as st
import pandas as pd
import joblib
import os

st.title("🌫️ Air Quality Prediction App")
st.write("Predict CO concentration using different machine learning models.")

model_dir = "models"
os.makedirs(model_dir, exist_ok=True)
available_models = [f for f in os.listdir(model_dir) if f.endswith(".pkl")]

if not available_models:
    st.warning("No trained models found in the 'models' directory.")
else:
    selected_model = st.selectbox("Select a model:", available_models)
    model = joblib.load(os.path.join(model_dir, selected_model))
    st.success(f"Loaded model: {selected_model}")

    # --- Input Fields ---
    st.header("Enter Environmental Parameters")

    NOx = st.number_input("NOx(GT)", value=150.0)
    NO2 = st.number_input("NO2(GT)", value=40.0)
    C6H6 = st.number_input("C6H6(GT) (Benzene µg/m³)", value=5.0)
    PT08_S5 = st.number_input("PT08.S5(O3) Sensor Output", value=800.0)
    T = st.number_input("Temperature (°C)", value=20.0)
    RH = st.number_input("Relative Humidity (%)", value=50.0)
    AH = st.number_input("Absolute Humidity (AH)", value=0.8)

    # --- Predict Button ---
    if st.button("Predict CO Level"):
        X = pd.DataFrame([[NOx, NO2, C6H6, PT08_S5, T, RH, AH]],
                         columns=['NOx(GT)', 'NO2(GT)', 'C6H6(GT)', 'PT08.S5(O3)', 'T', 'RH', 'AH'])
        pred = model.predict(X)[0]
        if pred.lower() == "good":
            st.success(f"✅ Air Quality: {pred}")
        elif pred.lower() in ["moderate", "fair"]:
            st.info(f"😐 Air Quality: {pred}")
        elif pred.lower() in ["poor", "unhealthy"]:
            st.warning(f"⚠️ Air Quality: {pred}")
        else:
            st.error(f"🚨 Air Quality: {pred}")


