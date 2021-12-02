from urllib.request import urlopen
from urllib.parse import unquote
import time
import concurrent.futures
import os
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.request import Request, urlopen
from urllib.parse import unquote


def writeLinks():
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    if os.path.isfile("res.txt"):
        return
    res = open('res.txt', 'w', encoding='utf8')

    for i in tqdm(range(100)):
        html = urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')

        for l in links:
            href = l.get('href')
            if href and href.startswith('http') and 'wiki' not in href:
                print(href, file=res)


def checkLink(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=0.5)
        resp.close()
    except Exception as e:
        pass


def findOldLink(workersCount=1):
    links = open('res.txt', encoding='utf8').read().split('\n')
    log = open("log.txt", "w")
    beginTime = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=workersCount) as executor:
        futures = []
        for url in links:
            futures.append(executor.submit(checkLink, url))

    log.write(f"threads: {workersCount}\ntime: {((time.time() - beginTime) * 1000).__round__()}ms")

    log.close()


writeLinks()
findOldLink()