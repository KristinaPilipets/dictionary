from random import*

def find_word(Capitals:dict)->str:
	"""Otsing sõna sõnavaras
	"""
	a=input("Siseta riigi nimi või pealinn inglise keeles >>> ")
	for key, value in Capitals.items(): #проверяем каждое значение вместе со словами 
		if a.title()==value:
			ans=(a+"/"+key)
			break
		elif a.title()==key:
			ans=(a+"/"+value)
			break
		else:
			ans="See sõna ei olema"
	return ans,a

def add_word(Capitals:dict, a:str)->dict:
	b=input("Siseta sõna tähendus >>> ")
	Capitals.update({a:b})
	return Capitals

def change_smth(Capitals:dict)->dict:
	a=input("Siseta sõna >>> ")
	c=input("Siseta uus tähendus >>> ")
	Capitals.update({a.title():c.title()})
	return Capitals

def testingknoledge(Capitals:dict):
	b=input("Kas te tahate testida Pealinns või Riigid? 1-pealinn, 2-riigid")
	if b=="1":
		a=0
		capitals=list(Capitals)
		print(capitals)
		for i in range (0,11): 
			word=choice(capitals)
			print(word)
			ans=input(str(i)+" Siseta pealinn >>> ")
			if ans in Capitals.values():
				print("Õige!")
				a+=1
			else:
				print("Vale!")
		result=a*100/10
	print("Teie resultat on "+str(result)+"%")
	#ans=input("Siseta riig >>> ")