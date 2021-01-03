from bs4 import BeautifulSoup
import requests
import scrap_soup as soup
import csv
import scrap_all_categories as all_c


	#fonction version précédente 

	#def get_href_books(content):
		#"""return the links to all books in linked category"""
		#parsed_content = soup.get_soup(content)
		#list_category_links = []

		#next_page_end = parsed_content.select_one(".next a").text
		#category_titles = parsed_content.select(".product_pod h3")
		#for book in category_titles:
			#book_href = book.a.extract().attrs['href']
			#list_category_links.append("http://books.toscrape.com/catalogue" + book_href[8:])


		#return list_category_links



#indices ici, il faut reconstruire je pense ton code car tu as écris tes modules indépendamment
#faut lier ce module au précédent
#ci-dessus cela marche car on parse direct depuis la bonne page mais on veut récup les données du précédent module

def get_href_books(content):
	"""return the links to all books in linked category"""
	categories_urls = list(all_c.get_category_details(content).values())
	list_category_links = []

	#next_page_end = parsed_content.select_one(".next a").text
	#category_titles = categories_titles_urls.select(".product_pod h3")
	for book in categories_urls:
		#book_href = book.a.extract().attrs['href']
		list_category_links.append(book)


	return list_category_links

print(get_href_books("http://books.toscrape.com/"))