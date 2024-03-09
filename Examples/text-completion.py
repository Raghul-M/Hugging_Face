from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "In this course, we will teach how to",
    max_length=60,
    num_return_sequences = 2,
)

print(res)