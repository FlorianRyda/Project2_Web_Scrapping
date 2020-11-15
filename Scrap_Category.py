from bs4 import BeautifulSoup
import requests
import csv


def get_soup(category_url):
	"""return all the category's book URLs"""
	response = requests.get(category_url)
	if response.status_code != 200:
		raise Exception("couldn't pull information!/ URL not valid")
	return BeautifulSoup(response.content, features='html.parser')



def get_href_books(content):
	"""return the links to all books in linked category"""
	parsed_content = get_category_urls(content)
	list_category_links = []


	next_page_end = (parsed_content.select_one(".next a")).text
	one_category = parsed_content.select(".product_pod h3")
	for book in one_category:
		book_href = (book.a.extract()).attrs['href']
		list_category_links.append(book_href)


	return list_category_links


	
