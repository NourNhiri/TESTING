from spellchecker import SpellChecker
spell=SpellChecker()

while True:
    word=input()
    if not spell.unknown([word]):
        print(word+" is goed")
    else:
        print("nieet foood")