import requests
import re
from flask import url_for
from bs4 import BeautifulSoup

base_url = "https://monoschinos2.com/"
search_url = "buscar/"
episodes_url = "anime/"
watch_url = "ver/"

def search_anime(anime_name):
    url = f"{base_url}{search_url}"
    payload = {'q': anime_name}
    r = requests.get(url, params=payload)  

    soup = BeautifulSoup(r.content, features="lxml")
    result = soup.select(".col-md-4.col-lg-2.col-6")
    animes = []
    for anime in result:
        a = {}
        a['title'] = anime.select_one(".seristitles").text
        a['img'] = anime.select_one(".animemainimg")['src']
        a['href'] = anime.a['href'].replace(base_url+episodes_url, "").replace("-sub-espanol", "")
        animes.append(a)
    return animes


def get_episodes(anime_name):
    url = f"{base_url}{episodes_url}"
    response = requests.request("GET", f'{url}{anime_name}')
    soup = BeautifulSoup(response.text, features="html.parser")
    episodes = soup.select('.col-item')

    return len(episodes)

def get_episode_info(anime_name, episode_number):
    url = f"{base_url}{watch_url}"
    r = requests.get(f"{url}{anime_name}-{episode_number}")
    soup = BeautifulSoup(r.content, features="lxml")
    servers = get_servers(soup=soup)
    title = soup.select_one('h1.heromain_h1').text
    anime_info = {
        'title': title,
        'servers': servers 
    }
    return anime_info
def get_servers(soup):
    import base64

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


def get_last_episodes():
    url = base_url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    episodes = soup.select('.col.col-md-6.col-lg-2.col-6')

    result = []
    for episode in episodes:
        e = {}
        href = episode.a['href']
        anime_name = episode.select_one('.animetitles').text
        cover_src = episode.select_one('.animeimgdiv').img['data-src']
        an, en = href.replace(base_url+watch_url, '').rsplit('-', 1)
        e['href'] = f"{url_for('anime.watch', anime_name=an, episode_number=en)}"
        e['cover_src'] = cover_src
        e['anime_title'] = anime_name
        result.append(e)
    return result