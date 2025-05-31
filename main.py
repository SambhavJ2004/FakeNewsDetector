from flask import Flask, render_template, request
from predict import predict_news, extract_text_from_url

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text", "").strip()
    url = request.form.get("url", "").strip()

    if not text and url:
        try:
            text = extract_text_from_url(url)
        except Exception as e:
            return render_template("index.html", prediction="Error fetching URL", confidence="0")

    if not text:
        return render_template("index.html", prediction="No text provided.", confidence="0")

    label, confidence = predict_news(text)
    confidence_percent = round(confidence * 100, 2)
    return render_template("index.html", prediction=label, confidence=confidence_percent)

if __name__ == "__main__":
    app.run(debug=True)
