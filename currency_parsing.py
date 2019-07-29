# 1. Парсер однопоточный
# 2. Замер времени
# 3. Библиотека multiprocessing, класс Pool
# 4. Замер времени
# 5. Экспорт данных в csv файл


import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool

def get_html(url):
	r = requests.get(url) # Получаем объект класса Response
	return r.text		# Возвращает html-код страницы, которая передана в качестве аргумента функции (то есть url)


def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml') # Первый аргумент - html, второй аргумент - название парсера
	tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name') # Здесь после выполнения всех этих штук будет список объектов супа, 
																							# к которым применимы все методы и свойства объеков супа
	links = []

	for td in tds:
		a = td.find('a').get('href') # Здесь каждая а - это уже не объект супа, а строка
		link = 'https://coinmarketcap.com' + a
		links.append(link)

	return links



def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	try:
		name = soup.find('h1', class_='details-panel-item--name').find('span').previous.strip() # .text используется, чтобы забрать текст из объекта супа, а .strip() используется, чтобы его очистить от непечатаемых символов
	# else:
	# 	name = soup.find('span', class_='text-large').text.strip()
	except:
		name = ''

	try:
		price = soup.find('span', id='quote_price').find('span', class_='details-panel-item--price__value').text.strip()
	except:
		price = ''

	data = {'name': name,
			'price': price}
	return data

def write_csv(data):
	with open ('coinmarketcap.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['name'],
						data['price']))

		print(data['name'], 'parsed')


def make_all(url):
	html = get_html(url)
	data = get_page_data(html)
	write_csv(data)


def main():
	start = datetime.now()

	url =  'https://coinmarketcap.com/all/views/all/'

	all_links = get_all_links(get_html(url))

	# for index, url in enumerate(all_links):
	
	

	with Pool(40) as p:
		p.map(make_all, all_links)



	end = datetime.now()
	total = end - start
	print(str(total))


if __name__ == '__main__':
	main()