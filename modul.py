from random import*

def find_word(Capitals:dict)->str:
	"""Otsing sõna sõnavaras
	"""
	a=input("Siseta riigi nimi või pealinn inglise keeles >>> ")
	for key, value in Capitals.items(): #проверяем каждое значение вместе со словами 
		if a.title()==value: #смотрим если введенная переменная это значение
			ans=( a.title()+" / "+key ) # к переменной добавляем ключ
			break
		elif a.title()==key: #смотрим если введенная переменная это ключ
			ans=( a.title()+" / "+value ) # к переменной добавляем значение
			break
		else:
			ans="See sõna ei olema" #если слова не существует в словаре
	return ans,a

def add_word(Capitals:dict, a:str)->dict:
	"""Lisama sõna sõnavaras
	"""
	b=input("Siseta sõna tähendus >>> ") #просим ввести значение слова, мы знаем ключ из прошлой функции по поиску
	Capitals.update({a.title():b.title()}) # добавляем в словарь
	return Capitals

def change_smth(Capitals:dict)->dict:
	"""Muutma sõna tähendus sõnavaras
	"""
	a=input("Siseta sõna, milline tähendus te tahate muuta >>> ")
	if a not in Capitals.keys():
		print("see sõna ei ole sõnavaras")
	else:
		c=input("Siseta uus tähendus >>> ")
		Capitals.update({a.title():c.title()}) #обновляем значение слова по ключу
		return Capitals #возращаем измененый словарь

def testingknoledge(Capitals:dict)->float:
	"""Küsida mis ta tahab testida ja küsida 10 küsimust
	"""
	result=0 #переменную приравниваем к нулю чтобы при не той выборе функции результат был ноль
	country=list(Capitals) # делаем из словаря список
	nocount={} 
	with open("Cap.txt") as f:
		for i in f:
			v,k=i.strip().split("-") #создаем словарь наоборот где столицы это ключи, а страны - значения
			nocount[k.strip()]=v.strip()
	capitals=list(nocount)
	b=input("Kas te tahate testida Pealinns või Riigid? 1-pealinn (10 küsimused), 2-riigid (10 küsimused), 3-riigid ja pealinnad (15 küsimused)")
	if b=="1":
		a=0
		for i in range (1,11): 
			word=choice(country) #выбираем случайное значение из списка
			print()
			ans=input(str(i)+". Siseta "+word+" pealinn >>> ")
			realans=Capitals.get(word) #делаем правильный ответ переменной
			if ans.title()==realans: #проверяем правильность ответа
				print("Õige!")
				a+=1 #если ответ правильный к переменной а добавляем 1
			else:
				print("Vale!")
		result=a*100/10 #расчет результата
	elif b=="2":
		a=0
		for i in range (1,11):
			word=choice(capitals)
			ans=input(str(i)+". Siseta mis riig pealinn on "+word+" >>> ")
			realans=findkey(word,Capitals) #использую функцию чтобы найти ключ зная значение
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
			for key, value in Capitals.items(): #проверяем каждое значение вместе с ключами чтобы опредилить даем мы столицу(значение) или страну(ключ) схожа с функцией поиска слова в словаре
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
		result=a*100/15
	else:
		print("Vale funktsioon") #если была выбрана не одна из 3 функций то выдаем ошибку 
	return result

def findkey(val:str,Capitals:dict)->str:
	"""otsing "key" sõnavars
	"""
	for key, value in Capitals.items(): # создаем цикл в котором проверяем значения
		if val == value: # если значение совподает с переменной
			return key # возращаем ключ
	return "ei ole"