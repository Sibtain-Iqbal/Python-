text = input("Enter a line of text: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

text = input("Enter a string: ")
word_count = text.count(" ") + 1

print("Estimated number of words:", word_count)

s = input("Enter a string: ")
s = s.lower().replace(".", "").replace(",", "")
print("Resulting string:", s)