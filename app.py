import re
from collections import Counter

def calculate_word_frequency(file_path):
    # Metin dosyasını okuma
    with open(file_path, 'r') as file:
        data = file.read()

    # Metinden kelimeleri ayırma ve temizleme
    words = re.findall(r'\b\w+\b', data.lower())

    # Kelime frekansını hesaplama
    word_frequency = Counter(words)

    return word_frequency

# Metin dosyasının yolu
file_path = "metin.txt"

# Kelime frekansını hesaplama
frequency = calculate_word_frequency(file_path)

# Sonuçları görüntüleme
for word, count in frequency.most_common():
    print(f"{word}: {count}")
