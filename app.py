
import streamlit as st
import pandas as pd
import time
from utils import predict_transactions

st.set_page_config(page_title="Fraud Detection Bank Simulation", layout="centered")

st.title("🏦 Bank Transaction Fraud Detection Simulator")

#sample_data = pd.read_csv("/content/sample_inputs.csv")
all_data = pd.read_csv("/content/sample_inputsFinal.csv")
sample_data = all_data.sample(n=10)

if "logs" not in st.session_state:
    st.session_state.logs = []

st.subheader("📄 Sample Transactions to Simulate")
st.dataframe(sample_data)

if st.button("🔍 Simulate Transactions"):
    st.session_state.logs = []
    with st.spinner("Processing transactions..."):
        preds = predict_transactions(sample_data)
        time.sleep(1)

        for i, pred in enumerate(preds):
            tx = sample_data.iloc[i].to_dict()
            if pred == 0:
                status = "✅ Success"
                msg = "No fraud detected. Transaction approved."
            else:
                status = "🚫 Blocked"
                msg = "Fraud detected! Transaction flagged."

            st.session_state.logs.append({
                "Transaction ID": f"T{i+1:03d}",
                "Status": status,
                "Message": msg
            })
            time.sleep(0.5)

if st.session_state.logs:
    st.subheader("📜 Transaction Logs")
    df_logs = pd.DataFrame(st.session_state.logs)
    st.dataframe(df_logs)
