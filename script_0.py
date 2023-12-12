from bs4 import BeautifulSoup
import requests 
def data(url):

	response = requests.get(url)

	print(response)

	data = response.text
	soup = BeautifulSoup(data,'html.parser')
	items = soup.find_all('div',{'class':"listing__content__wrapper"})
	for item in items:
	    contact = item.find('h4').text
	    cname =item.find('a',{'class':"listing__name--link listing__link jsListingName"}).text[2:]
	    print('Company Name:',cname)
	    print('Çontact:',contact)
data("https://www.yellowpages.ca/search/si/1/health+wellness/Toronto+ON") 