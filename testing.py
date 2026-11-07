import re 




email=input(">")
tld=[".com",".be",".it",".nl"]

m=re.fullmatch(r"(?P<user>\w+)@(?P<provider>\w+)(?P<domain>\.\w+)",email)
if m==None:
    print("not valid")
elif m.group("domain") not in tld:
    print("not valid top level domain or domain is not supported")
else:
    print("valid")

    print(f"user is: {m.group("user")}")
    print(f" provider is: {m.group("provider")}")
    print(f"domain is: {m.group("domain")}")

