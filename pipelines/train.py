from src.model import SpamClassifier

# Simple dataset
texts = [
    "Win a free iPhone",
    "Hello how are you",
    "Claim your prize now",
    "Let's meet tomorrow"
]

labels = ["spam", "ham", "spam", "ham"]

model = SpamClassifier()
model.train(texts, labels)

predictions = model.predict(["Free prize now"])
print(predictions)
