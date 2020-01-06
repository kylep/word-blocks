# Word Blocks

This little app was made to help find fun ways to rearange the wooden blocks
that typically spell MERRY CHRISTMAS at my parents house. Since the blocks also
work in french, some have a second possible letter.

## To download the word list

There are a bunch you can choose from

### DWYL List

From [https://github.com/dwyl/english-words](dwyl/english-words).
This one is huge, but you'll get a ton of gibberish strings too.

```bash
wget https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
```

### Google's Greatest Hits

From [https://github.com/first20hours/google-10000-english](first20hours/google-10000-english).

```bash
# 20k words
wget https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt

# 10k words
wget https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt
```


### Deekayen's 1000 most common words

Good for immediately useful strings

```bash
wget https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt
```

---

## To run the tests

Set up a venv:

```bash
python3 -m virtualenv env
source env/bin/activate
python3 -m pip install .
```

Run the integration tests:
```bash
python3 -m pytest -s tests/
```
