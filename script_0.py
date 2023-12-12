'''importing moduels'''
from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
from urllib.error import URLError 
import csv

#empty list for storing items
all_items= []

'''function for the scraper'''
def data(url):

	#error handling
	try:
		response = requests.get(url)
	except HTTPError as error:
	 	print(error)
	except URLError as error:
	 	print('The server could not be found!')
	else:
		data = response.text
		soup = BeautifulSoup(data,'html.parser')
		items = soup.find_all('div',{'class':"listing__content__wrapper"})
		for item in items:
		    contact = item.find('h4').text
		    cname =item.find('a',{'class':"listing__name--link listing__link jsListingName"}).text[2:]
		    print('Company Name:',cname.strip())
		    print('Çontact:',contact.strip())

		    #appensing all the data into the empty list
		    all_items.append({"Company Name":cname,"Contact":contact})
		    keys=all_items[0].keys()

		    #writign data to csv file
		    with open('items.csv','w',newline='') as file:
		    	dict_writer=csv.DictWriter(file, keys)
		    	dict_writer.writeheader()
		    	dict_writer.writerows(all_items)
	file.close()
'''function calling'''
data("https://www.yellowpages.ca/search/si/1/health+wellness/Toronto+ON")