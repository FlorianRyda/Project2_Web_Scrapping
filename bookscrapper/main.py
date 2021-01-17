import requests
import csv
from parser.all_categories import get_category_details
import parser.pagination
import export.writer


def run():
    """Creates csv and writes files with book information"""
    website_url = "http://books.toscrape.com/"
    categories = scrapper.all_categories.get_category_details(website_url)

    for category_name, category_url in categories.items():
        with open(f'result/{category_name}.csv', 'w', newline='', 
                 encoding='utf-8') as csv_file:
            fields = ['URL', 'Title', 'Category', 'Description', 'Image URL', 'UPC',
                      'Price Excluding Tax', 'Price Including Tax', 
                      'Availability', 'Review Rating']
            csv_writer = csv.DictWriter(
                csv_file, fieldnames=fields, dialect='excel')
            csv_writer.writeheader()
            scrapper.writer.get_and_write_books(csv_writer, category_url)
            category_pages = pagination.get_pages_number(category_url)
            if category_pages > 1:
                for i in range(category_pages-1):
                    page_url = category_url[:-10] + f"page-{i + 2}.html"
                    get_and_write_books(csv_writer, page_url)


if __name__ == "__main__":
    run()
