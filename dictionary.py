Capitals={}
c="1"
with open("Cap.txt") as f:
	for i in f:
		k,v=i.strip().split("-")
		Capitals[k.strip()]=v.strip()
print(Capitals.items())

while True:
	
	if c=="1":
		a=input("Siseta riigi nimi või pealinn >>> ")
		ans=Capitals.get(a.title)
		print(ans)