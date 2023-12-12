'''importing moduels'''
from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
from urllib.error import URLError 

'''function for the scraper'''
def data(url):
	try:
		response = requests.get(url)
	except HTTPError as e:
	 	print(e)
	except URLError as e:
	 	print('The server could not be found!')
	else:
		data = response.text
		soup = BeautifulSoup(data,'html.parser')
		items = soup.find_all('div',{'class':"listing__content__wrapper"})
		for item in items:
		    contact = item.find('h4').text
		    cname =item.find('a',{'class':"listing__name--link listing__link jsListingName"}).text[2:]
		    print('Company Name:',cname)
		    print('Çontact:',contact)

'''function calling'''
data("https://www.yellowpages.ca/search/si/1/health+wellness/Toronto+ON")