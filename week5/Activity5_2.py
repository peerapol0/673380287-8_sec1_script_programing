
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()

word_counts = {}

for w in words:
    word = w.strip('.,!?"')
    if word:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")