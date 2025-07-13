
# FS Traders Official – AI Powered Stock Market Dashboard

🚀 Live F&O data | 📊 PCR & OI Tables | 📰 Crude Oil News | 🔥 Sector Heatmap

## 📦 Features

- Angel One auto-login with TOTP
- Live Option Chain + PCR
- Crude oil live price + news feed
- Sector heatmap (dummy layout)
- Streamlit Cloud ready

## 🔐 Secrets Required

Add this in `.streamlit/secrets.toml`:

```toml
[angelone]
api_key = "YOUR_API_KEY"
client_id = "YOUR_CLIENT_ID"
password = "YOUR_PASSWORD"
totp_secret = "YOUR_TOTP_SECRET"
```

## ▶️ Run

```bash
streamlit run main.py
```

Deploy on Streamlit Cloud ✅
