# 📰 Fake News Detection App

A BERT-based fake news classifier using PyTorch and HuggingFace Transformers. This app can classify whether a given news article or URL is **Real** or **Fake**.

---

## 🚀 Features

- 🔍 Accepts raw text or article URLs
- 🧠 Fine-tuned BERT model for binary classification
- 📦 Automatically downloads model weights from Google Drive if missing

---

## 🗂️ Project Structure

```

FakeNewsDetector/
├── main.py                # Flask web app
├── predict.py             # Model definition + inference logic
├── templates/
│   └── index.html         # Web interface template
├── .gitignore
├── README.md
└── requirements.txt       # Dependencies

````



---

## 🧠 Model Weights

The model weights (`c1_fakenews_weights.pt`) are hosted on Google Drive and will be **automatically downloaded** on first run.

If needed, you can manually download them:

🔗 [Download weights](https://drive.google.com/file/d/1Nuh44sBDXNEngrs3n-CaqlaXkIvrRzTY/view?usp=sharing)

Place the file in your project root if you're not using auto-download.

---

## 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/SambhavJ2004/FakeNewsDetector.git
cd FakeNewsDetector
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

Make sure the following packages are listed in `requirements.txt`:

```
torch
transformers
flask
newspaper3k
requests
```

Then install them:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
python main.py
```

Then open your browser and go to:
[http://localhost:5000](http://localhost:5000)

---

## ✏️ How It Works

* You can input:

  * A **raw news article**
  * Or a **URL** (the app will extract the article automatically)
* The model outputs:

  * A label: `Real` or `Fake`
  * A confidence score (0 to 1)

---

## 📌 Notes

* First-time use may take a few seconds to download the model weights (\~100MB).
* The model runs on **CPU** by default for maximum compatibility.

---

## 🙌 Credits

* Model: `bert-base-uncased` from HuggingFace
* Libraries: PyTorch, Flask, Transformers, Newspaper3k

---
