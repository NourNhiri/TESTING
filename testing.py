from jinja2 import *

env=Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

t=Template("<ul>{% for item,price in list.items() %} <li>{{item}}  {{price}}</li>{% endfor %}</ul>")
producten = {
    "T-shirt": 15.99,
    "Jeans": 49.95,
    "Sneakers": 79.00,
    "Roman: De Avonden": 22.50,
    "Python kookboek": 39.90,
    "Minecraft": 26.95,
    "Controller": 59.99,
}

print(t.render(list=producten))

