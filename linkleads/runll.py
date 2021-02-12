from linkleads.searchengine import Bing, Yahoo, Google


def runLinkedLeads(args):
    print('\nSearch Running. Press Ctrl-C to cancel\n')
    searchEngines = []
    if args.all:
        searchEngines = ['bing', 'yahoo', 'google']
    else:
        if args.bing:
            searchEngines.append('bing')
        if args.yahoo:
            searchEngines.append('yahoo')
        if args.google:
            searchEngines.append('google')
    try:
        for engine in searchEngines:
            if engine == 'bing':
                b = Bing()
                b.getSearchResults(geturl=True)
            if engine == 'yahoo':
                y = Yahoo()
                y.getSearchResults()
            if engine == 'bing':
                g = Google()
                g.getSearchResults()
    except KeyboardInterrupt:
        print('Search Canceled')
