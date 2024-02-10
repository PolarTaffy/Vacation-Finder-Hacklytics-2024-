from transformers import pipeline
generator = pipeline('text-generation', model='HuggingFaceH4/zephyr-7b-beta')
generator("Once upon a time,", max_length=30, num_return_sequences=1)