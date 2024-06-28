import requests
from bs4 import BeautifulSoup

# Get the Wikipedia page content

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = BeautifulSoup(res.text, 'lxml')

# Find the second image with the class 'mw-file-element'

computer = soup.select('.mw-file-element')[1]
image_url = 'https:' + computer['src']

# Download the image

img_data = requests.get(image_url).content
with open('Deep_Blue.jpg', 'wb') as handler:   # 'wb' --> write in binary 
      handler.write(img_data)

print("Image downloaded as 'Deep_Blue.jpg'")
