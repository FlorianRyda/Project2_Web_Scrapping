from bs4 import BeautifulSoup
import requests

def get_soup(website_url):
	"""return all html from website chosen"""
	response = requests.get(website_url)
	if response.status_code != 200:
		raise Exception(f"couldn't pull information for {website_url}!")
	return BeautifulSoup(response.content, features='html.parser')