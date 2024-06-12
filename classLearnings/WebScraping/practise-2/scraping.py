import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

page_num = 12
# print(base_url.format(page_num))

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')

products = soup.select('.product_pod')


example = products[0]

# Method - 1 to check weather the class is present or not
# 'star-rating Three' in str(example)   # make to print it, returns the boolean value

# Method - 2 to check weather the class is present or not
example.select('.star-rating.Three')

# selects the achor tag from the product pod class example is getting a first product item and where title is selecting a title of a item
title = example.select('a')[1]
# print(title['title'])    # give the title of a book


########### ---> Loop to move,all the pages and get the title of a book of two star rating  
two_star_titles = []

for n in range(1,51):
      scrape_url = base_url.format(n)
      res = requests.get(scrape_url)
      
      soup = bs4.BeautifulSoup(res.text,'lxml')
      books = soup.select(".product_pod")
      
      for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                  book_title = book.select('a')[1]['title']
                  two_star_titles.append(book_title)
                  # print(f"Found a two-star book: {book_title}") 1


print(two_star_titles)