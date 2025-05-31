# 📰 Fake News Detection App

A BERT-based fake news classifier using PyTorch and HuggingFace Transformers. This app can classify whether a given news article or URL is **Real** or **Fake**.

---

## 🚀 Features

- 🔍 Accepts raw text or article URLs
- 🧠 Fine-tuned BERT model for binary classification
- 📦 Automatically downloads model weights from Google Drive if missing

---

## 📁 Project Structure


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
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
