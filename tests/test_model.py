from src.model import SpamClassifier

def test_prediction():
    texts = ["free money", "hello friend"]
    labels = ["spam", "ham"]

    model = SpamClassifier()
    model.train(texts, labels)

    result = model.predict(["free money"])
    assert result[0] == "spam"
  
