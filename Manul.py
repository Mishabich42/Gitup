import string


def analyze_text(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"Файл з назвою {file_name} не знайдено.")
        return

    for p in string.punctuation:
        text = text.replace(p, " ")

    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    with open("word_count.txt", "w") as file:
        for word, count in sorted_words:
            file.write(f"{word}: {count}\n")

    print("Аналіз тексту успішно завершено.")
    return sorted_words


file_name = input("Введіть назву файлу: ")
analyze_text(file_name)
