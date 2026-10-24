list_of_words = [
    "appel", "peer", "banaan", "appel", "kers", "peer", "appel",
    "druif", "banaan", "kers", "kers", "kers", "citroen", "appel",
    "peer", "druif", "mango", "banaan", "appel", "kiwi", "mango",
    "citroen", "kers", "druif", "peer", "appel", "kiwi", "banaan",
]
counter={}

for word in list_of_words:
    if word not in counter:
        counter[word]=1
    else:
        counter[word]=counter[word]+1

print(counter)
    