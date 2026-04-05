import pandas as pd
from src.model import SpamClassifier

# Load dataset
data = pd.read_csv("data/raw/emails.csv")

texts = data["text"].tolist()
labels = data["label"].tolist()

# Train model
clf = SpamClassifier()
clf.train(texts, labels)

# Predict sample
pred = clf.predict(["Free prize available"])
print("Prediction:", pred[0])

# Save report
with open("reports/eval_report.md", "w") as f:
    f.write("# Evaluation Report\n")
    f.write(f"Total samples: {len(texts)}\n")
    f.write("Pipeline executed successfully\n")

print("Pipeline completed ✅")
