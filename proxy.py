from bs4 import BeautifulSoup
import requests
from random import choice
from time import sleep
from random import uniform



def get_html(url, useragent=None, proxy=None):
	print('get_html')
	r = requests.get(url, headers=useragent, proxies=proxy)
	return r.text


def get_ip(html):
	print('New Proxy & User-Agent:')
	soup = BeautifulSoup(html, 'lxml')
	ip = soup.find('span', class_='ip').text.strip()
	ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
	print(ip)
	print(ua)
	# curl('http://ipinfo.io/ip')
	print('-----------------------')


def main():
	url = 'http://sitespy.ru/my-ip'
	useragents = open('useragents.txt').read().split('\n')
	proxies = open('proxies.txt').read().split('\n')


	for i in range(10):
		a = uniform(1, 3)
		print(a)
		sleep(a)

		useragent = {'User-Agent': choice(useragents)}
		proxy = {'http': 'http://' + choice(proxies)}
		
		try:
			html = get_html(url, useragent, proxy)
		except:
			print('---FAILED---')
			continue

		get_ip(html)



if __name__ == "__main__":
	main()