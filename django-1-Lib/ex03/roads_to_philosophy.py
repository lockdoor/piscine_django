import requests
from bs4 import BeautifulSoup
import sys

def my_func():
	if len(sys.argv) != 2:
		exit("Usage: python3 roads_to_philosophy.py string_to_find")
	href = '/wiki/' + sys.argv[1]
	titles = []
	titles.append(sys.argv[1])
	while "Philosophy" not in titles:
		page = requests.get(f"https://en.wikipedia.org{href}")
		if page is None or page.status_code != 200:
			exit("It leads to a dead end!") 
		soup = BeautifulSoup(page.text, features="html.parser")
		bodyContent = soup.find(id="bodyContent")
		paragraph_list = bodyContent.find_all('p')
		is_href = False
		for p in paragraph_list:
			link = p.a
			if link:
				is_href = True
				href = link.get("href")
				title = link.get("title")
				if title in titles:
					exit("It leads to an infinite loop ! ")
				titles.append(title)
				break
		if not is_href:
			exit("It leads to a dead end!")
	for title in titles:
		print(title)
	print(f'{len(titles)} roads from {sys.argv[1]} to philosophy')	

if __name__ == "__main__":
	my_func()

'''
# chat_improve.py
def my_func():
	if len(sys.argv) != 2:
		exit("Usage: python3 roads_to_philosophy.py <string_to_find>")

	# Initialize starting point
	href = '/wiki/' + sys.argv[1]
	titles = [sys.argv[1]]  # Track visited titles

	while "Philosophy" not in titles:
		# Fetch the Wikipedia page
		page = requests.get(f"https://en.wikipedia.org{href}")
		if page is None or page.status_code != 200:
			exit("It leads to a dead end!")
		
		# Parse page content using BeautifulSoup
		soup = BeautifulSoup(page.text, features="html.parser")
		body_content = soup.find(id="bodyContent")
		if body_content is None:
			exit("It leads to a dead end!")
		
		# Find all paragraphs
		paragraph_list = body_content.findAll('p')
		is_href = False

		for p in paragraph_list:
			# Exclude parenthesis content (links in parenthesis should be ignored)
			for parenthesis in p.findAll('i'):
				parenthesis.decompose()

			# Find the first valid link
			for link in p.findAll('a'):
				href = link.get("href")
				title = link.get("title")
				
				# Check if the link points to a valid Wikipedia article
				if href and href.startswith('/wiki/') and ':' not in href:
					if title in titles:
						exit("It leads to an infinite loop!")
					
					# Valid link found, process it
					is_href = True
					titles.append(title)
					break
			
			if is_href:
				break

		# If no valid link found in the paragraphs
		if not is_href:
			exit("It leads to a dead end!")

	# Output the sequence of titles and number of steps
	for title in titles:
		print(title)
	print(f'{len(titles)} roads from {sys.argv[1]} to philosophy.')
'''