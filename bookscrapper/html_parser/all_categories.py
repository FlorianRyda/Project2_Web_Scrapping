from bookscrapper.requester import get_soup

def get_category_details(website_url):
    """returns names and URLs of categories in a dictionnary"""
    soup_object = get_soup(website_url)
    categories = soup_object.select(".side_categories li ul li a")
    categories_details = {}

    for element in categories:
        title = element.get_text('a').strip()
        url = "http://books.toscrape.com/" + str(element.get('href'))
        categories_details[title] = url

    return categories_details