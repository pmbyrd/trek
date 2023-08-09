from datetime import datetime
from random import uniform
from bs4 import BeautifulSoup as Soup
from bs4 import SoupStrainer, Tag
import requests
import urllib.request
from flask import session, abort



# ********************************!SECTION: HELPER FUNCTIONS********************************

def replace_space(string):
    """Replace spaces with underscores"""
    if " " in string:
        string = string.replace(" ", "_")
    else:
        string = string
    

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            abort(401)  # Unauthorized
        else:
            return function()
    return wrapper

class MemoryAlphaScraper:
    def __init__(self, name, base_url="https://memory-alpha.fandom.com/wiki"):
        self.base_url = base_url
        self.name = name
        
    def soup(self):
        url = f"{self.base_url}/{self.name}"
        html_content = urllib.request.urlopen(url)
        soup = Soup(html_content, 'html.parser')
        # print(url)
        return soup
    
    # NOTE at the moment this is good enough
    def get_images(self):
        soup = self.soup()
        images = []
        for i in soup.find_all("img"):
            if i.has_attr('data-src'):
                images.append(i['data-src'])
        return images
    
    def get_images_aside(self):
        try: 
            url = self.soup()
            aside = url.find("aside")
            image_class = url.find("div", {"class": "image"})        
            # print(aside)
            if aside:
                print("aside found")
                try:
                    images = aside.findAll("img")
                    if images:
                        images = [{image.get("src"), image.get("alt")} for image in images]
                        return images
                    else:
                        print("No image found in the 'aside' section.")
                except (TypeError, AttributeError, NameError) as e:
                    print(e)
            elif image_class:
                    if image_class:
                        images = [{image.get("src"), image.get("alt")} for image in image_class]
                    else:
                        print("No image found in the 'image' section.")
        except AttributeError as e:
            print(e)
    
    def get_formatted_info(self):
        soup = self.soup()
        div = soup.find("div", class_="mw-parser-output")
        spans = div.find_all("span", class_="mw-headline")
        all_paragraphs = div.find_all("p")
        # Combine `spans` and `all_paragraphs` using zip
        paired_elements = zip(spans, all_paragraphs)

        for span, p in paired_elements:
            print(span.get_text())
            print(p.get_text())
            return paired_elements
        
    def get_summary(self):
        """Gets the summary of the show"""
        soup = self.soup()
        div = soup.find("div", {"class": "mw-parser-output"})
        content_nodes = div.find_all(["h2", "h3", "p", "b", "ul", "span"])
        # Create a list to store tuples of paired elements (headline, content)
        spans = div.find_all("span", class_="mw-headline")
        headlines = div.find_all(["h2", "h3", "h4"])
        content_nodes = div.find_all(["p", "b", "ul"])
          
        paired_elements = []
        current_headline = None
    
        for node in content_nodes:
            if node.name in ["h2", "h3", "h4"]:
                # If the node is a headline, update the current_headline
                current_headline = node.get_text()    
            else:
                # If the node is not a headline, it's content associated with the current_headline
                paired_elements.append((current_headline, node.get_text()))
                
        for span in spans:
            if span.name in ["span"]:
                # If the node is a headline, update the current_headline
                current_headline = span.get_text()
    
        # Loop through the paired elements and print the information
        for headline, content in paired_elements:
            print(headline)
            print(content)
            print(spans)
            return paired_elements
    

        
        
    
    def get_paragraphs(self):
        content = []
        soup = self.soup()
        # get the content by looking for the all items in the div with the id of content
        content_raw = soup.find("div", id="content")
        all_paragraphs = content_raw.find_all("p")
        for p in all_paragraphs:
            content = [p.get_text().replace("\n", " ") for p in all_paragraphs]

        return content
    
 
# class MemoryAlphaScraper:
#     def __init__(self, name, base_url="https://memory-alpha.fandom.com/wiki"):
#         self.base_url = base_url
#         self.name = name

#     def soup(self):
#         url = f"{self.base_url}/{self.name}"
#         html_content = urllib.request.urlopen(url)
#         soup = Soup(html_content, 'html.parser')
#         # print(url)
#         return soup
    
#     def __repr__(self):
#         return f"<MemoryAlphaScraper {self.name}>"
    
#     def get_content(self):
#         url = self.soup()
#         result = url.find("div", {"class": "mw-parser-output"})
#         # 
#         try:
#             content = result.findAll("p")
#             if content:
#                 content_raw = [p.get_text() for p in content]
#                 content = [p.get_text().replace("\n", " ") for p in content]
#                 print(content)
#                 return content
#             else:
#                 print("No content found in the 'div' section.")
#                 return None    
#                 # print(content)
#                 # NOTE in the value being returned the links to other pages are in escaped characters
#                 # !those links to be stored some where and then user can click them go to the page of that object
        
#         except AttributeError as e:
#             print(e)
            
#     def get_links(self):
#         url = self.soup()
#         # The href needs to contain /wiki/<name> and the title needs to be the name

#     def get_all_headlines(self):
#         url = self.soup()
#         result = url.find("div", {"class": "mw-parser-output"})
#         headlines = result.findAll(["h2", "h3"])
#         headlines = [headline.get_text() for headline in headlines]
#         return headlines
    
#     def get_all_titles(self):
#         url = self.soup()
#         result = url.find("div", {"class": "mw-parser-output"})
#         titles = result.findAll("title")
#         print(titles)

# class MemomryAlphaShowScraper(MemoryAlphaScraper):
#     """A child class of MemoryAlphaScraper that scrapes the information for a show"""    
#     def get_summary(self):
#         """Gets the summary of the show"""
        
# dukat = MemoryAlphaScraper("Dukat") #!This is the object instance
# dukat.get_all_titles()
# # dukat.soup()
# # dukat.get_images()
# # dukat.get_content()
# # picard = MemoryAlphaScraper("Jean-Luc_Picard")
# # picard.get_content()

#     # def scrape_image(self):
        
#     #     url = self.soup
#     #     aside = self.soup.find("aside")
#     #     if aside:
#     #         print("aside found")
#     #         try:
#     #             images = aside.findAll("img")
#     #             if images:
#     #                 first_image = images[0]
#     #                 image_src = first_image.get("src")
#     #                 image_alt = first_image.get("alt")
#     #                 print("First Image URL:", image_src)
#     #                 print("First Image Alt Text:", image_alt)
#     #                 first_image = {
#     #                     image_alt,
#     #                     image_src
#     #                 }
#     #                 return first_image
#     #             else:
#     #                 print("No image found in the 'aside' section.")
#     #         except AttributeError as e:
#     #             print(e)
                
#     # def get_content(self, name):
#     #     print("get_content")
        

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





# def get_random_datetime(year_gap=5):
#     """Get a random datetime within the last few years."""

#     now = datetime.now()
#     then = now.replace(year=now.year - year_gap)
#     random_timestamp = uniform(then.timestamp(), now.timestamp())

#     return datetime.fromtimestamp(random_timestamp)

# def test_hello(name):
#     name = input('What is your name? ')
#     yield f'Hello {name}!'
    