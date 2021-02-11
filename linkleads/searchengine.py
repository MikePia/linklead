from bs4 import BeautifulSoup
import csv
import datetime as dt
import json
import os
import random
import re
import requests
import time
from urllib.parse import urlparse, urlencode, unquote

from linkleads.agents import agents
from linkleads.terms import terms
from linkleads.terms import terms
import linkleads.searchterms as st


# for reference. JSON type for SearchEngine.results[]
result = {
    "link": None,
    "site": None,
    "engine": None,
    "term": None
}

class SearchEngine:
    outfile = ''
    date = None
    url = None
    _LIMIT=1000
    results = []
    terms = terms
    fb_q = None #'"Page created - {month} {day}, {year}"'
    bbb_q = None # '"Accredited Since:{month}/{day}/{year}" intitle: Construction inurl: bbb.org '
    headers = ['link', 'site', 'engine','term']
    config=True

    def __init__(self, outfile=None, date=None, config=True):
        self.config = config

        # set from searchterms module, default priority (lowest)
        if self.config:
            self._LIMIT = st.LIMIT
            self.forceoverwrite = st.forceoverwrite
            self.outfile = st.outfile
            self.date = st.searchday
            self.bingbbbtime = st.bingbbbtime
            self.yahoobbbtime = st.yahoobbbtime
            self.bingwixtime = st.bingwixtime
            self.yahoowixtime = st.yahoowixtime
            self.fb_q = st.fbsearch
            self.bbb_q = st.bbbsearch
            self.wix_q = st.wix_q
            self.runsearches = st.runsearches
            self.randomsleep = st.randomsleep

        # override date and outfile
        if date is not None:
            self.date = date
            self.fb_q, self.bbb_q, self.outfile, self.bingbbbtime, self.yahoobbbtime, self.bingwixtime, self.yahoowixtime = st.formatTerms(self.date)

        assert isinstance(self.date, dt.datetime)

        writeheader = True
        if self.forceoverwrite == False:
            if os.path.exists(self.outfile):
                with open(self.outfile, 'r', newline='', encoding='utf-16') as file:
                    x = file.readline()
                    if x and x.startswith(self.headers[0]):
                        writeheader = False
        if writeheader:
            self.writeToFile(mode="w", data=[{k: v for k, v in zip(self.headers, self.headers)}])
        self.agents = agents
                       
    def getSearchResults(self, searches=None):
        searches = searches if searches else self.runsearches

        for term in self.terms:
            if 'all' in searches or 'fb' in searches:
                self.getFbResults(term)
            if 'all' in searches or 'bbb' in searches:
                self.getBbbResults(term)
            if 'all' in searches or 'wix' in searches:
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
        with open(self.outfile, mode, newline='', encoding='utf-16') as file:
            csv_file = csv.writer(file)
            for item in data:
                try:
                    csv_file.writerow([item['link'], item['site'], item['engine'], item['term']])
                except:
                    print(f'failed to write link: {item["link"]}')
    
    def randomSleep(self):
        if self.randomsleep is not None:
            time.sleep(self.randomsleep[0] + random.random() * self.randomsleep[1])


class Google(SearchEngine):
    def __init__(self, outfile=None, date=None, config=True):
        super().__init__(outfile, date, config)
        self.url = 'https://www.google.com/search?'

    
    def getFbResults(self, term):
        '''
        fb: https://www.google.com/search?"Page created - January 01, 2021" inurl:facebook.com intitle:Home Improvement
        '''
        query = f'{self.fb_q} inurl:facebook.com intitle:{term}'
        url = self.url + urlencode({'q': query, 'oq': query, 'start': 0})
        # url = self.formatUrl(term=term, start='0', site='facebook.com', search=self.fb_q)
        url = self.url + 'q=fred+flintstone'

        nglinks = 0
        nlinks = 0
        previousurl = ""
        # resp = requests.get(URL, headers=headers)
        while nlinks < self._LIMIT:
            agent = self.agents[random.randrange(len(self.agents))]
            headers = {"user-agent" : agent}
            if url == previousurl:
                break
            previousurl = url
            try:
                if self.randomsleep is not None:
                    time.sleep(self.randomsleep[0] + random.random() * self.randomsleep[1])
                proxies = {
                    'http': 'http://154.72.204.122:8080',
                    'https': 'https://117.6.161.118:53281',
                }

                # requests.get('http://example.org', proxies=proxies)
                html = requests.get(url, headers=headers, proxies=proxies)
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
                                    break
                            continue
                        except Exception as ex:
                            print(str(type(ex)), ex)
                else:
                    print("servererror", html.status_code, html.reason)
                    print('Interrupted gathering docs for term:', term)
                    print(url)
                    # print(html.content)
                
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        print('Wrote to file', len(self.results), "links", term, 'facebook', 'sleeping...')
        self.randomSleep()
        self.results = []

    def getBbbResults(self, term):
        # https://www.google.com/search?&as_q=Construction&as_qdr=d&as_sitesearch=bbb.org&as_occt=title&start=0
        url = self.formatUrl(term=term, start='0', site='bbb.org', search=self.bbb_q, etime=self.bingbbbtime)

        nglinks = 0
        nlinks = 0
        previousurl = ""
        while nlinks < self._LIMIT:
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
                        if not href: 
                            continue
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
                            if link.text and link.text.startswith('Next') & href.startswith('/search?'):
                                x = re.search("&start=([0-9]+)", href)
                                if x and x.group(1):
                                    # url = self.formatUrl(term=term, start=x.group(1), site='bbb.org', search=self.bbb_q, etime=self.bingbbbtime)
                                    url = re.sub(r"&start=(\d\d?\d?)", f'&start={x.group(1)}', url)
                                    break
                            continue
                        except Exception as ex:
                            print(str(type(ex)), ex)
                            raise ex
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        print('Wrote to file', len(self.results), "links", term, 'BBB', 'sleeping...')
        self.randomSleep()
        self.results = []

    def getWixResults(self, query):
        print('notimplemnted')

    def formatUrl(self, term='', start='0',  site='', search='', etime=''):
        """
        bbb: https://www.google.com/search?q=allintitle:+Construction+site:bbb.org&tbs=qdr:m&start=0
        bbb: https://www.google.com/search?q=intitle:Construction+site:bbb.org+AND+Accredited&oq=intitle:Construction+site:bbb.org+AND+Accredited&tbs=qdr:d&start=0
        bbb: https://www.google.com/search?q=intitle:Home+Improvement+site:bbb.org+AND+Accredited&oq=intitle:Home+Improvement+site:bbb.org+AND+Accredited&tbs=qdr:d&start=0
        bbb: https://www.google.com/search?q=intitle:Home+Improvement+site:bbb.org+AND+Accredited&oq=intitle:Home+Improvement+site:bbb.org+AND+Accredited&tbs=qdr:d&start=0
        """
        query = f'intitle:{term} site:{site}' + (f' AND {search}' if search else '')
        url = self.url + urlencode({'q': query, 'oq': query, 'tbs': f'qdr:{etime}','start': start}, safe=':')
        return url


class Bing(SearchEngine):
    def __init__(self, outfile=None, date=None, config=True):
        super().__init__(outfile, date, config)
        self.url = 'https://www.bing.com/search?'
        self.fb_q = self.fb_q.format(self.date.strftime("%B"),
                                     str(self.date.day),
                                     self.date.strftime("%Y"))
    
    def getFbResults(self, term):
        query = f'{self.fb_q} site: facebook.com intitle: {term}'
        # query = '"Page created - February 7, 2021" site: facebook.com intitle: Home Improvement'
        url = self.url + urlencode({'q': query, 'pq': query.lower(), 'qs': 'n', 'form': 'QBRE', 'sp': '-1', 'first': '0'})
        
        
        nglinks = 0
        nlinks = 0
        previousurl = ""
        while nlinks < self._LIMIT:
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
                                npage = re.search("&first=(\d\d?\d?)", href).group(1)
                                url = re.sub(r"&first=(\d\d?\d?)", f'&first={npage}', url)
                                break
                            continue
                        except Exception as ex:
                            continue
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        print('Wrote to file', len(self.results), "links", term, 'facebook', 'sleeping...')
        self.randomSleep()
        self.results = []

    def getBbbResults(self, term):
        query = f'{self.bbb_q} site:bbb.org intitle:{term}'
        url = self.url + urlencode({'q': query, 'pq': query.lower(), 'qs': 'n', 'form': 'QBRE', 'sp': '-1', 'first': '0'})
        
        
        nglinks = 0
        nlinks = 0
        previousurl = ""
        while nlinks < self._LIMIT:
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
                                npage = re.search("&first=(\d\d?\d?)", href).group(1)
                                url = re.sub(r"&first=(\d\d?\d?)", f'&first={npage}', url)
                                break
                            continue
                        except Exception as ex:
                            continue
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        print('Wrote to file', len(self.results), "links", term, 'BBB', 'sleeping...')
        self.randomSleep()
        self.results = []

    def getWixResults(self, term):
        query = f'{self.wix_q}  intitle:{term}'
        url = self.url + urlencode({'q': query, 'pq': query.lower(), 'qs': 'n', 'form': 'QBRE', 'sp': '-1', 'filters': self.bingwixtime, 'first': '0'}, safe=':')
        
        
        nglinks = 0
        nlinks = 0
        previousurl = ""
        while nlinks < self._LIMIT:
            # agent = self.agents[random.randrange(len(self.agents))]
            agent = self.agents[random.randrange(len(self.agents))]
            headers = {"user-agent" : agent}
            if url == previousurl:
                break
            previousurl = url
            try:
                html = requests.get(url, headers=headers)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    links = soup.find_all('a')
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
                                npage = re.search("&first=(\d\d?\d?)", href).group(1)
                                url = re.sub(r"&first=(\d\d?\d?)", f'&first={npage}', url)
                                break
                            continue
                        except Exception as ex:
                            continue
            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        print('Wrote to file', len(self.results), "links", term, 'Wix', 'sleeping...')
        self.randomSleep()
        self.results = []


class Yahoo(SearchEngine):
    '''
    The links are embedded <a href=https://search.yahoo.com/ .... /RU=https://www.facebook.com... // >
    Everything is encoded --> {0x3a: ':', 0x2f: '/'}
    '''
    def __init__(self, outfile=None, date=None, config=True):
        super().__init__(outfile, date, config)
        self.url = 'https://search.yahoo.com/search?'
    

    def getYahooResults(self, url, term, searchtype):
        nlinks = 0
        previousurl = ""
        while nlinks < self._LIMIT:
            # agent = self.agents[random.randrange(len(self.agents))]
            agent = self.agents[random.randrange(len(self.agents))]
            headers = {"user-agent" : agent}
            if url == previousurl:
                break
            previousurl = url
            try:
                html = requests.get(url, headers=headers)
                if html.status_code == 200:
                    soup = BeautifulSoup(html.text, 'html.parser')
                    # results = soup.find(id="results")
                    results = soup.find("ol", {"class": "searchCenterMiddle"})
                    listofdivs =  results.find_all("div", {"class": "options-toggle"})
                    for div in listofdivs:
                        try:
                            a = div.find('a')
                            href = a.get('href')
                            href =  unquote(href)
                            if re.search(r'^https?://r.search.yahoo', href):
                                real = re.search(r'(https?://.*)//?RK', href[5:])
                                if real:
                                    href = real.group(1)
                            self.results.append({
                                "link": href,
                                "site": urlparse(href).netloc,
                                "engine": "yahoo",
                                "term": term,
                                "date": self.date.strftime("%Y/%m/%d")
                            })
                            nlinks += 1
                        except:
                            continue
                    next = soup.find('a', {"class": "next"})
                    if next:
                        href = next.get('href')
                        href = unquote(href)
                        npage = re.search("&b=(\d\d?\d?)", href).group(1)
                        url = re.sub(r"&b=(\d\d?\d?)", f'&b={npage}', url)

            except Exception as ex:
                print(str(ex))

        self.writeToFile()
        print('Wrote to file', len(self.results), "links", term, searchtype, 'sleeping...')
        self.randomSleep()
        self.results = []

    def getFbResults(self, term, geturl=False):
        '''
        fb: https://www.google.com/search?"Page created - January 01, 2021" inurl:facebook.com intitle:Home Improvement
        '''
        query = f'{self.fb_q} site:facebook.com intitle:{term}'
        url = self.url + urlencode({'p': query, 'b': '0'})
        if geturl:
            print(url)
            return
        self.getYahooResults(url, term, 'facebook')

    def getBbbResults(self, term, geturl=False):
        '''
        # '"Accredited Since:{month}/{day}/{year}" intitle:Construction site:bbb.org'
        '''
        # url = self.formatUrl(term, '0')
        query = f'{self.bbb_q} intitle:{term} site:bbb.org'
        bbbtime =  self.yahoobbbtime if self.yahoobbbtime and self.yahoobbbtime in ['d', 'w', 'm'] else ''
        if bbbtime:
             url = self.url + urlencode({'p': query,'fr2': 'time', 'age': f'1{bbbtime}', 'btf': bbbtime , 'b': '0'})
        else:
            url = self.url + urlencode({'p': query, 'b': '0'})
        if geturl:
            print(url)
            return
        self.getYahooResults(url, term, 'BBB')

    def getWixResults(self, term, geturl=False):
        """
        # s = intext:Proudly created with Wix.com "construction"
        """
        # intitle seach in body and title
        query = f'intext:{self.wix_q} "{term}"'
        wixtime =  self.yahoowixtime if self.yahoowixtime and self.yahoowixtime in ['d', 'w', 'm'] else ''
        if wixtime:
            # &fr2=time&age=1d&btf=d 
            url = self.url + urlencode({'p': query,'fr2': 'time', 'age': f'1{wixtime}', 'btf': wixtime , 'b': '0'})
        else:
            url = self.url + urlencode({'p': query, 'b': '0'})

        if geturl:
            print(url)
            return
        self.getYahooResults(url, term, "Wix")
        

def test_yahooFormatUrl():
    expected = 'https://search.yahoo.com/search?p=%22Page+created+-+February+5%2C+2021%22+site%3A+facebook.com+intitle%3A+Home+Improvement&b=0'
    input = 'Home Improvement'
    y = Yahoo(outfile="yahoo8.csv", date=dt.datetime.today())
    result = y.formatUrl(input, '0')
    assert result == expected

def test_dateSetup():
    g = Google(config=True)
    y = Yahoo()
    b = Bing()
    assert g.date == st.searchday
    assert y.date == st.searchday
    assert b.date == st.searchday
    assert g.outfile == st.outfile
    assert y.outfile == st.outfile
    assert b.outfile == st.outfile

    assert g.fb_q == st.fbsearch
    assert y.bbb_q == st.bbbsearch
    assert b.wix_q == st.wix_q

    g = Google(date=dt.datetime(2021,1,1,1,1,1))
    expectedout = st.outf.format(g.date.strftime("%Y%m%d_%H-%M-%S"))
    assert g.outfile == expectedout

if __name__ == '__main__':
    # test_dateSetup()
    # g = Google()
    # g.getSearchResults('bbb')
    # d = dt.datetime(2021, 2, 5)
    # b = Bing()
    # b.getSearchResults('wix')
    # y = Yahoo(outfile="yahoo8.csv", date=d)
    y = Yahoo()
    y.getSearchResults()



