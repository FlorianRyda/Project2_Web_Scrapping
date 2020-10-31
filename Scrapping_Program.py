from bs4 import BeautifulSoup
import requests
import csv


url = "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
#pull the code from the website and parse it
def get_content(url):
	pullUrl = requests.get(url)
	if pullUrl.status_code != 200:
		raise Exception("couldn't pull information!/ URL not valid")
	request = BeautifulSoup(pullUrl.content, features='html.parser')
	return request


def get_book_rating(content):
	#gets the rating from class name
	bookInfoRating = str((get_content(url).body))
	if "star-rating Four" in bookInfoRating:
		return ("Four Stars")
	elif "star-rating Three" in bookInfoRating:
		return ("Three Stars")
	elif "star-rating Two" in bookInfoRating:
		return ("Two Stars")
	elif "star-rating One" in bookInfoRating:
		return ("One Star")
	else:
		return ("No Rating Available")


#start empty list 
bookInfo = []
#convert pulled elements to strings of text
#associate each value to a key in a dictionnary and append it in the empty list
def get_book_info(content):
	all_info = get_content(url)
	for info in all_info:
		bookInfoTitle = all_info.select('h1')[0].text.strip()
		bookInfoCategory = all_info.select('ul li a')[2].text.strip()
		bookInfoDescription = all_info.select('.product_page p')[3].text.strip()
		bookInfoImgUrl = all_info.select('img')[0].get('src')
		bookInfoUPC = all_info.select('td')[0].text.strip()
		bookPriceExclTax = all_info.select('td')[2].text.strip()
		bookPriceInclTax = all_info.select('td')[3].text.strip()
		BookAvailable = all_info.select('td')[5].text.strip()

		bookInfo.append(
			{"URL" : url,
			"Title": bookInfoTitle,
			"Category": bookInfoCategory,
			"Description" : bookInfoDescription,
			"Image URL" : bookInfoImgUrl,
			"UPC" : bookInfoUPC,
			"Price Excluding Tax" : bookPriceExclTax,
			"Price Incuding Tax" : bookPriceInclTax,
			"Availability" : BookAvailable,
			"Review Rating" : get_book_rating(get_content(url))
			})
		return bookInfo

get_book_info(get_content(url))
keys = bookInfo[0].keys()


with open('Output_file','w',newline='') as csvfile:
	writer = csv.DictWriter(csvfile, keys, dialect='excel')
	for csv in csvfile:
		writer.writeheader()
		writer.writerows(bookInfo)
	

