# Words-2-Speech
From a list of words, and a list of sound files, make a list of words into a sound.

## Setup
First, you must configure `words.yml`. For example, if I have a file called `hello_word.py` of someone saying the word `hello`, I'd put this line in `words.yml`:
```yaml
hello: 'hello_world.py'
```
NOTE: put words as lowercase, as they're all converted to lowercase in the script.

## Usage
Usage is quite simple:
```sh
python3 main.py Hello world
```
Make sure not to use any punctuation marks. Capitalization doesn't matter either.

However, if a word you use isn't in words.yml, a `NotImplementedError` will be raised, telling you which word isn't there.

## Automated setup
If all your files are in the same naming format, you can use `auto_setup.py` as shown:
```sh
python3 auto_setup.py saying_WORDHERE_lmao.mp3 hello world bye lol
```
Where `WORDHERE` is what to replace with the word, and `hello world bye lol` is a list of space-seperated words that are recorded with this format.