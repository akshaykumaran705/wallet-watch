import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("transaction_dataset.csv")
df["Address"] = df["Address"].astype(str)

st.set_page_config(page_title="Wallet Watch", layout="wide")

st.sidebar.title("🛡️ Wallet Watch")
st.sidebar.markdown("Ethereum Risk Explorer")

st.title("🛡️ Wallet Watch: Ethereum Wallet Analysis")
st.markdown("Explore Ethereum wallet activity with filters for risk signals.")

# Filter widgets
addr_input = st.text_input("🔍 Enter part of a wallet address", "")
min_txns = st.slider("📊 Minimum Total Transactions", 0, 1000, 100)
flagged_only = st.toggle("⚠️ Show only flagged wallets (FLAG=1)?", False)

# Apply filters
filtered = df[df["total transactions (including tnx to create contract"] > min_txns]

if addr_input.strip():
    filtered = filtered[filtered["Address"].str.contains(addr_input.strip(), case=False, na=False)]

if flagged_only:
    filtered = filtered[filtered["FLAG"] == 1]

# Show table
st.dataframe(filtered.head(50), use_container_width=True)

# Plot
fig = px.scatter(
    filtered,
    x="total Ether sent",
    y="total ether received",
    color="FLAG",
    hover_data=["Address"],
    title="Total ETH Sent vs Received (Colored by FLAG)"
)
st.plotly_chart(fig, use_container_width=True)
