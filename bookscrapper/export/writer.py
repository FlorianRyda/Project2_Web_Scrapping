import csv
import re
import shutil

import requests

from bookscrapper.constants import EXPORT_DOCUMENT
from bookscrapper.constants import SITE_URL
from bookscrapper.html_parser.book import get_book_info
from bookscrapper.html_parser.category import get_href_books


def get_and_write_books(csv_writer, page_url):
    """create csv files with book information
    and retrieve book pictures jpg files"""
    books_urls = get_href_books(page_url)
    for book_url in books_urls:
        book_info = get_book_info(book_url)
        csv_writer.writerow(book_info)
        book_info_img_url = SITE_URL + book_info[
            "Image URL"
        ].replace("../../", "/")
        book_img_title = re.sub(r"[^a-zA-Z\s]", "", book_info["Title"])
        img_file_name = (
            book_info["Category"]
            + "_"
            + book_img_title
            +".jpg")

        request = requests.get(book_info_img_url, stream=True)
        if request.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded
            # image file's size will be zero.
            request.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.

            with open(f"{EXPORT_DOCUMENT}{img_file_name}", "wb") as img:
                shutil.copyfileobj(request.raw, img)
        else:
            print(f"Image file from book {book_img_title} in category {book_info['Category']} could not be retrieved")
