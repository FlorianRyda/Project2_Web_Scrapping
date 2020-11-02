from bs4 import BeautifulSoup
import requests
import csv


#Maintenant que vous avez obtenu les informations concernant un premier livre, 
#vous pouvez essayer de récupérer toutes les données nécessaires 
#pour toute une catégorie d'ouvrages. 
#Choisissez n'importe quelle catégorie sur le site de Books to Scrape. 
#Écrivez un script Python qui consulte la page de la catégorie choisie, 
#et extrait l'URL de la page Produit de chaque livre appartenant à cette catégorie. 
#Combinez cela avec le travail que vous avez déjà effectué afin d'extraire 
#les données produit de tous les livres de la catégorie choisie, 
#puis écrivez les données dans un seul fichier CSV.

#Remarque : certaines pages de catégorie comptent plus de 20 livres, qui sont donc répartis sur différentes pages 
#(«  pagination  »). 
#Votre application doit être capable de parcourir automatiquement les multiples pages si présentes. 

category_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

def get_category_urls(category_url):
	"""return all the category's book URLs"""
	response = requests.get(category_url)
	if response.status_code != 200:
		raise Exception("couldn't pull information!/ URL not valid")
	return BeautifulSoup(response.content, features='html.parser')

def get_href_books(content):
	"""return the links to all books in linked category"""
	parsed_content = get_category_urls(category_url)
	category_links = parsed_content.findAll('a')[54:]
	strip_category_links = []
	for bookdetail in category_links:
		book_detail_href = bookdetail.get('href')
		strip_category_links.append(book_detail_href)
	return strip_category_links

category = get_href_books(get_category_urls(category_url))
print (category)

#missing here, you need to iterate through several pages, thanks to the url
#a for loop smight do the trick! need to see if you can stop it perfectly