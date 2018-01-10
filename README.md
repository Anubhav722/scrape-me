# scrape-me

### Passing arguments in scrapy

To scrape a particular category in scrapy pass in arguments like so:
scrapy crawl books -a category="http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"

(which is the link of the category that we wish to scrape)

### Storing data in a csv file

To store data in a csv type in:
scrapy crawl books -a category="http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html" -o items.csv

But ultimately the file will be saved as foobar.csv since in books.py we have created a close function.
