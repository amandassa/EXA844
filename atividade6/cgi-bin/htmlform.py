#!/usr/bin/python3
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('name')
d=form.getvalue('data')
text = form.getvalue('mensagem')
arquivo = open("mensagens.txt","a")
arquivo.write("Data:  "+d)
arquivo.write("Autor: "+nm)
arquivo.write("Mensagem: "+text)
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print ("<h2>Mensagem recebida</h2>")
print("Name: {}".format(nm))
print ("</br>")
print("Data: {}".format(d))
print ("</br>")
print("Text : {}".format(text))
print ("</br>")
print("</body>")
print ("</html>")