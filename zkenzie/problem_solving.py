text = "hello how are you today, I am fine"

count = 1

for word in text:
    if word == " ":
        count += 1
count = 1

for char in text.lower():
    if char in ["a", "i", "o", "u"]:
        # if char in ["a","i","o","u","A","I","U"]:
        count += 1
print(f"how many vowels in the sentence: {count +1}")

text = "hello world."
count = 0

if len(text) > 0:
    count = 1
for word in text:
    if word == " ":
        count += 1
print("total number of words: ", count)
