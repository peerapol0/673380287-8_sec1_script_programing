
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()

word_counts = {}

for word in words:
    cleaned_word = word.strip('.,!?"')
    if cleaned_word:
        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

print(word_counts)
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")