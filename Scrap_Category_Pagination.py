from bs4 import BeautifulSoup
import requests
import scrap_soup as soup
import csv

def get_pages_number(category_url):
	"""gets number of pages in category and returns it"""
	soup_object = soup.get_soup(category_url)

	total_pages = (soup_object.select_one(".current").text).split()[-1]
	return total_pages
