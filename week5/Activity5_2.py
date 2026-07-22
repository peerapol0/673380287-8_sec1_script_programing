
sentence = input("Enter a sentence: ")
sentence_lower = sentence.lower()
words = sentence_lower.split()

word_counts = {}

for word in words:
    cleaned_word = word.strip('.,!?"')
    if cleaned_word:
        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")