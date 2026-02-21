# ✉️ Service Email Generator

A simple Streamlit web app that generates client-ready emails based on selected services.

This tool allows manual client entry and produces a formatted email that can be copy-pasted into an email client.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-generator.git
cd email-generator
```

---

### 2️⃣ Create a Virtual Environment

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

After activation, your terminal should show:

```
(venv)
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the App

```bash
streamlit run ui.py
```

Your browser will open automatically at:

```
http://localhost:8501
```

---

## 🛠 Project Structure

```
email-generator/
│
├── ui.py              # Streamlit interface
├── email_gen.py       # Email generation logic
├── requirements.txt   # Project dependencies
├── README.md
└── .gitignore
```

---

## 📦 Dependencies

- streamlit

---

## 🌐 Deployment

This app is deployed using Streamlit Community Cloud.

To deploy:
1. Push this repository to GitHub
2. Connect the repo in Streamlit Cloud
3. Set `ui.py` as the main file
4. Deploy

---

## ✨ Notes

- This app does not send emails.
- It generates copy-ready email text for manual sending.
- All client data is entered manually through the UI.
