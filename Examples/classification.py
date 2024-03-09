from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "This is a Python Course",
    candidate_labels=["Computer Science","Programming","English"],
)

print(res['scores'])