import csv

import requests

from bookscrapper.constants import SITE_URL
from bookscrapper.constants import EXPORT_DOCUMENT
from bookscrapper.export.writer import get_and_write_books
from bookscrapper.html_parser.all_categories import get_category_details
from bookscrapper.html_parser.pagination import get_pages_number



def run():
    """Creates csv and writes files with book information"""
    website_url = SITE_URL
    categories = get_category_details(website_url)

    for category_name, category_url in categories.items():
        with open(
            f"{EXPORT_DOCUMENT}{category_name}.csv",
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file:
            fields = [
                "URL",
                "Title",
                "Category",
                "Description",
                "Image URL",
                "UPC",
                "Price Excluding Tax",
                "Price Including Tax",
                "Availability",
                "Review Rating",
            ]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fields, dialect="excel")
            csv_writer.writeheader()
            get_and_write_books(csv_writer, category_url)
            category_pages = get_pages_number(category_url)
            if category_pages > 1:
                for i in range(category_pages - 1):
                    page_url = category_url[:-10] + f"page-{i + 2}.html"
                    get_and_write_books(csv_writer, page_url)


if __name__ == "__main__":
    run()
