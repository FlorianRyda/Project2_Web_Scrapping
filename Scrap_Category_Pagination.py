from bs4 import BeautifulSoup
import requests
import csv


def get_soup(website_url):
	"""return all html from website chosen"""
	response = requests.get(website_url)
	if response.status_code != 200:
		raise Exception(f"couldn't pull information for {website_url}!")
	return BeautifulSoup(response.content, features='html.parser')

def get_pages_number(category_url):
	"""gets number of pages in category and returns it"""
	soup_object = get_soup(category_url)

	total_pages = (soup_object.select_one(".current").text).split()[-1]
	return total_pages



