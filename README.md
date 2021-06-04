# WikiScraper
This is a tool used to scrape paragraphs from Wikipedia pages and beautify them by removing the clutter like annotations and references

## How it works
It uses Requests and BeautifulSoup libraries to get and parse HTML pages. 

Headings and paragraphs are then extracted from HTML document. Paragraphs are then cleaned(removing citations).

Headings and their corresponding paragraphs are then stored in a dictionary whose key-value pair looks like this: {heading:paragraph}