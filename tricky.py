import requests
from bs4 import BeautifulSoup
import csv
from random import choice, uniform
from time import sleep
from datetime import datetime

# Самая удачная конфигурация серверов: https://take.ms/oklub (особенно см. анонимити и https)

def get_html(url, useragent=None, proxy=None):
	#print('get_html')
	r = requests.get(url, headers=useragent, proxies=proxy)
	return r.text


def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')
	tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
	links = []

	for td in tds:
		a = td.find('a').get('href')
		link = 'https://coinmarketcap.com' + a
		links.append(link)

	return links

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	
	name = soup.find('h1', class_='details-panel-item--name').find('span').previous.strip() # .text используется, чтобы забрать текст из объекта супа,
																								# а .strip() используется, чтобы его очистить от непечатаемых символов

	try:
		price = soup.find('span', id='quote_price').find('span', class_='details-panel-item--price__value').text.strip()
	except:
		price = ''

	data = {'name': name,
			'price': price}
	return data


def write_csv(data):
	with open ('tricky.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['name'],
						data['price']))

		print(data['name'], 'parsed')

def main():
	start = datetime.now()

	url =  'https://coinmarketcap.com/all/views/all/'

	useragents = open('useragents.txt').read().split('\n')
	proxies = open('proxies.txt').read().split('\n')

	useragent = {'User-Agent': choice(useragents)}
	proxy = {'http': 'http://' + choice(proxies)}

	all_links = get_all_links(get_html(url, useragent, proxy))

	number = 0
	for i in range(120):
		t = uniform(3, 12)
		sleep(t)
		number += 1
		print(number)
		url = all_links[i]
		
		
		while True:
			try:
				useragent = {'User-Agent': choice(useragents)}
				proxy = {'http': 'http://' + choice(proxies)}
				html = get_html(url, useragent, proxy)
				data = get_page_data(html)
				write_csv(data)
				print(data)
			except AttributeError:
				continue
			break

	end = datetime.now()
	total = end - start
	print(str(total))

if __name__ == '__main__':
	main()
