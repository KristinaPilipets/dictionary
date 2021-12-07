from modul import*
Capitals={}
c="1"
with open("Cap.txt") as f:
	for i in f:
		k,v=i.strip().split("-")
		Capitals[k.strip()]=v.strip()
print(Capitals.items())

while True:
	c=input("Otsing sõna sõnavaras - 1, ")
	if c=="1":
		find_word()
	elif c=="2"