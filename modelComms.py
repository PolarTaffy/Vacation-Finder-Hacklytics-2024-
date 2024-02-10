from transformers import pipeline
class modelComms:

    
    def __init__(input):
        pass
    def askGPT(input):
        generator = pipeline('text-generation', model='HuggingFaceH4/zephyr-7b-beta')
        generator(input, min_length=30, num_return_sequences=1)