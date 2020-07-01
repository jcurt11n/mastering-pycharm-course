from xml.etree import ElementTree
from collections import namedtuple
import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def download_info():
    url = 'https://talkpython.fm/episodes/rss'
    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')
    # print(len(items))
    episode_count = len(items)

    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        print("int show_id ", int(episode.show_id))
        print("no type case show_id ", episode.show_id)
        show_id = int(episode.show_id)
        # episode_data[episode.show_id] = episode
        episode_data[show_id] = episode
        # print("episode dict ", episode_data[show_id])

    return episode_count


# def get_episode(show_id: int) -> Optional[Episode]:
# def get_episode(show_id: int) -> Episode:
# def get_episode(show_id):
def get_episode(show_id: int) -> Episode:
    print("*" * 45)
    # print("IN Service ", episode_data.get(show_id))
    # print("IN Service ", episode_data[int(show_id)])
    return episode_data.get(show_id)
    # return episode_data[int(show_id)]
