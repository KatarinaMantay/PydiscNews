import feedparser
import re
from Config import RSS_URL

def getTweetInfo():
    feed = feedparser.parse(RSS_URL)
    recentTweet = feed.entries[0]

    tweetTitle = recentTweet.title
    tweetTitle = re.sub(r'http\S+', '', tweetTitle).strip()

    tweetLink = recentTweet.link

    return tweetTitle, tweetLink

