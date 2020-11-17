from bs4 import BeautifulSoup
import requests
import csv
import Scrapping_Program as scrap_book
import Scrap_All_Categories as all_c
import Scrap_Category_Pagination as num_pages
import Scrap_Category as scrap_cat
import scrap_soup as soup

#this module is a work in progress
url = "http://books.toscrape.com/index.html"

def run():
    """Calls all other functions to return all categories and book information from selected website"""
    categories = all_c.get_category_details(url)

    with open('result/output_file', 'w', newline ='') as category_csv:
	    for category_name, category_url in categories.items():
	    	csv_doc = csv.writer(category_csv)
	    	category_pages = num_pages.get_pages_number(category_url)

	    	for i in range(category_pages):
	    		category_page_url = f"http://books.com/category/mystery/page-{i + 1}.html"
	    		books_urls = scrap_cat.get_href_books(category_page_url)

	    		for book_url in books_urls:
	    			book_info = scrap_book.get_book_info(book_url)
	    			csv.writeDict(book_info)


    #book_info = scrap_book.get_book_info(url)
    #keys = book_info.keys()
    #with open('result/output_file.csv', 'w', newline='') as csvfile:
        #writer = csv.DictWriter(csvfile, keys, dialect='excel')
        #writer.writeheader()
        #writer.writerows([book_info])


if __name__ == "__main__":
    run()