from bs4 import BeautifulSoup as bs
import warnings
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


warnings.filterwarnings("ignore", module='bs4')
# To show the real simulation of mimicing google search engine
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def searchWithSelenium(query):
    print("------------------SearchwithSelinium Started------------------------")
    links = []
    title = []
    values = []
    # Specify number of pages on google search, each page contains 10 links
    n_pages = 6
    wd = webdriver.Chrome(ChromeDriverManager().install(),
                          options=chrome_options)

    for page in range(1, n_pages):
        url = "http://www.google.com/search?q=" + \
            query + "&start=" + str((page - 1) * 10)
        wd.get(url)

        soup = bs(wd.page_source, 'html.parser')

        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            links.append(h.a.get('href'))
            title.append(h.h3.get_text())
    wd.quit()
    print("-------------------Scrapped Items---------------------------")
    print(links)
    print("-------------------Scrapped Items Ended---------------------")

    for i in range(len(links)):
        values.append({
            "url": links[i],
            "title": title[i],
        })
        print(values)
    # Returns all  list of links and title after google search
    return values
