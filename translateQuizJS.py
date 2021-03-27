import os
import re

FullWords = open('words.txt', 'r')
NewWords = open('newWords.txt', 'w')

for line in FullWords:
	f = ('text: \'Напишите слово ' + line.strip())
	# Удаление цифры из строки
	f = re.sub(r'\d+\.','',f)
	# Строка 'text: Напишите слово '
	defaultString = f[0: 21]
	# перевод слова
	russianText = f[22:]
	#Слово на англ
	englText = re.findall(r'\w+', russianText)[0]
	# Слова на русском
	russianText = " ".join(russianText.split()[1:])
	# Вывод первой строки
	firstString = defaultString + ' ' + '"' + russianText + '"' + ' на англ.,'
	secondString = 'right: ' + "'" + englText + "',"
	thirdString = 'help: ' + "'" + englText + "'"
	#print('{' + '\n' + firstString + '\n' + secondString + '\n' + thirdString + '\n' + '},')
	NewWords.write('{' + '\n' + firstString + '\n' + secondString + '\n' + thirdString + '\n' + '},')