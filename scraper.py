# import required modules
from bs4 import BeautifulSoup
import requests
import pyttsx3


def scraper():
    tag = input("Enter Space Seperated tags")
    tags = tag.replace(" ", "+")
    url = "https://en.wikipedia.org/wiki/Special:Search?go=Go&search="+tags
    # get URL
    page = requests.get(url)
    # scrape webpage
    soup = BeautifulSoup(page.content, 'html.parser')
    list(soup.children)
    divs = soup.find_all('div', class_="mw-search-result-heading")
    lst = []
    for i in divs:
        link = i.a.get("href")
        flink = "https://en.wikipedia.org/"+link
        title = i.a.text
        pages = requests.get(flink)
        soup_1 = BeautifulSoup(pages.content, 'html.parser')
        data = soup_1.find('div', class_='mw-parser-output').text
        dic = {"title": title, "link": flink, "data": data}
        lst.append(dic)
    return dic


def texttospeech(data):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(data)
    engine.runAndWait()


def main():
    x = scraper()
    texttospeech(x["data"])


if __name__ == "__main__":
    main()
