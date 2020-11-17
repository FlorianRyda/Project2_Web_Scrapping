from bs4 import BeautifulSoup
import requests
import scrap_soup as soup
import csv



def get_category_details(website_url):
	"""returns names and URLs of categories in a dictionnary"""
	soup_object = soup.get_soup(website_url)
	categories = soup_object.select(".side_categories li ul li a")
	categories_details = {}

	for element in categories:
		title = element.get_text('a').strip()
		url = "http://" + str(element.get('href'))
		categories_details[title] = url

	return categories_details

