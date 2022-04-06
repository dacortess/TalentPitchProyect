import re

palabras = ["<a ghhj href=\"refref\" ageadg> hola </a gjg jfdh>"]

patron = re.compile("href=\".*?\"")
for palabra in palabras:
    m = patron.findall(palabra)[0][6:-1]
    print(m)