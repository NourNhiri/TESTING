from jinja2 import *

env=Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

t=Template("<ul>{% for item in list %} <li>{{item}}</li>{% endfor %}</ul>")
list=[]
while True:
    fruit=input()
    if fruit == "": break
    list.append(fruit)

print(t.render(list=list))

