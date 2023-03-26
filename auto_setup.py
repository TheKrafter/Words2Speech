import sys

audio_format = sys.argv[0]

words = sys.argv
del words[0]

words_yml = [f'# Start of automated setup with format {audio_format}\n']
for word in words:
    line = f"{word.lower()}: '{audio_format.replace('WORDHERE', word)}'"
    words_yml.append(f'{line}\n')
    print(line)

print('Writing...')

with open('words.yml', 'a') as file:
    for line in words_yml:
        file.write(line)

print('Success!')
