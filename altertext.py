import random
text = ""
try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        text = content
except FileNotFoundError:
    print(f"Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

def alterText(txt):
    sentences = txt.split(".")

    if len(sentences) / 3 < 1:
        return txt
    sentences.pop(len(sentences) - 1)
    sentences.pop(random.randint(0, len(sentences)))
    sentences.pop(random.randint(0, len(sentences)))
    sentences.pop(random.randint(0, len(sentences)))

    alteredSentence = ""
    for s in sentences:
        alteredSentence += s
        alteredSentence += ". "

    return alteredSentence

print(alterText(text))



