fruit = [
    "appel",
    "peer",
    "banaan",
    "sinaasappel",
    "kiwi",
    "aardbei",
    "druif",
    "ananas",
    "mango",
    "kers",
]


while True:
    for i,item in enumerate(fruit,1):
        print(f"{i}. {item}")

    item=input("welke item wil je verwijderen?>").lower()
    
    if item not in fruit:
        print("bestaat niet")
        if input("wil je toevoegen?>").lower()=="j":
            fruit.append(item)
    else:
        i=fruit.index(item)
        fruit.pop(i)

