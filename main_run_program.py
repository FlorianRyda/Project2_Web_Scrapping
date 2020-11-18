from bs4 import BeautifulSoup
import requests
import urllib3
import csv
import scrapping_program_book as scrap_book
import scrap_all_categories as all_c
import scrap_category_pagination as num_pages
import scrap_category as scrap_cat
import scrap_soup as soup

#this module is a work in progress
def run():
    """Calls all other functions to return all categories and book information from selected website"""
    url = "http://books.toscrape.com/"

    categories = all_c.get_category_details(url)

    with open('result/output_file', 'w', newline ='') as category_csv:
	    for category_name, category_url in categories.items():
	    	csv_doc = csv.writer(category_csv)
	    	category_pages = num_pages.get_pages_number(category_url)

	    	for i in range(category_pages):
	    		category_page_url = f"http://books.toscrape.com/category/{category_name}/page-{i + 1}.html"
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