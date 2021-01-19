from bookscrapper.requester import get_soup


def get_pages_number(category_url):
	"""gets number of pages in category and returns it"""
	soup_object = get_soup(category_url)
	try:
		return int((soup_object.select_one(".current").text).split()[-1])
	except AttributeError:
		return 1
