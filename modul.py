def find_word(Capitals:dict):
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
	print(ans)

