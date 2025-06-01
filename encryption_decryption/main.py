from collections import Counter

file_path = 'encrypted_text'

with open(file_path, 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

encrypted_text = encrypted_text.lower()

letter_counts = Counter(encrypted_text)

print("Фреквенција на букви:")
for letter, count in letter_counts.items():
    if letter.isalpha():
        print(f"{letter}: {count}")

language_frequencies = ['е', 'н', 'т', 'и', 'а', 'с', 'р', 'о', 'л', 'в', 'к', 'м', 'д', 'п', 'у', 'г', 'з', 'б', 'ј',
                        'ц', 'ш', 'ч', 'ђ', 'ж', 'љ', 'њ', 'ф', 'х', 'ч', 'ч', 'ј']

decrypted_text = ""
letter_mapping = {}

sorted_letters = sorted(letter_counts, key=lambda x: letter_counts[x], reverse=True)
for i in range(len(sorted_letters)):
    if i < len(language_frequencies):
        letter_mapping[sorted_letters[i]] = language_frequencies[i]

for char in encrypted_text:
    if char.isalpha():
        decrypted_text += letter_mapping.get(char, char)
    else:
        decrypted_text += char

print("Дешифриран текст:")
print(decrypted_text)
