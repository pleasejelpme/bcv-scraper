from bs4 import BeautifulSoup
import requests
import urllib3

# Attempting to scrap the website causes an SSL error because a bad implementation of SSL certification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://bcv.org.ve'

try:
    response = requests.get(url, verify=False)
except Exception as err:
    with open('error.txt', 'w') as file:
        file.write(str(err))


content = response.text

soup = BeautifulSoup(content, 'lxml')
dolar = soup.find(id='dolar').get_text(strip=True, separator=' ')
euro = soup.find(id='euro').get_text(strip=True, separator=' ')


with open('dolarbcv.txt', 'w') as file:
    file.write(f'{dolar}   |    {euro}')
    file.close()
