from bookscrapper.constants import site_url
from bookscrapper.requester.requester import get_soup


def get_href_books(category_url):
    """return the links to all books in page 1 of each category"""
    list_category_links = []
    soup_object = get_soup(category_url)
    book_select = soup_object.select("h3 a")
    for book in book_select:
        book_href = book.get("href", None)
        book_href = book_href.replace("../../..", "catalogue")

        book_url = site_url + str(book_href)
        list_category_links.append(book_url)

    return list_category_links
