import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
# print(htmlContent)		# printing the code

htmlText = r.text
# print(htmlText)

soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify)


for i in soup.find_all("code"):
    print(i.text)
