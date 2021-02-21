# Priority
* Facebook data. Look into Facebook api and getting an agreement to scrape for particular data.

## MVP
* Scrape search pages using Google, Bing, and Yahoo for facebook, Wix and BBB searches using the given 20 terms. 
* Write all results to a csv file. * 
* The Command line call will do all the searches by default and write all results to a single file

## Possible Todos
* handle duplicates. (Don't have a policy howto yet)
* Enable a continue mode so it starts on the term it left off where it left off
* Change the filname to include all the info like ***filename_bing_goog_yahoo_fb_wix_20210212_12-35-11.csv***
* More customization of search parameters using Command line
* Embed in web or gui standalone app with results going to the screen
* scrapers to harvest the biz info from the links
    * Look for libraries/tools that already do the facebook scraping
    * See if I can get a facebook agreement so I can develop it
* harvest more information from the search pages
* Enable more search engines
* Use rotating proxies to decrease the chance of getting blocked
* Use a javascript runner to pop up the link when you get blocked so you can click on the captcha
* Automate it, many variables here



## MVP Develop stuff
* Put the bulk of the code in SearchEngine class to share
    * Each Subclass implement the url/query specifications, filter sites, the pagination regex and substitution
    * Generate the url in formatUrl from configurable search paramaters.