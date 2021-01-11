from bs4 import BeautifulSoup
import requests
import scrapper.requester


def get_href_books(category_url):
    """return the links to all books in page 1 of each category"""
    list_category_links = []
    soup_object = scrapper.requester.get_soup(category_url)
    book_select = soup_object.select("h3 a")
    for book in book_select:
        book_href = book.get('href', None)
        book_href = book_href.replace("../../..", "catalogue")

        book_url = "http://books.toscrape.com/" + str(book_href)
        list_category_links.append(book_url)

    return list_category_links
