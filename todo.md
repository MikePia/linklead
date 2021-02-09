## MVP
* Scrape search pages for facebook, Wix and BBB using the given 20 terms. 
* Write all results to a csv file. * 
* The Command line call will do all the searches by default and write all results to a single file

## Possible Todos
* handle duplicates. (Don't have a policy howto yet)
* Customization of search parameters using an input file
* Customization of search parameters using Command line
* Customize LIMIT on the command line
* Specify which search engines on commandline
* Specify which sites to do on the command line (of the 3 current supported)
* Embed in web or gui standalone app with results going to the screen
* scrapers for business info for the three sites. 
    * Look for libraries/tools that already do the facebook scraping
    * See if I can get a facebook agreement so I can develop it
* harvest more than just the link

## MVP Develop stuff
* Put the bulk of the code in SearchEngine class to share
    * Each Subclass implement the url/query specifications, filter sites, the pagination regex and substitution
    * Generate the url in formatUrl from configurable search paramaters.