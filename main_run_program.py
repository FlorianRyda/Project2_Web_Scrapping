from bs4 import BeautifulSoup
import requests
import urllib3
import csv
import scrapping_program_book as scrap_book
import scrap_all_categories as all_c
import scrap_category_pagination as num_pages
import scrap_category as scrap_cat
import scrap_soup as soup




def get_and_write_books(csv_writer, page_url):
    books_urls = scrap_cat.get_href_books(page_url)
    for book_url in books_urls:
        book_info = scrap_book.get_book_info(book_url)
        csv_writer.writeDict(book_info)


def run():
    website_url = "http://books.toscrape.com/"


    categories = all_c.get_category_details(website_url)
    for category_name, category_url in categories.items():
        with open(f'result/{category_name}.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            get_and_write_books(csv_writer, category_url)

            category_pages = num_pages.get_pages_number(category_url)
            if category_pages > 1:
                for i in range(category_pages):
                    page_url = category_url[:-10] + f"page-{i + 2}.html"
                    get_and_write_books(page_url)




if __name__ == "__main__":
   run()

#book_info = scrap_book.get_book_info(url)
#keys = book_info.keys()
#with open('result/output_file.csv', 'w', newline='') as csvfile:
#    #writer = csv.DictWriter(csvfile, keys, dialect='excel')
#    #writer.writeheader()
#    #writer.writerows([book_info])