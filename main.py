# Words2Speech
# Copyright (c) 2023 Krafter et. al.
from playsound import playsound
import yaml
import sys

# Open words.yml
with open('words.yml', 'r') as file:
    words = yaml.load(file, Loader=yaml.FullLoader)

# Play a word
def play(word):
    if word in words:
        print(word)
        playsound(words[word])
    else:
        raise NotImplementedError(f'The word "{word}" was not found in "words.yml"!')


# Get input
sentence = sys.argv
del sentence[0]

# Play sentence
print(f'Playing words: {sentence}')
for word in sentence:
    play(word.lower())