from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games = []
    feed = feedparser.parse(FEED_URL)
    for e in feed.entries:
        game = Game(e['title'], e["link"])
        games.append(game)
    return games
