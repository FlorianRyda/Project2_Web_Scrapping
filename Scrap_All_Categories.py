from bs4 import BeautifulSoup
import requests
import csv


def get_website_info(website_url):
	"""return all html from website chosen"""
	response = requests.get(website_url)
	if response.status_code != 200:
		raise Exception("couldn't pull information!/ URL not valid")
	return BeautifulSoup(response.content, features='html.parser')



def get_category_details(website_url):
	"""returns names and URLs of categories in a dictionnary"""
	soup_object = get_website_info(website_url)
	category = soup_object.select(".side_categories li ul li a")
	dico = {}

	for element in category:
		title = element.get_text('a').strip()
		url = "http://" + str(element.get('href'))
		dico[title] = url

	return dico

print(get_category_details("http://books.toscrape.com/index.html"))