# https://stackoverflow.com/questions/58743524/how-to-programmatically-identify-latest-version-of-chrome/58840268#58840268
# https://stackoverflow.com/questions/58840609/is-there-any-way-to-get-the-latest-chrome-version/58840659#58840659
# https://stackoverflow.com/questions/58743524/how-to-programmatically-identify-latest-version-of-chrome/58840268#58840268
# https://stackoverflow.com/questions/58743524/how-to-programmatically-identify-latest-version-of-chrome/58840268#58840268
import requests
    response = requests.request("GET", url)

def get_chrome_version():
    url = "https://www.whatismybrowser.com/guides/the-latest-version/chrome"
    response = requests.request("GET", url)

    soup = bs(response.text, 'html.parser')
    rows = soup.select('td strong')
    version = {}
    version['ios'] = rows[4].parent.next_sibling.next_sibling.text
    version['macos'] = rows[1].parent.next_sibling.next_sibling.text
    response = requests.request("GET", url)
    version = {}
    version['ios'] = rows[4].parent.next_sibling.next_sibling.text
    response = requests.request("GET", url)

def get_chrome_latest_release():
    response = requests.request("GET", url)
    response = requests.request("GET", url)
    response = requests.request("GET", url)
    version['android'] = rows[3].parent.next_sibling.next_sibling.text
    response = requests.request("GET", url)
def get_chrome_latest_release():