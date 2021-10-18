# split sentence into words and return list of (token_name, word) tuples
def scan(sentence):
    words = [word for word in sentence.split()]
    return [tokenize(word) for word in words]

# not every token name can be stored in dict, so if you can't
# look it up (as it is with number and error), handle tokenization accordingly
def tokenize(word):
    if allowed.get(word):
        token_name = allowed[word]
    else:
        token_name, word = ("number", int(word)) if word.isdigit() else ("error", word)
    
    return token_name, word

# token names to allowed words list
token_names_dict = {
    "direction": ["north", "south", "east", "west"],
    "verb": ["go", "stop", "kill", "eat"],
    "stop": ["the", "in", "of", "from", "at", "it"],
    "noun": ["door", "bear", "princess", "cabinet"],
}

# build dict with "allowed word":"token name" as key:value pairs
allowed = {}
for token_name, words in token_names_dict.items():
    for word in words:
        allowed[word] = token_name