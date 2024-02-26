text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

words = text.split()
texting = []
for word in words:
    if word.endswith(','):
        word = word[:-1] + 'ing,'
    elif word.endswith('.'):
        word = word[:-1] + 'ing.'
    else:
        word = word + 'ing'
    texting.append(word)

print(' '.join(texting))
