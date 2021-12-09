from random import*

def find_word(Capitals:dict)->str:
	"""Otsing sõna sõnavaras
	"""
	a=input("Siseta riigi nimi või pealinn inglise keeles >>> ")
	for key, value in Capitals.items(): #проверяем каждое значение вместе со словами 
		if a.title()==value:
			ans=(a+" / "+key)
			break
		elif a.title()==key:
			ans=(a+" / "+value)
			break
		else:
			ans="See sõna ei olema"
	return ans,a

def add_word(Capitals:dict, a:str)->dict:
	"""Lisama sõna sõnavaras
	"""
	b=input("Siseta sõna tähendus >>> ")
	Capitals.update({a:b.title()})
	return Capitals

def change_smth(Capitals:dict)->dict:
	"""Muutma midagi sõnavaras
	"""
	a=input("Siseta sõna >>> ")
	c=input("Siseta uus tähendus >>> ")
	Capitals.update({a.title():c.title()})
	return Capitals

def testingknoledge(Capitals:dict)->float:
	"""Küsida mis ta tahab testida ja küsida 10 küsimust
	"""
	result=0
	country=list(Capitals)
	nocount={}
	with open("Cap.txt") as f:
		for i in f:
			v,k=i.strip().split("-")
			nocount[k.strip()]=v.strip()
	capitals=list(nocount)
	b=input("Kas te tahate testida Pealinns või Riigid? 1-pealinn, 2-riigid, 3-riigid ja pealinnad")
	if b=="1":
		a=0
		for i in range (1,11): 
			word=choice(country)
			print(word)
			ans=input(str(i)+". Siseta "+word+" pealinn >>> ")
			realans=Capitals.get(word)
			if ans.title()==realans:
				print("Õige!")
				a+=1
			else:
				print("Vale!")
		result=a*100/10
	elif b=="2":
		a=0
		for i in range (1,11):
			word=choice(capitals)
			ans=input(str(i)+". Siseta mis riig pealinn on "+word+" >>> ")
			realans=findkey(word,Capitals)
			if ans.title()==realans:
				print("Õige!")
				a+=1
			else:
				print("Vale!")
		result=a*100/10
	elif b=="3":
		country.extend(capitals)
		a=0
		for i in range (1,16):
			word=choice(country)
			for key, value in Capitals.items(): #проверяем каждое значение вместе с ключами
				if word==value:
					realans=key
					ans=input(str(i)+"Siseta riig kus pealinn on "+word+" >>> ")
					break
				elif word==key:
					realans=value
					ans=input(str(i)+". Siseta "+word+" pealinn >>> ")
					break
			if ans.title()==realans:
				print("Õige!")
				a+=1
			else:
				print("Vale!")
		result=a*100/10
	else:
		print("Vale funktsioon")
	return result
	
def findkey(val:str,Capitals:dict)->str:
	for key, value in Capitals.items():
		if val == value:
			return key
	return "ei ole"