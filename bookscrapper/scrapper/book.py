from bs4 import BeautifulSoup
import requests
import urllib3
import scrapper.requester

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def get_book_rating(url):
    """gets and returns the rating from selected book"""
    book_info_rating = str((scrapper.requester.get_soup(url)))
    if "star-rating Four" in book_info_rating:
        return 4
    elif "star-rating Three" in book_info_rating:
        return 3
    elif "star-rating Two" in book_info_rating:
        return 2
    elif "star-rating One" in book_info_rating:
        return 1
    else:
        return ("No Rating Found")


def get_book_info(url):
    """
    convert pulled elements to strings of text
    and return a dictionnary.
    """
    parsed_content = scrapper.requester.get_soup(url)
    book_info_rating = get_book_rating(url)
    book_info_title = parsed_content.select('h1')[0].text.strip()
    book_info_category = parsed_content.select('ul li a')[2].text.strip()
    book_info_description = parsed_content.select('.product_page p')[
        3].text.strip()
    book_info_img_url = parsed_content.select('img')[0].get('src')
    book_info_upc = parsed_content.select('td')[0].text.strip()
    book_price_excl_tax = parsed_content.select('td')[2].text.strip()
    book_price_incl_tax = parsed_content.select('td')[3].text.strip()
    book_available = parsed_content.select('td')[5].text.strip()

    return {
        "URL": url,
        "Title": book_info_title,
        "Category": book_info_category,
        "Description": book_info_description,
        "Image URL": book_info_img_url,
        "UPC": book_info_upc,
        "Price Excluding Tax": book_price_excl_tax,
        "Price Including Tax": book_price_incl_tax,
        "Availability": book_available,
        "Review Rating": book_info_rating
    }


    