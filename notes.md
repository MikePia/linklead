# Gig for Dennis Thompson from Upwork

*  Completed first version 2/20/21
### Commandline program
[linklead.py](linklead.py)

### Configue these 12 variables in [searchterms.py](linkleads/searchterms.py)

```python
searchday = dt.datetime(2021, 2, 9)
timebbb = 'w'
timewix = 'c'
customdate = (dt.datetime(2020, 11, 1), dt.datetime(2021, 2, 5))
runsearches = 'all'
fb_q = '"Page created - {month} {day}, {year}"'
bbb_q = "Accredited"
wix_q = 'Proudly created with Wix.com'
outf = 'outfile_{}.csv'
forceoverwrite = False
randomsleep = (15, 30)
LIMIT = 22
```
### Edit terms in [terms.py](linkleads/terms.py)

## Disorganized Scraper Notes


https://www.wincher.com/blog/google-search-operators
http://devcoma.blogspot.com/2017/04/google-search-parameters-resources.html

#### Programmable search engine
Is a google product. I believe most of the seach parameters can be used with url parameters but there are no equivalence docs
https://developers.google.com/custom-search/docs/xml_results

### The important parameters for Google
discard all the gobledegook encoded BS the server uses to track 
##### google could change this stuff but not likely in the near future.
<table>
    <tr>
        <th>param</th>
        <th>meaning</th>
        <th>regular use</th>
    </tr>
    <tr>
        <td><strong>q</strong></td>
        <td>each word must be found uses <strong>AND</strong></td>
        <td>Seperate words with '+'</td>
    </tr>
    <tr>
        <td><strong>oq</strong></td>
        <td>Any word must be found. Uses <strong>OR</strong></td>
        <td>Seperate words with '+'</td>
    <tr>
        <td><strong>eq</strong></td>
        <td>No word found. Uses <strong>NOT</strong></td>
        <td>Seperate words with '+'</td>
    </tr>
    <tr>
        <td><strong>start</strong></td>
        <td>Used for pagination </td>
        <td>Locate Next in link.text and the href is relative beginning w  /search?</td>
    </tr>
    <tr>
        <td><strong>site:</strong></td>
        <td>Not a seperate parameter. Include as part of q, eq, oq</td>
        <td>https://www.google.com/search?&q=site:google.com/finance+GME</td>
    </tr>
    <tr>
        <td><strong>-</strong></td>
        <td>Add to q string</td>
        <td>https://www.google.com/search?&q=google+urls+-presentation+-Console&oq=google+urls+-presentation+-Console</td>
    </tr>
</table>

<table class="table">
    <thead>
        <tr>
            <th colspan="2">II. Advanced Search Operators</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">intitle:</th>
            <td><strong><a href="https://www.google.com/search?q=intitle:"tesla+vs+edison"">intitle:"tesla vs
                        edison"</a></strong><br>Search only in the page's title for a word or phrase. Use exact-match
                (quotes) for phrases.</td>
        </tr>
        <tr>
            <th scope="row">allintitle:</th>
            <td><strong><a href="https://www.google.com/search?q=allintitle:+tesla+vs+edison">allintitle:&nbsp;tesla vs
                        edison</a></strong><br>Search the page title for every individual&nbsp;term following
                "allintitle:". Same as multiple intitle:'s.</td>
        </tr>
        <tr>
            <th scope="row">inurl:</th>
            <td><strong><a href="https://www.google.com/search?q=tesla+announcements+inurl:2016">tesla announcements
                        inurl:2016</a></strong><br>Look for a word or phrase&nbsp;(in quotes) in the document URL. Can
                combine with other terms.</td>
        </tr>
        <tr>
            <th scope="row">allinurl:</th>
            <td><strong><a href="https://www.google.com/search?q=allinurl:+amazon+field-keywords+nikon">allinurl: amazon
                        field-keywords nikon</a></strong><br>Search the URL for every individual term following
                "allinurl:". Same as multiple inurl:'s.</td>
        </tr>
        <tr>
            <th scope="row">intext:</th>
            <td><strong><a href="https://www.google.com/search?q=intext:"orbi+vs+eero+vs+google+wifi"">intext:"orbi
                        vs eero vs google wifi"</a></strong><br>Search for a word or phrase&nbsp;(in quotes),
                but&nbsp;only in the body/document text.</td>
        </tr>
        <tr>
            <th scope="row">allintext:</th>
            <td><strong><a href="https://www.google.com/search?q=allintext:+orbi+eero+google+wifi">allintext: orbi eero
                        google wifi</a></strong><br>Search the body text for&nbsp;every individual term following
                "allintext:". Same as multiple intexts:'s.</td>
        </tr>
        <tr>
            <th scope="row">filetype:</th>
            <td><strong><a href="https://www.google.com/search?q="tesla+announcements"+filetype:pdf">"tesla
                        announcements" filetype:pdf</a></strong><br>Match only a specific file type. Some examples
                include&nbsp;PDF, DOC, XLS, PPT, and TXT.</td>
        </tr>
        <tr>
            <th scope="row">related:</th>
            <td><strong><a
                        href="https://www.google.com/search?q=related:nytimes.com">related:nytimes.com</a></strong><br>Return
                sites that are related to a target domain. Only works for larger domains.</td>
        </tr>
        <tr>
            <th scope="row">AROUND(X)</th>
            <td><strong><a href="https://www.google.com/search?q=tesla+AROUND(3)+edison">tesla AROUND(3)
                        edison</a></strong><br>Returns results where the two terms/phrases are within (X)&nbsp;words of
                each other.</td>
        </tr>
    </tbody>
</table>

<table class="table">
    <thead>
        <tr>
            <th colspan="2">III. Unreliable/Deprecated Operators</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">~</th>
            <td><strong><a href="https://www.google.com/search?q=~cars">~cars</a></strong><br>Include synonyms. Seems to
                be unreliable, and synonym inclusion&nbsp;is default now.</td>
        </tr>
        <tr>
            <th scope="row">+</th>
            <td><strong><a href="https://www.google.com/search?q= +cars">+cars</a></strong><br>Force exact-match on a
                single phrase. Deprecated with the launch of Google+.</td>
        </tr>
        <tr>
            <th scope="row">daterange:</th>
            <td><strong><a href="https://www.google.com/search?q=tesla+announcements+daterange:2457663-2457754">tesla
                        announcements daterange:2457663-2457754</a></strong><br>Return results in the specified
                range.&nbsp;Can be inconsistent. Requires 
                [Julian dates](http://www.searchcommands.com/julian/#:~:text=Julian Date Searches,since January 1, 4713 BCE.)</td>
        </tr>
        <tr>
            <th scope="row">link:</th>
            <td><strong><a href="https://www.google.com/search?q=link:nytimes.com">link:nytimes.com</a></strong><br>Find
                pages that link to the target domain. This operator was deprecated in early 2017.</td>
        </tr>
        <tr>
            <th scope="row">inanchor:</th>
            <td><strong><a href="https://www.google.com/search?q=inanchor:">inanchor:"tesla
                        announcements"</a></strong><br>Find pages linked to with the specified anchor text/phrase. Data
                is heavily sampled.</td>
        </tr>
        <tr>
            <th scope="row">allinanchor:</th>
            <td><strong><a
                        href="https://www.google.com/search?q=allinanchor:+tesla+announcements">allinanchor:&nbsp;tesla
                        announcements</a></strong><br>Find pages with all individual terms after "inanchor:" in the
                inbound anchor text.</td>
        </tr>
    </tbody>
</table>



https://www.google.com/search?&q=google+urls+-presentation+-Console&oq=google+urls+-presentation+-Console

### Embedding the site and intitle are  part of the q parameter
* Need to include oq parameter with
* start 
###### "Page created - February 5, 2021" inurl:facebook.com intitle:Home Improvement
https://www.google.com/search?
q="Page+created+-+February+5,+2021"+site:facebook.com+intitle:Home+Improvement
&oq="Page+created+-+February+5,+2021"+site:facebook.com+intitle:Home+Improvement
&start=0

### Generated from server- sending it back gets same results
https://www.google.com/search?q="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&oq="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&ie=UTF-8
https://www.google.com/search?q="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&oq="Page+created+-+February+7,+2021"+inurl:facebook.com+intitle:Home+Improvement&ie=UTF-8&start=0

### possible extra params
&client=ubuntu&channel=fs
&ie=utf-8
&oe=utf-8

# Bing
"Page created - February 7, 2021" site:facebook.com intitle: Home Improvement
"Page created - February 7, 2021" site:facebook.com intitle: Home Improvement
"Page created - February 7, 2021" site: facebook.com intitle: Home Improvement

<table>
    <tr>
        <th>param</th>
        <th>meaning</th>
        <th>regular use</th>
    </tr>
    <tr>
        <td><strong>q</strong></td>
        <td>each word must be found uses <strong>AND</strong></td>
        <td>Seperate words with '+'</td>
    </tr>
    <tr>
        <td><strong>pq</strong></td>
        <td>both both p and pq for some reason </td>
        <td>The terms and keywords all go in p and pq</td>
    </tr>
    <tr>
        <td><strong>&filters=</strong></td>
        <td>time arg or custom date</td>
        <td>ex1:ez1 for example</td>
    </tr>
    <tr>
        <td><strong>pq</strong></td>
        <td>both both p and pq for some reason </td>
        <td>The terms and keywords all go in p and pq</td>
    </tr>
    <tr>
        <td><strong>pq</strong></td>
        <td>both both p and pq for some reason </td>
        <td>The terms and keywords all go in p and pq</td>
    </tr>
    <tr>
        <td><strong>first</strong></td>
        <td>Pagination</td>
        <td>Seperate words with '+'</td>
    </tr>
</table>

### Search Engine date stuff
<table>
    <tr>
        <th>google term</th>
        <th>meaning</th>
        <th>Google</th>
        <th>Bing</th>
        <th>Yahoo</th>
    </tr>
        <td>h</td>
        <td>hour</td>
        <td>&as_qdr=h</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>d</td>
        <td>day</td>
        <td>&as_qdr=d</td>
        <td>&filters=ex1:"ez1"</td>
        <td>&fr2=time&age=1d&btf=d</td>        
    </tr>
      <tr>
        <td>w</td>
        <td>week</td>
        <td>&as_qdr=w</td>
        <td> &filters=ex1:"ez2"</td>
        <td>&fr2=time&age=1w&btf=w</td>
    </tr>
    <tr>
        <td>m</td>
        <td>month</td>
        <td>&as_qdr=m</td>
        <td>&filters=ex1:"ez3"</td>
        <td>&fr2=time&age=1m&btf=m</td>
    </tr>
    <tr>
        <td>y</td>
        <td>year</td>
        <td>&as_qdr=d</td>
        <td>&filters=ex1:"ez5_18423_18659""</td>
        <td></td>
    </tr>
    <tr>
        <td>c</td>
        <td>custom</td>
        <td>&tbs=cdr:1,cd_min:1/31/2021,cd_max:1/9/2021</td>
        <td>&filters=ex1:"ez5_18628_18629"</td>
        <td></td>
    </tr>
    <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>18628 = Jan 1 2021</td>
    <td></td>
    </tr>
</table>
#### Notes on date stuff above
* Google has  date: and daterange: parameter-- http://www.searchcommands.com/ (?)
    * Haven't implemented the goolge date range -- neither &as_qdr nor daterange:
    * The &as_adr may be responsible for getting flagged by google
* Notice that Yahoo date alters three parameters-- Yahoo has no date range
https://www.google.com/search?
q=intext:Proudly+created+with+Wix.com+"Home+Improvement"
&source=lnt
&tbs=cdr:1,cd_min:1/1/2021,cd_max:2/10/2021
&tbm=


### Google BBB using as_qdr
* Construction in title on bbb.org for the past day:0
https://www.google.com/search?&as_q=Construction&as_qdr=d&as_sitesearch=bbb.org&as_occt=title

hl=en
&as_epq=
&as_oq=
&as_eq=
&as_nlo=
&as_nhi=
&lr=
&cr=
&safe=images
&as_filetype=
&tbs=
['h',

intitle:Construction site:bbb.org AND Accredited plus past 24 hour
https://www.google.com/search?
&q=intitle:Construction+site:bbb.org+AND+Accredited
&oq=intitle:Construction+site:bbb.org+AND+Accredited
&tbs=qdr:d
&hl=en



 'd', 'w', 'm', 'y']

# Yahoo
"Page created - February 7, 2021" site:facebook.com intitle: Home Improvement
https://search.yahoo.com/search
p="Page+created+-+February+8 2C+2021"+site:facebook.com+intitle:+Home+Improvement
&fr2=sb-top
&fr=yfp-t
&fp=1
&n=30

#### Yahoo links a different approach -- with  the ;_ylt param included
##### Quick example based on the URL you provided:
* http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=<My_Keyword>
Page 1 (offset = 10 x 1 - 9 = 1)

* http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=<My_Keyword>&b=1
Page 2 (offset = 10 x 2 - 9 = 11)

* http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=<My_Keyword>&b=11
Page 3 (offset = 10 x 3 - 9 = 21)

* http://search.yahoo.com/search;_ylt=A0oG7l7PeB5P3G0AKASl87UF?p=<My_Keyword>&b=21

### Yahoo next
https://search.yahoo.com/search?p="Page+created+-+February+5,+2021"+site:facebook.com+intitle:+Home+Improvement&b=11
Baskcally find the value of &b and replace it in the original search

### Scraping Yahoo links with soup
* [stack post using jsoup that shows this in link](https://stackoverflow.com/questions/33736046/how-to-extract-results-from-a-yahoo-search)
* soup.find(id="results").find("ol", {"class": "searchCenterMiddle"}).find_all("div", {"class": "options-toggle"})[0].find('a')['href']
* Note that one time this approach found actual links, but every other time this produced a link to a yahoo search that included the real link as RU=https: ...

### originals from DT
inurl:bbb.org "Accredited Since:2/5/2021" intitle:Construction

intext:Proudly created with &.com "construction"
this 1 i have to change the time created to 24 hours or less


### Bing next
https://www.bing.com/search?
q="Page+created+-+February+5 2c+2021"+site:+facebook.com+intitle:+Home+Improvement
&first=12
&FORM=PORE

### The othere 2
https://www.bing.com/search?q=fred
&form=QBLH
&sp=-1
&pq=fred
&sc=8-4
&qs=n&sk=&cvid=7CB8FB843D1F42BE8EE5878EC76A3EB4

### Google bor BBB
https://www.google.com/search?q=allintitle:+Construction+site:bbb.org&tbs=qdr:m
&lr=
&hl=en
&source=lnt
&sa=X
&ved=2ahUKEwjm2Pv82dzuAhVCBs0KHRiXDLYQpwV6BAgKECM
&biw=1755
&bih=895

http://www.searchcommands.com/yahoo/

<table style= border-color: solid black;>
    <tr>
        <th>param</th>
        <th>meaning</th>
        <th>stuff</th>
    </tr>
    <tr>
        <td> site: </td>
        <td> Restrict a search to a single site </td>
        <td> The site: restrict a search to one site or to list all the pages Yahoo has indexed from one site. </tr>
    <tr>
        <td> hostname: </td>
        <td> List pages which link to a page </td>
        <td> </td>
    </tr>
     <tr>
        <td> inurl: </td>
        <td>Restrict a search so that some keywords must appear in the page address </td>
        <td>
        </td>
    </tr>
     <tr>
        <td> hostname: </td>
        <td> Restrict a search to a single host name </td>
        <td>
        </td>
    </tr>
    <tr>
        <td> intitle: </td>
        <td> Restrict a search so that some of the keywords must appear in the title </td>
        <td></td>
    </tr>
    <tr>
        <td> 
            news
        </td>
        <td> 
            Include and link to news headlines which match the keyword
        </td>
        <td></td>
    </tr>
    <tr>
        <td> 
            quote
        </td>
        <td> 
            stock quote
        </td>
        <td></td>
    </tr>
</table>

https://search.yahoo.com/search?
p=intext:intext:Proudly+created+with+Wix.com+"construction"+"Home+Improvement"
&ei=UTF-8
&fr2=time
&age=1d
&btf=d

### stuff from a scraper code here
https://github.com/NikolaiT/GoogleScraper/blob/master/GoogleScraper/http_mode.py
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Connection': 'keep-alive',
}
