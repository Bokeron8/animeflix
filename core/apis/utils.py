import requests
import re
from bs4 import BeautifulSoup

base_url = "https://monoschinos2.com"

def search_anime(anime_name):
    url = f"{base_url}/buscar"
    payload = {'q': anime_name}
    r = requests.get(url, params=payload)  

    soup = BeautifulSoup(r.content, features="lxml")
    result = soup.select(".col-md-4.col-lg-2.col-6")
    animes = []
    for anime in result:
        a = {}
        a['title'] = anime.select_one(".seristitles").text
        a['img'] = anime.select_one(".animemainimg")['src']
        title_sano = re.sub(r'[^\w\s]', '', a['title'])
        a['href'] = f"{'-'.join(title_sano.split(' '))}"
        animes.append(a)
    return animes


def get_episodes(anime_name):
    url = f"{base_url}/anime/"
    response = requests.request("GET", f'{url}{anime_name}')
    soup = BeautifulSoup(response.text, features="html.parser")
    episodes = soup.select('.col-item')

    return len(episodes)


def get_servers(anime_name, episode_number):
    import base64
    url = f"{base_url}/ver/"
    r = requests.get(f"{url}{anime_name}-{episode_number}")
    soup = BeautifulSoup(r.content, features="lxml")
    soup = soup.select_one(".playother")
    servers = soup.select(".play-video")
    links = []
    for server in servers:
        l = {}
        link = base64.b64decode(server['data-player']).decode("utf-8")
        l['link'] = re.findall('url=([:/?=&;a-zA-Z0-9%\._-]*)', link)[0]
        l['name'] = server.text
        links.append(l)

    return links