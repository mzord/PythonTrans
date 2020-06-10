import requests
import urllib.parse
import json


class Translator:

    def __init__(self, lang, langTrans="en"):

        self.__lang = lang
        self.__langTrans = langTrans

        self.url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        self.headers = {
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': "04442b8be9mshec7e90578c5cd85p12ab36jsnb63cde929a08",
            'accept-encoding': "application/gzip",
            'content-type': "application/x-www-form-urlencoded"
            }

    def getLang(self):
        return self.__lang

    def translate(self, word):

        if(word[0] == "!"):
            newLang = word[1:3]
            try:
                self.__lang = newLang
                return "Changed language to {lang}".format(lang=newLang)
            except:
                return "Could not change language"
        else:
            query = urllib.parse.quote(word)
            payload = "source=" + self.__lang + "&q=" + query + "&target=pt"

            response = requests.request("POST", self.url, data=payload, headers=self.headers)
            return json.loads(response.text)["data"]["translations"][0]["translatedText"]

    

