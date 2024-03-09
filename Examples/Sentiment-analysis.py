from transformers import pipeline

classifier = pipeline("sentiment-analysis")


res=classifier("Raghul is so bad and good")

print(res[0]['label'])