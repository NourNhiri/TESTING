from pathlib import Path, PurePath



def main():
    p=input("geef je path\n>")
    p=Path(p)
    if not p.is_dir():
        print("path is geen directory")
        return

    print("dit is een directory. Dit zijn de files er in")

    for f in list(p.glob("*.py")):
        print(f.name)

    pass




if __name__=="__main__":
    main()