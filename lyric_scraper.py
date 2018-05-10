from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import re
import sys

# req = Request("https://genius.com/The-weeknd-cant-feel-my-face-lyrics",  headers={'User-Agent': 'Mozilla/5.0'})
KEYWORDS = ["Introduction", "Intro",
			"Verse",
			"Refrain",
			"Pre-Chorus", "Climb",
			"Chorus",
			"Post-Chorus",
			"Hooks",
			"Riffs/Basslines",
			"Scratches",
			"Sampling",
			"Bridge",
			"Interlude",
			"Skit",
			"Collision",
			"Instrumental", "Solo",
			"Ad lib",
			"Segue",
			"Outro"]

def compute(artist, song):
	url = "https://genius.com/"
	for word in artist.split(' '):
		url+= word+"-"
	for word in song.split(' '):
		url+= word+"-"
	url += "lyrics"
	# print(url)
	try:
		scraped = scrape(url)
	except urllib.error.HTTPError:
		print("url not found")
		scraped = "lyrics not found"
		

	# scraped = scrape(url)
	return scraped


def scrape(url):
	"""returns array of song structure"""
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	body = urlopen(req).read()
	soup = BeautifulSoup(body, 'html.parser')
	section = soup.find('div', {"class": "lyrics"}).find_all("p")
	text = ' '.join([item.text for item in section])
	#use regex to pattern match all things in brakcets
	match = re.findall(r'\[(.*?)\]', text)
	if match:
		cleaned = []
		for m in match:
			#cleaning titles
			new = m.split(' ', 1)[0]
			if new in KEYWORDS:
				cleaned.append(new)
	return cleaned
def main():

	#text scraping from lyrics part of the webpage
	if len(sys.argv) > 1:
		url = "https://genius.com/"
		for word in sys.argv[1:]:
			url+= word+"-"
		url += "lyrics"
	print(url)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	body = urlopen(req).read()
	soup = BeautifulSoup(body, 'html.parser')
	section = soup.find('div', {"class": "lyrics"}).find_all("p")
	text = ' '.join([item.text for item in section])
	#use regex to pattern match all things in brakcets
	match = re.findall(r'\[(.*?)\]', text)
	if match:
		cleaned = []
		for m in match:
			#cleaning titles
			new = m.split(' ', 1)[0]
			if new in KEYWORDS:
				cleaned.append(new)
		print(cleaned)

if __name__ == "__main__":
	main()