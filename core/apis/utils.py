import re
import cloudscraper
from flask import url_for
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper() 
base_url = 'https://jkanime.net/'
anime_url = '{anime_name}/'
buscar_url = 'buscar/{anime_name}/{page_number}/'
watch_url = '{anime_name}/{episode_number}/'


def search_anime(data, filters):

  url = base_url+buscar_url.format(**data)
  r = scraper.get(url, params=filters)
  soup = BeautifulSoup(r.content, features='lxml')
  results = soup.select('.anime__item')
  animes = []
  for result in results:
    a = {}
    a['title'] = result.select_one(".title").text
    a['img'] = result.a.div['data-setbg']
    an, nouse = result.a['href'].replace(base_url, "").split('/')
    a['href'] = f"{url_for('anime.episodes', anime_name=an)}"
    animes.append(a)

  return animes
  
def get_episodes(anime_name):
  url = base_url+anime_url.format(anime_name=anime_name)
  r = scraper.get(url)
  soup = BeautifulSoup(r.content, features='lxml')
  details = soup.select('div.col-lg-6.col-md-6 ul li')
  result = {}
  for detail in details:
    info = detail.text.split(':')
    result[info[0]] = " ".join(info[1].split())
  if result['Episodios'] == "Desconocido":
    episodes = soup.select_one(".anime__pagination :last-child")
    result['Episodios'] = int(episodes.text.split('-')[1])
  else:
    result['Episodios'] = int(result['Episodios'])
  return result
    

def get_episode_info(anime_name, episode_number):

  url = f"{base_url}{watch_url.format(anime_name=anime_name, episode_number=episode_number)}"
  r = scraper.get(url)
  soup = BeautifulSoup(r.content, features='lxml')
  title = soup.select_one('.breadcrumb__links').h1.text
  servers = get_servers(soup=soup)
  anime_info = {
    'title': title,
    'servers': servers
  }
  return anime_info

def get_servers(soup):
  
  scripts = soup.select('script')
  result = []
  for script in scripts:
    script = script.text
    if 'var video = [];' in script:
      servers = re.findall('src=".([:?=/&;a-zA-Z0-9%\._-]*)', script)
      for i, server in enumerate(servers, start=1):
        s = {}
        btn = soup.select_one(f'a#btn-show-{i}')
        server_name = btn.text
        s['name'] = server_name
        s['link'] = base_url+server
        if server_name == 'Nozomi':
          continue
        elif server_name == 'Mega':
          s['link'] = 'h'+server
        result.append(s)
  return result

def get_last_episodes():
  url = base_url
  r = scraper.get(url)
  soup = BeautifulSoup(r.content, features='lxml')

  results = soup.select('.bloqq')

  episodes = []
  for result in results:
    e = {}
    href = result['href'].replace(base_url, "")
    anime_name = result.select_one('.anime__sidebar__comment__item__text h5').text
    cover_src = result.select_one('.anime__sidebar__comment__item__pic.listadohome img')['src']
    an, en, nouse = href.split('/')
    e['href'] = f"{url_for('anime.watch', anime_name=an, episode_number=en)}"
    e['cover_src'] = cover_src
    e['anime_title'] = anime_name
    episodes.append(e)

  return episodes