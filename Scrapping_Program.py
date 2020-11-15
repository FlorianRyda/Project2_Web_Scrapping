from bs4 import BeautifulSoup
import requests
import csv


def get_content(url):
	"""gets html information from werbsite and returns parsed object"""
	response = requests.get(url)
	if response.status_code != 200:
		raise Exception("couldn't pull information!/ URL not valid")
	return BeautifulSoup(response.content, features='html.parser')


def get_book_rating(url):
	"""gets and returns the rating from selected book"""
	book_info_rating = str((get_content(url)))
	if "star-rating Four" in book_info_rating:
		return ("Four Stars")
	elif "star-rating Three" in book_info_rating:
		return ("Three Stars")
	elif "star-rating Two" in book_info_rating:
		return ("Two Stars")
	elif "star-rating One" in book_info_rating:
		return ("One Star")
	else:
		return ("No Rating Available")

def get_book_info(url):
    """
    convert pulled elements to strings of text
    associate each value to a key in a dictionnary and append it in the empty list
    """
    parsed_content = get_content(url)
    book_info_rating = get_book_rating(url)

    book_info_title = parsed_content.select('h1')[0].text.strip()
    book_info_category = parsed_content.select('ul li a')[2].text.strip()
    book_info_description = parsed_content.select('.product_page p')[3].text.strip()
    book_info_img_url = parsed_content.select('img')[0].get('src')
    book_info_upc = parsed_content.select('td')[0].text.strip()
    book_price_excl_tax = parsed_content.select('td')[2].text.strip()
    book_price_incl_tax = parsed_content.select('td')[3].text.strip()
    book_available = parsed_content.select('td')[5].text.strip()

    return {
        "URL" : url,
        "Title": book_info_title,
        "Category": book_info_category,
        "Description" : book_info_description,
        "Image URL" : book_info_img_url,
        "UPC" : book_info_upc,
        "Price Excluding Tax" : book_price_excl_tax,
        "Price Incuding Tax" : book_price_incl_tax,
        "Availability" : book_available,
        "Review Rating" : book_info_rating
    }


