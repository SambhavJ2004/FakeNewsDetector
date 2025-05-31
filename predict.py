import torch
import torch.nn as nn
from transformers import BertTokenizerFast, AutoModel
import torch.nn.functional as F
from newspaper import Article




# Load tokenizer and base BERT
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
bert = AutoModel.from_pretrained('bert-base-uncased')

# Define the same architecture
class BERT_Arch(nn.Module):
    def __init__(self, bert):
        super(BERT_Arch, self).__init__()
        self.bert = bert
        self.dropout = nn.Dropout(0.1)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(768, 512)
        self.fc2 = nn.Linear(512, 2)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, sent_id, mask):
        cls_hs = self.bert(sent_id, attention_mask=mask)['pooler_output']
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# Initialize model and load weights
model = BERT_Arch(bert)
model.load_state_dict(
    torch.load("c1_fakenews_weights.pt", map_location=torch.device("cpu")),
    strict=False  # <-- This will ignore unexpected keys like "position_ids"
)


# Prediction function
def predict_news(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        output = model(inputs["input_ids"], inputs["attention_mask"])
        probabilities = torch.exp(output)  # Since you're using LogSoftmax
        predicted_class = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0][predicted_class].item()

    label = "Fake" if predicted_class == 1 else "Real"
    return label, confidence
def extract_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

