#LOOK OVER THIS!!!
import hashlib

class URLShortener:
    def __init__(self):
        self.short_to_url_map = dict()
        self.m = hashlib.sha256
        self.prefix = 'http://urlsho.rt/'

    def shorten(self, url):
        sha_signature = self.m(url.encode()).hexdigest()
        short_hash = sha_signature[:6]
        self.short_to_url_map[short_hash] = url
        return self.prefix + short_hash

    def restore(self, short):
        short_hash = short.replace(self.prefix, "")
        return self.short_to_url_map[short_hash]

url = 'https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3366/'
shortener = URLShortener()

assert shortener.restore(shortener.shorten(url)) == url