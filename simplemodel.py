import languagemodels as lm

lm.config["max_ram"] = "4gb"
print(lm.do("What are some good vacation spots and what makes each spot good? In each spot, tell me what the night life scene is like there for young adults. Give me spots outside of the US, each spot should be from a different continent."))
