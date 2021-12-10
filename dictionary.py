from modul import*
Capitals={}
with open("Cap.txt","r") as f:
	for i in f: # создаем цикл по кол-ву строк
		k,v=i.strip().split("-") # отделяем слова на строчке в строчке по знаку "-"
		Capitals[k.strip()]=v.strip() # добавляем в словарь
print(Capitals)
while True:
	c=input("Otsing sõna sõnavaras - 1, muutma sõna tähendus - 2, test - 3, välja - 4")
	if c=="1":
		ans,a=find_word(Capitals)
		print(ans)
		if ans=="See sõna ei olema": # если слова нет в словаре спрашиваем хочет ли пользователь добавить это слово
			b=input("Kas te tahate lisa sõna sõnavars, 1-jah 2-ei >>> ")
			if b=="1": # если да 
				Capitals=add_word(Capitals,a) # используем функцию добавления в словарь и из поиска слова берем переменную а которая будет ключем
			else:
				pass
		else:
			pass
	elif c=="2":
		Capitals=change_smth(Capitals)
	elif c=="3":
		result=testingknoledge(Capitals)
		print("Sinu resultat on "+str(result)+"%") # на экране показываем ответ
	elif c=="4": # заканчиваем цикл
		with open("Cap.txt", "w") as f:
			for key, value in Capitals.items(): # создаем цикл по кол-ву ключей
				f.write(key+"-"+value+"\n") # перезаписать словарь в файл
		break
	else:
		print("See funktioon ei olema")
		