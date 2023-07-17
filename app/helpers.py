from datetime import datetime
from random import uniform
from bs4 import BeautifulSoup as Soup
from bs4 import SoupStrainer, Tag
import requests
import urllib.request


def replace_space(string):
    """Replace spaces with underscores"""
    if " " in string:
        string = string.replace(" ", "_")
    else:
        string = string
    
    return string
    

class MemoryAlphaScraper:
    def __init__(self, name, base_url="https://memory-alpha.fandom.com/wiki"):
        self.base_url = base_url
        self.name = name

    def soup(self):
        url = f"{self.base_url}/{self.name}"
        html_content = urllib.request.urlopen(url)
        soup = Soup(html_content, 'html.parser')
        print(url)
        return soup
    
    def __repr__(self):
        return f"<MemoryAlphaScraper {self.name}>"
    
    def get_images(self):
        try: 
            url = self.soup()
            aside = url.find("aside")
            print(aside)
            if aside:
                print("aside found")
                try:
                    images = aside.findAll("img")
                    if images:
                        images = [{image.get("src"), image.get("alt")} for image in images]
                        print(images)
                    else:
                        print("No image found in the 'aside' section.")
                except AttributeError as e:
                    print(e)
        except AttributeError as e:
            print(e)
    
    def get_content(self):
        url = self.soup()
        result = url.find("div", {"class": "mw-parser-output"})
        # 
        try:
            content = result.findAll("p")
            if content:
                content_raw = [p.get_text() for p in content]
                content = [p.get_text().replace("\n", " ") for p in content]
                print(content)
                # NOTE in the value being returned the links to other pages are in escaped characters
                # !those links to be stored some where and then user can click them go to the page of that object
            else:
                print("No content found in the 'div' section.")
        
        except AttributeError as e:
            print(e)
        
        

# dukat = MemoryAlphaScraper("Dukat")
# dukat.soup()
# dukat.get_images()
# dukat.get_content()
# picard = MemoryAlphaScraper("Jean-Luc_Picard")
# picard.get_content()

    # def scrape_image(self):
        
    #     url = self.soup
    #     aside = self.soup.find("aside")
    #     if aside:
    #         print("aside found")
    #         try:
    #             images = aside.findAll("img")
    #             if images:
    #                 first_image = images[0]
    #                 image_src = first_image.get("src")
    #                 image_alt = first_image.get("alt")
    #                 print("First Image URL:", image_src)
    #                 print("First Image Alt Text:", image_alt)
    #                 first_image = {
    #                     image_alt,
    #                     image_src
    #                 }
    #                 return first_image
    #             else:
    #                 print("No image found in the 'aside' section.")
    #         except AttributeError as e:
    #             print(e)
                
    # def get_content(self, name):
    #     print("get_content")
        

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





def get_random_datetime(year_gap=5):
    """Get a random datetime within the last few years."""

    now = datetime.now()
    then = now.replace(year=now.year - year_gap)
    random_timestamp = uniform(then.timestamp(), now.timestamp())

    return datetime.fromtimestamp(random_timestamp)

def test_hello(name):
    name = input('What is your name? ')
    yield f'Hello {name}!'
    