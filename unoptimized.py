# word_counter_original.py

def count_words(text):
    words = text.split(" ")
    word_count = {}
    for w in words:
        w = w.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
        if w in word_count:
            word_count[w] = word_count[w] + 1
        else:
            word_count[w] = 1
    return word_count

# Example usage
if __name__ == "__main__":
    with open("sample.txt", "r") as file:
        data = file.read()
    result = count_words(data)
    for key in result:
        print(key, ":", result[key])
