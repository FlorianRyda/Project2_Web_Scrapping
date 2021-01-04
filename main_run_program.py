from bs4 import BeautifulSoup
import requests
import urllib3
import csv
import scrapping_program_book as scrap_book
import scrap_all_categories as all_c
import scrap_category_pagination as num_pages
import scrap_category as scrap_cat
import scrap_soup as soup
import shutil
import re

def get_and_write_books(csv_writer, page_url):
    """create csv files with book information"""
    books_urls = scrap_cat.get_href_books(page_url)
    csv_writer.writeheader()
    
    for book_url in books_urls:
        book_info = scrap_book.get_book_info(book_url)
        csv_writer.writerow(book_info)
        
        book_info_img_url = "https://books.toscrape.com" + book_info['Image URL'].replace("../../","/")
        book_img_title = re.sub(r"[^a-zA-Z\s]", "", book_info['Title'])

        img_file_name =  book_info['Category'] + '_' + book_info_title_quotes_removed + '_' + book_info_img_url.split('/')[-1]
        print(Img_File_Name)

        request = requests.get(book_info_img_url, stream = True)
        if request.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            request.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(f'result/{img_file_name}',"wb") as img:
                shutil.copyfileobj(request.raw, img)
            print('Image retrieved successfully')
        else:
            print('Image not retrieved')

def run():
    """Creates DictWriter object and calls function to create csv files with book information"""
    website_url = "http://books.toscrape.com/"
    categories = all_c.get_category_details(website_url)

    for category_name, category_url in categories.items():
        with open(f'result/{category_name}.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fields = ['URL','Title','Category','Description','Image URL','UPC',
            'Price Excluding Tax','Price Including Tax','Availability','Review Rating']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fields, dialect='excel')
            get_and_write_books(csv_writer, category_url)
           
            category_pages = num_pages.get_pages_number(category_url)
            if category_pages > 1:
                for i in range(category_pages-1):
                    page_url = category_url[:-10] + f"page-{i + 2}.html"
                    get_and_write_books(csv_writer, page_url)

if __name__ == "__main__":
   run()

