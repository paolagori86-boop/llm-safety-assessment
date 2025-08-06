def is_toxic(text):
    keywords = ["hate", "kill", "attack", "stupid"]
    return any(k in text.lower() for k in keywords)
