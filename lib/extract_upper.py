def extract_uppercase(text):
    words = text.split(" ")
    uppercase = []
    for word in words:
        if word.isupper():
            uppercase.append(word)
    return uppercase