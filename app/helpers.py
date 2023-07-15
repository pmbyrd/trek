from datetime import datetime
from random import uniform
from bs4 import BeautifulSoup as Soup
from bs4 import SoupStrainer, Tag
import requests
import urllib.request



class MemoryAlphaScraper:
    def __init__(self, base_url="https://memory-alpha.fandom.com/wiki"):
        self.base_url = base_url

    def scrape_info(self, name):
        url = f"{self.base_url}/{name}"
        html_content = urllib.request.urlopen(url)
        soup = Soup(html_content, 'html.parser')
        
        aside = soup.find("aside")
        if aside:
            print("aside found")
            try:
                images = aside.findAll("img")
                if images:
                    first_image = images[0]
                    image_src = first_image.get("src")
                    image_alt = first_image.get("alt")
                    print("First Image URL:", image_src)
                    print("First Image Alt Text:", image_alt)
                    first_image = {
                        image_alt,
                        image_src
                    }
                    return first_image
                else:
                    print("No image found in the 'aside' section.")
            except AttributeError as e:
                print(e)
            
    # def ma_article(self, url, content_format="xml", content_nodes=("h2", "h3", "p", "b", "ul"), browse=False):
    #     # Make a GET request to the URL
    #     response = requests.get(url)
    #     response.raise_for_status()  # Raise an exception for unsuccessful requests

    #     # Parse the HTML content using BeautifulSoup
    #     soup = BeautifulSoup(response.content, content_format)

    #     # Find the desired content nodes
    #     nodes = soup.find_all(content_nodes)

    #     # Print or process the extracted content nodes
    #     for node in nodes:
    #         print(node.get_text())  # Example: printing the text content of each node

    #     # Optionally, browse the extracted content
    #     if browse:
    #         # Perform some actions to browse the extracted content
    #         pass


class MemoryAlphaAnimalScrapper:
    def __init__(self, name):
        self.name = name
        self.scraper = MemoryAlphaScraper()

    def get_info(self):
        return self.scraper.scrape_info(self.name)
    
seagull = MemoryAlphaAnimalScrapper("Seagull")
print(seagull.get_info())




def get_random_datetime(year_gap=5):
    """Get a random datetime within the last few years."""

    now = datetime.now()
    then = now.replace(year=now.year - year_gap)
    random_timestamp = uniform(then.timestamp(), now.timestamp())

    return datetime.fromtimestamp(random_timestamp)

def test_hello(name):
    name = input('What is your name? ')
    yield f'Hello {name}!'
    