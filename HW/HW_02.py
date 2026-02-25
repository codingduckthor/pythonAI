# Требования
# TextDataset хранит список строк
# Preprocessor приводит к lower, убирает лишние пробел
# Analyzer считает частоты слов (dict) и уникальные слова (set)
# Смысл: связать ООП + структуры данных из 1 пары.

class TextDataset:
    def __init__(self, texts):
        self.texts = texts


class Preprocessor:
    def process(self, texts):
        processed = []

        for text in texts:
            text = text.lower()
            text = " ".join(text.split())
            processed.append(text)

        return processed


class Analyzer:
    def analyze(self, texts):
        word_freq = {}
        unique_words = set()

        for text in texts:
            words = text.split()

            for word in words:
                unique_words.add(word)

                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

        return word_freq, unique_words


data = TextDataset([
    "Hello   World",
    "Hello Python",
    "Python   is   GREAT"
])

preprocessor = Preprocessor()
clean_texts = preprocessor.process(data.texts)

analyzer = Analyzer()
freq, unique = analyzer.analyze(clean_texts)

print("Processed texts:", clean_texts)
print("Word frequencies:", freq)
print("Unique words:", unique)
