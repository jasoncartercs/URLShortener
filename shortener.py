import random
import string
from db_connect import DBConnect
from url_shortner_model import UrlShortenerModel

class Shortener:
    def __init__(self, url):
        self.long_url = url

    def shorten_url(self):
        db_connect = DBConnect("url.db")

        if not db_connect.is_long_url_in_database(self.long_url):
            '''generate a unique token for the url
               if we find a unique token that is 6 characters we can stop
               otherwise increase the length of the characters by 1 until we find a unique token'''
            for index in range(6, 11):
                short_url = self.__generate_token(index)

                if not db_connect.is_short_url_in_database(short_url):
                    url_shortener_model = UrlShortenerModel(0, self.long_url, short_url)
                    db_connect.insert_url(url_shortener_model)
                    return "https://r.com/" + short_url
        else:
            url_shortener_model = db_connect.get_shortened_url(self.long_url)
            return "https://r.com/" + url_shortener_model.short_url

    # This function generates random string of 'length' length
    def __generate_token(self, length):
        random_string = ''.join(random.choice(
            string.ascii_letters + string.digits) for x in range(length))
        return random_string

