from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline
import torch

# Load the pretrained tokenizer and model from Hugging Face's library
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained(
    'bert-base-uncased',
    num_labels=3,  # Assuming we have three labels: ['Non-Smoker', 'Current Smoker', 'Past Smoker']
)

# Convert list of labels to numerical ids
label_map = {'Non-Smoker': 0, 'Current Smoker': 1, 'Past Smoker': 2}

# Example text to classify
texts = ["Patient has a history of chronic smoking, currently smokes 10 cigarettes a day.",
         "Former smoker, quit smoking 5 years ago.",
         "No history of tobacco use."]

# Encode texts
encoded_texts = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

# Make predictions
with torch.no_grad():
    outputs = model(**encoded_texts)

# Convert model logits to probabilities and get the predicted labels
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
predictions = torch.argmax(probabilities, dim=-1)

# Convert predictions back to label strings
predicted_labels = [list(label_map.keys())[label_id] for label_id in predictions.numpy()]

# Print out texts with their predicted labels
for text, predicted_label in zip(texts, predicted_labels):
    print(f"Text: {text}\nPredicted Smoking Status: {predicted_label}\n")
