import requests
import csv
import scrapper.book
import scrapper.category
import shutil
import re



def get_and_write_books(csv_writer, page_url):
    """create csv files with book information 
    and retrieve book pictures jpg files"""
    books_urls = scrapper.category.get_href_books(page_url)
    for book_url in books_urls:
        book_info = scrapper.book.get_book_info(book_url)
        csv_writer.writerow(book_info)
        book_info_img_url = "https://books.toscrape.com" + \
            book_info['Image URL'].replace("../../", "/")
        book_img_title = re.sub(r"[^a-zA-Z\s]", "", book_info['Title'])
        img_file_name = book_info['Category'] + '_' + \
            book_img_title + '_' + book_info_img_url.split('/')[-1]

        request = requests.get(book_info_img_url, stream=True)
        if request.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded
            # image file's size will be zero.
            request.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(f'result/{img_file_name}', "wb") as img:
                shutil.copyfileobj(request.raw, img)
            print('Image retrieved successfully')
        else:
            print('Image not retrieved')