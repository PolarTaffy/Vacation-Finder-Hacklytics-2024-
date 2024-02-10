from transformers import pipeline
class modelComms:

    generator = pipeline('text-generation', model='HuggingFaceH4/zephyr-7b-beta')
    def __init__(input):
        pass
    def askGPT(input):
        generator(input, min_length=30, num_return_sequences=1)