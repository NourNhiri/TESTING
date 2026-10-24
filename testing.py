from collections import Counter

list_of_words = [
    "appel", "peer", "banaan", "appel", "kers", "peer", "appel",
    "druif", "banaan", "kers", "kers", "kers", "citroen", "appel",
    "peer", "druif", "mango", "banaan", "appel", "kiwi", "mango",
    "citroen", "kers", "druif", "peer", "appel", "kiwi", "banaan",
]

count=Counter(list_of_words)


print(count)