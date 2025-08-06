def is_biased(text):
    keywords = ["stereotype", "disparage", "inferior"]
    return any(k in text.lower() for k in keywords)
