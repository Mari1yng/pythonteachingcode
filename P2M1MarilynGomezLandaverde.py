main = "Enter your full name: "
nm = input(main)
name = ("Welcome, " + nm)
quote = input(name + ". Enter a 1 sentence quote, non-alpha separate words: ")
word = ''
for letter in quote:
    if letter.isalpha():
        word += letter
    elif word.lower() >= 'h':
        print(word.upper())
        word = ''
    else:
        word = ''
if word.lower() >= 'h':
    print(word.upper())
