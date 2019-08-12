import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from random import choice


def get_html(url, useragent=None, proxy=None):
	r = requests.get(url, headers=useragent, proxies=proxy)
	return r.text


def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')
	tags = soup.find('table', class_='js-rum-hero').find_all('a', class_='all')
	links = []


	for tag in tags:
		tail = tag.get('href')
		links.append('https://www.kinopoisk.ru' + tail)
	for i in links[:10]:
		print(i)
	return links

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		title = soup.find('h1', class_='moviename-big').text
	except:
		title = ''
	data = {'title': title}
	return data


def write_csv(data):
	with open('kinopoisk.csv', 'a') as file:
		writer = csv.writer(file)

		writer.writerow( (data['title']) )
		print(data['title'] + ' parsed')


def main():
	start = datetime.now()
	useragents = open('useragents.txt').read().split('\n')
	proxies = open('proxies.txt').read().split('\n')

	url = 'https://www.kinopoisk.ru/top/'

	useragent = {'User_Agent': choice(useragents)}
	proxy = {'http': 'http://' + choice(proxies)}	

	all_links = get_all_links(get_html(url, useragent, proxy))

	print(all_links)
	
	for i in all_links[:2]:
		useragent = {'User_Agent': choice(useragents)}
		proxy = {'http': 'http://' + choice(proxies)}
		write_csv(get_page_data(get_html(i, useragent, proxy)))

if __name__ == '__main__':
	main()
