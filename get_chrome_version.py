# Answer to stackoverflow question: 
# https://stackoverflow.com/questions/58840609/is-there-any-way-to-get-the-latest-chrome-version/58840659#58840659
# https://stackoverflow.com/questions/58743524/how-to-programmatically-identify-latest-version-of-chrome/58840268#58840268

import requests
from bs4 import BeautifulSoup as bs

def get_chrome_version():
    url = "https://www.whatismybrowser.com/guides/the-latest-version/chrome"
    response = requests.request("GET", url)

    soup = bs(response.text, 'html.parser')
    rows = soup.select('td strong')
    version = {}
    version['windows'] = rows[0].parent.next_sibling.next_sibling.text
    version['macos'] = rows[1].parent.next_sibling.next_sibling.text
    version['linux'] = rows[2].parent.next_sibling.next_sibling.text
    version['android'] = rows[3].parent.next_sibling.next_sibling.text
    version['ios'] = rows[4].parent.next_sibling.next_sibling.text
    return version

def get_chrome_latest_release():
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.request("GET", url)
    return response.text

print(get_chrome_latest_release())
print(get_chrome_version())
