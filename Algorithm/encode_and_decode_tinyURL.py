import string
import random
import math
full_tiny = {}
tiny_full = {}
letters = string.ascii_letters + string.digits

def encode(longUrl):
    # Ecodes a URL to a Shorten 

    def short_addr():
        ans = ''
        tmp = ''
        for i in range(6):
            tmp  = letters[random.randint(0, 10000) % 62]
            ans += tmp
        return ans

        if longUrl in full_tiny:
            return 'http://tinyurl.com/' + full_tiny[longUrl]
        else:
            suffix = short_addr()
            full_tiny[longUrl] = suffix
            tiny_full[suffix]  = longUrl
            return 'http://tinyurl.com' + suffix

    def decode(shortUrl):
        # Decodes a shortened URL to its original URL.
        
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None
