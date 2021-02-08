from bs4 import BeautifulSoup
import csv
import datetime as dt
import json
import os
import random
import re
import requests
from urllib.parse import urlparse, urlencode, quote

from linkleads.terms import terms


# for reference. JSON type for SearchEngine.results[]
result = {
    "link": None,
    "site": None,
    "engine": None,
    "term": None
}

class SearchEngine:
    outfile = ""
    date = None
    url = None
    _LIMIT=1000
    results = []
    terms = terms
    fb_q = '"Page created - {} {}, {}"'
    headers = ['link', 'site', 'engine','term']


    def __init__(self, outfile=None, date=None):
        self.date = date if date is not None else dt.datetime.today()
        assert isinstance(self.date, dt.datetime)
        if outfile == None:
            self.outfile = f'outfile{self.date.strftime("%Y%m%d_%H-%M-%S")}.csv'
            self.writeToFile(mode="w", data=[{k: v for k, v in zip(self.headers, self.headers)}])
        else:
            self.outfile = outfile 




        # Some agents to use randomly. Mobile triggers different pagination and requires javascript execution 
        # "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                    #    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
        self.agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"]
 



    def getSearchResults(self):
        for term in self.terms:
            self.getFbResults(term)
            self.getBbbResults(term)
            self.getWixResults(term)

    def getFbResults(self, query):
        raise NotImplementedError("SearchEngine is a virtual class. Instantiate a specific search engine")

    def getBbbResults(self, query):
        raise NotImplementedError("SearchEngine is a virtual class. Instantiate a specific search engine")

    def getWixResults(self, query):
        raise NotImplementedError("SearchEngine is a virtual class. Instantiate a specific search engine")


    def replaceSpaces(self, s, ch='+'):
        query = re.sub(r"\s+", ch, s)
        return query

    def setLimit(self, n):
        self._LIMIT = n

    def writeToFile(self, mode="a", f=None, data=None):
        f = self.outfile if f is None else f
        data = self.results if data is None else data
        with open(self.outfile, mode, newline='') as file:
            csv_file = csv.writer(file)
            for item in data:
                csv_file.writerow([item['link'], item['site'], item['engine'], item['term']])


class Google(SearchEngine):
    def __init__(self, outfile=None, date=None):
        super().__init__(outfile, date)
        self.url = 'https://www.google.com/search?'
        self.fb_q = self.fb_q.format(self.date.strftime("%B"),
                                     str(self.date.day),
                                     self.date.strftime("%Y"))
        print()

    
    def getFbResults(self, term):
        # term=self.replaceSpaces(term)
        # self.fb_q = self.replaceSpaces(self.fb_q)
        query = f'{self.fb_q} inurl:facebook.com intitle:{term}'

        nglinks = 0
        nlinks = 0
        previousurl = ""
        # resp = requests.get(URL, headers=headers)
        while nlinks < self._LIMIT:
            # url = self.url.format(query=query, nglinks=0)
            # url = self.url +  urlencode({"q": query, "oq": query, "ie": "utf-8"})
            url = self.url + query
            # agent = self.agents[random.randrange(len(self.agents))]
            agent = self.agents[0]
            headers = {"user-agent" : agent}
            if url == previousurl:
                break
            previousurl = url
            try:
                html = requests.get(url, headers=headers)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    links = soup.find_all('a')
                    for link in links:
                        href = link.get('href')
                        try:
                            m = re.search(r"(?P<url>https?://[^\s]+)", href)
                            n = m.group('url')
                            rul = n.split('&')[0]
                            domain = urlparse(rul)
                            if re.search('google.com', domain.netloc):
                                continue
                            else:
                                self.results.append({
                                    "link": rul,
                                    "site": 'facebook',
                                    "engine": "google",
                                    "term": term,
                                    "date": self.date.strftime("%Y/%m/%d")
                                })
                                nlinks += 1
                        except AttributeError as ex:
                            if link.text.startswith('Next') & href.startswith('/search?'):
                                x = re.search("&start=([0-9]+)", href)
                                if x and x.group(1):
                                    nglinks = x.group(1)
                                    print(x.group(1))
                                    break
                            continue
                        except Exception as ex:
                            print(str(type(ex)), ex)
                            raise ex
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        self.results = []

    def getBbbResults(self, query):
        print(str(__class__) + ' notimplemnted')

    def getWixResults(self, query):
        print('notimplemnted')

class Bing(SearchEngine):
    def __init__(self, outfile=None, date=None):
        super().__init__(outfile, date)
        self.url = 'https://www.bing.com/search?'
        self.fb_q = self.fb_q.format(self.date.strftime("%B"),
                                     str(self.date.day),
                                     self.date.strftime("%Y"))
    
    def getFbResults(self, term):
        query = f'{self.fb_q} site: facebook.com intitle: {term}'
        # query = '"Page created - February 7, 2021" site: facebook.com intitle: Home Improvement'
        # url = self.url + urlencode({"q": query})
        # url = 'https://www.bing.com/search?q=%22Page%20created%20-%20February%205%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20Home%20Improvement'
        # url = 'https://www.bing.com/search?q=%22Page%20created%20-%20February%205%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20Home%20Improvement&pq=%22page%20created%20-%20february%207%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20home%20improvement'
        url = 'https://www.bing.com/search?q=%22Page%20created%20-%20February%205%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20Home%20Improvement&pq=%22page%20created%20-%20february%207%2C%202021%22%20site%3A%20facebook.com%20intitle%3A%20home%20improvement&qs=n&form=QBRE&sp=-1'
        
        # url = self.url + query
        # url = "https://www.bing.com/search?q=%22%22Page%20created%20-%20February%207%22%20site:facebook.com%20intitle:%22Home%20Improvement%22"
        # xxx = 'https://www.bing.com/search?q=%22Page%20created%20-%20February%207%2C%202021%22%20site%3Afacebook.com%20intitle%3AHome%20Improvement'
        # yyy = 'https://www.bing.com/search?q=%22Page%20created%20-%20February%207%2C%202021%22%20site%3Afacebook.com%20intitle%3AHome%20Improvement'
        # zzz = 'https://www.bing.com/search?q=%22Page+created+-+February+7%2C+2021%22+site%3A+facebook.com+intitle%3A+Home+Improvement'
        
        nglinks = 0
        nlinks = 0
        previousurl = ""
        # resp = requests.get(URL, headers=headers)
        while nlinks < self._LIMIT:
            # url = self.url + query
            # url = self.url +  urlencode({"q": query})
            # url = self.url +  url
            agent = self.agents[random.randrange(len(self.agents))]
            headers = {"user-agent" : agent}
            print(agent)
            if url == previousurl:
                break
            previousurl = url
            try:
                html = requests.get(url, headers=headers)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    links = soup.find_all('a')
                    # print(html.text)
                    f = open("tmp.html", "w", encoding='utf-16')
                    f.write(html.text)
                    f.close()
                    
                    for link in links:
                        href = link.get('href')
                        if not href:
                            continue
                        try:
                            m = re.search(r"(?P<url>https?://[^\s]+)", href)
                            n = m.group('url')
                            rul = n.split('&')[0]
                            domain = urlparse(rul)
                            if re.search('bing.com|microsoft.com', domain.netloc):
                                continue
                            else:
                                self.results.append({
                                    "link": rul,
                                    "site": 'facebook',
                                    "engine": "bing",
                                    "term": term,
                                    "date": self.date.strftime("%Y/%m/%d")
                                })
                                nlinks += 1
                        except AttributeError as ex:
                            if link.get('title') and  link.get('title').startswith('Next') & href.startswith('/search?'):
                                url = f'{self.url}{href}'
                                break
                            continue
                        except Exception as ex:
                            print(str(type(ex)), ex)
                            continue
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        self.results = []

    def getBbbResults(self, query):
        print('notimplemnted')

    def getWixResults(self, query):
        print('notimplemnted')

class Yahoo(SearchEngine):
    def __init__(self, outfile):
        super().__init__(outfile)
        self.url = 'https://www.yahoo.com/search?q={query}&start={nglinks}'
    
    def getFbResults(self, query):
        print('notimplemnted')

    def getBbbResults(self, query):
        print('notimplemnted')

    def getWixResults(self, query):
        print('notimplemnted')


if __name__ == '__main__':
    # g = Google()
    # g.getSearchResults()
    d = dt.datetime(2021, 2, 5)
    b = Bing(date=d)
    b.getSearchResults()



