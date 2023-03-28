#!/usr/bin/python3
# Import modules for CGI handling
import cgi, cgitb
from datetime import datetime
import json
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields

now = datetime.now()

nm=form.getvalue('name')
d=str(now)
text = form.getvalue('mensagem')
msg = dict(data=d,nome=nm,mensagem=text)

arquivo = open("mensagens.json","a")
arquivo.write(f'{json.dumps(msg)}\n')
arquivo.close

with open("mensagens.json", 'r') as leitor:
    linhas = leitor.readlines()

# arquivo.write(f'Data: {d}\n')
# arquivo.write(f"Autor: {nm}\n")
# arquivo.write(f"Mensagem: {text}\n")
form = """<form action="/cgi-bin/htmlform.py"  method="post"target="_blank">
Nome : <input type="text" name="name"/></br>
Mensagem: </br>
<textarea name="mensagem"cols="40"rows="4">
Type your text here...
</textarea>
<input type="submit" value="Submit"/>
</form>
"""
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
# form
print(form)
print ("<br>")

print ("<h2>Mensagem recebida</h2>")
print("Name: {}".format(nm))
print ("<br>")
print("Data: {}".format(d))
print ("<br>")
print("Text : {}".format(text))
print ("</br>")
print ("</br>")
# exibir arquivo na pagina
for l in linhas:
    print(l)
    print("<br>")

print("</body>")
print ("</html>")