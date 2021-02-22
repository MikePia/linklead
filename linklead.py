import argparse
from linkleads.runll import runLinkedLeads


p = argparse.ArgumentParser(description=' '.join([
    "LeadLinks:"
    "Harvest links from Google, Bing and Yahoo search.",
    "The command line provides control over which search engines",
    "to use. Set search terms, output file, and times in the file",
    "leadlinks/searchterms.py"]))

p.add_argument('-a',
               '--all',
               action='store_true',
               default=False,
               help="Run searches using Bing, Yahoo and Google")
p.add_argument('-b',
               '--bing',
               action='store_true',
               default=False,
               help="Run searches using Bing")
p.add_argument('-y',
               '--yahoo',
               action='store_true',
               default=False,
               help="Run searches using Yahoo")
p.add_argument('-g',
               '--google',
               action='store_true',
               default=False,
               help="Run searches using Google")
p.add_argument('-v',
               '--version',
               action='store_true',
               default=False,
               help="Show the version and exit")

ahgs = p.parse_args()
runLinkedLeads(ahgs)