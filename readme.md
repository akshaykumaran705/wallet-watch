# 🛡️ Wallet Watch

**Wallet Watch** is a lightweight Ethereum transaction analysis app built using [Streamlit](https://streamlit.io). It allows users to explore wallet behavior, filter by transaction volume, and detect potentially suspicious activity using a simple dashboard.

---

## 🚀 Features

- 🔍 **Search by Wallet Address** (partial matches)
- 📊 **Filter by Total Transactions**
- ⚠️ **Flagged Wallet View** (`FLAG = 1`)
- 📈 **Scatter Plot** of ETH Sent vs Received
- 📄 Interactive table of wallet activity
- 🧩 Powered by Streamlit, Plotly, and Pandas

---

## 📂 Dataset

The dataset (`transaction_dataset.csv`) contains features such as:

- Ethereum address (`Address`)
- Total transactions
- ETH sent and received
- FLAG column (indicating suspicious wallets)

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/akshaykumaran705/wallet-watch.git
cd wallet-watch

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run wallet_watch_app.py
