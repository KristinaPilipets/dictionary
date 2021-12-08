from modul import*
Capitals={}
with open("Cap.txt") as f:
	for i in f:
		k,v=i.strip().split("-")
		Capitals[k.strip()]=v.strip()

while True:
	c=input("Otsing sõna sõnavaras - 1, muutma sõna tähendus - 2, test - 3")
	if c=="1":
		ans,a=find_word(Capitals)
		print(ans)
		if ans=="See sõna ei olema":
			b=input("Kas te tahate lisa sõna sõnavars, 1-jah 2-ei >>> ")
			if b=="1":
				Capitals=add_word(Capitals,a)
			else:
				pass
		else:
			pass
	elif c=="2":
		Capitals=change_smth(Capitals)
	elif c=="3":
		result=testingknoledge(Capitals)
		print("Sinu resultat on "+str(result)+"%")
	else:
		print("See funktioon ei olema")
		