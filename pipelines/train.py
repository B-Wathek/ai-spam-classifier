from src.model import SpamClassifier
from sklearn.metrics import accuracy_score

texts = [
    "Win a free iPhone",
    "Hello how are you",
    "Claim your prize now",
    "Let's meet tomorrow"
]

labels = ["spam", "ham", "spam", "ham"]

model = SpamClassifier()
model.train(texts, labels)

preds = model.predict(texts)

acc = accuracy_score(labels, preds)

print("Accuracy:", acc)

# 🚨 CI GATE
if acc < 0.9:
    raise Exception("Model accuracy below threshold!"))
