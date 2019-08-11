import requests
from bs4 import BeautifulSoup




def get_html(url):
	r = requests.get(url)
	return r.text


def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')
	tags = soup.find('table', class_='js-rum-hero').find_all('a', class_='all')
	links = []


	for tag in tags:
		tail = tag.get('href')
		links.append('https://www.kinopoisk.ru' + tail)
	
	return links



def main():
	url = 'https://www.kinopoisk.ru/top/'

	all_links = get_all_links(get_html(url))
	
	#я подаю вот эту вот алл линкс в функцию которая берет каждый элемент списка и кидает как линку в гет_хтмл.
	#затем получает синтаксическую версию каждой из 250 страниц по очереди и по очереди же парсит, 
	#доставая оттуда название фильма, оценку на кинопоиске, оценку на аймдиби и ченить еще









if __name__ == '__main__':
	main()