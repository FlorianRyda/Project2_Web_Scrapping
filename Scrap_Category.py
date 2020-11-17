from bs4 import BeautifulSoup
import requests
import scrap_soup as soup
import csv


def get_href_books(content):
	"""return the links to all books in linked category"""
	parsed_content = soup.get_soup(content)
	list_category_links = []


	next_page_end = parsed_content.select_one(".next a").text
	category_titles = parsed_content.select(".product_pod h3")
	for book in category_titles:
		book_href = book.a.extract().attrs['href']
		list_category_links.append(book_href)


	return list_category_links