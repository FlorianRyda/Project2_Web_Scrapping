from bs4 import BeautifulSoup
import requests
import csv
import Scrapping_Program as scrap_book
import Scrap_All_Categories as all_c

#this module is a work in progress
url = "http://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"

def run():
    """Calls all other functions to return all categories and book information from selected website"""
    book_info = scrap_book.get_book_info(url)
    keys = book_info.keys()
    with open('result/output_file.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, keys, dialect='excel')
        writer.writeheader()
        writer.writerows([book_info])


if __name__ == "__main__":
    run()