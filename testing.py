import re

print(re.findall(r'\ba[a-z]*','apple, banana, avocado, cherry, apricot'))
print(re.findall(r'\d+','Er zijn 12 maanden in een jaar, 24 uur in een dag'))
print(re.findall(r'\b[a-z]*ing\b','I am walking while singing and eating.'))
print(re.findall(r'\b[aeiouAEIOU][a-z]*','Alice wonders everywhere under the sky'))
print(re.findall(r'\bf[a-z]*','wich foot or hand fell fastest'))
print(re.findall(r'\w+@\w+\.\w+','Mijn email is voorbeeld@voorbeeld.com en info@test.be.'))
