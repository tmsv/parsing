from bs4 import BeautifulSoup
import re

def main():
	html = open('index.html').read()
	soup = BeautifulSoup(html, 'lxml')

	# Первый способ задания аргументов для поиска
	# div = soup.find("div", class_='links')
	
	# Второй способ - через словарь
	# div = soup.find('div', {'class': 'links'})

	# links = soup.find_all('a')
	# # for i in links:
	# # 	print(i)

	# for i in links:
	# 	link = i.get('href')
	# 	print(link)

	# parent = find_parent()  Аналогичен методу find()
	# parents = find_parents()  Аналогичен методу find_all()

	# Ищем родителя
	# div = soup.find('h1').find_parent('div', class_='one')
	# print(div)

	# Знакомство с next_element
	# text = soup.find('h1').next_element.next_element.next_element.next_element.next_element.next_element.next_element
	# print(text)

	# Парсинг по маске элемента на примере ссылки
	# a = soup.find('a', href=re.compile('oo'))
	# url = a.get('href')
	# print(url)

	# Парсинг атрибутов
	# div = soup.find('h1').parent
	# n = div.get('data-set')
	# print(n)

	# Используем регулярные выражения
	# a = soup.find('a', href=re.compile('bing.com$'))
	# a = soup.find('a', text=re.compile('second'))
	
	# Ищем дату с помощью регулярных выражений
	# \d означает digit (цифра)
	# \w означает буквенные символы + цифры + нижние подчеркивания _
	# \w- означает диапазон, например, от a-z
	# если мы хотим найти прямо сочетание "w-", то мы должны экранировать слэш: "\w\-"
	# \^ означает начало строки. "^hello" - дай мне результат, который начинается с "hello"
	regexp = r'\d{2}.\d{2}.\d{4}'
	date = soup.find_all(text=re.compile(regexp))
	for i in date:
		print(i)

if __name__ == "__main__":
	main()