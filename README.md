# 🌫️ Air Quality Prediction Project

An end-to-end data science project analyzing urban air pollution data and predicting **air quality levels** using multiple machine learning models.  
This project combines **exploratory data analysis (EDA)**, **feature engineering**, **model training**, and a **Streamlit web app** for interactive predictions.

---

## 🧭 Overview

Air quality is one of the most critical environmental health indicators.  
This project uses historical air pollution sensor data to classify the air quality category (e.g., *Good*, *Moderate*, *Poor*).

The workflow includes:
1. Data cleaning and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Training and evaluating multiple ML models  
4. Saving trained models (`.pkl` format)  
5. Building a Streamlit web app for live predictions  

---

## 🧰 Tech Stack

- **Python 3**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn**, **Joblib**
- **Streamlit**

---

## ⚙️ Environment Setup & Installation

```bash
# =======================================================
# 🧠 Air Quality Project - Environment Setup Instructions
# =======================================================

# 1️⃣ Create and activate a virtual environment (recommended)
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 2️⃣ Upgrade pip
python -m pip install --upgrade pip

# 3️⃣ Install all required libraries
pip install -r requirements.txt

# 4️⃣ (Optional) Verify installation
python -m pip list

# 5️⃣ Run the Streamlit app 🚀
streamlit run app/streamlit_app.py
