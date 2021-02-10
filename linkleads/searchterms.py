"""
LeadLinks Search configuration module

This is a quick solution to providing control over the input without typing it 
all into the command line. This could be replaced by a config.txt file, a csv or an excel 
file.

This is a python code file that can be used to configure the search terms and dates used.

Lines beginning with # are comments. Deleting them or this beginning doc quote won't affect anything
"""
import datetime as dt

##################################### Dates #######################################
# These dates 
# sdate applies to facebook and bbb searches
# searchday = dt.datetime.today()
# datetime is (yyyy, m, d, h, min, sec) Time is optional.
searchday = dt.datetime(2021, 1, 1)
# searchday = dt.datetime(2021, 1, 1, 9, 30, 0)

# bbbtime  applies to bbb searches only currently
# wixtime  applies to wix searches only currently
# available values are ["d", "w", "m"]
# Implementing day week and month only because noting else is supported by all three 

bbbtime = "d"
wixtime = "w"


############################# Search Terms #######################################
# Enable these terms on the command line. 
# For example
# LeadLinks -st
# To include quotes, use a combination of single quotes and double quote.

# runsearches may be one of 'all', 'bbb', 'fb', 'wix' or an array like ['fb', 'bbb']
runsearches = 'fb'

fb_q = '"Page created - {month} {day}, {year}"'
bbb_q = '"Accredited Since:{day}/{month}/{year}"'
# bbb_q = '"Accredited Since:" {year}'
# bbb_q = "Accredited"
wix_q =  'intext:Proudly created with Wix.com "construction"'

############################# Save to file ###########################################
# They can be set to the same or different outfs. {} will place a date
outf = 'outfile_{}.csv'

############################# misc ############################
# Introduce time between hits. 
randomsleep = (.5, 1.1)
# randomsleep = None


########### Do not alter below line ##################################################
def formatTerms(dadate=None):
    global fb_q
    global bbb_q
    global outf
    global searchday 
    if dadate is None:
        dadate = searchday

    fb = fb_q.format(month=dadate.strftime("%B"), day=dadate.day, year=dadate.year)
    if bbb_q:
        bbb = bbb_q.format(day=dadate.day, month=dadate.month, year=dadate.year)
    out = outf.format(dadate.strftime("%Y%m%d_%H-%M-%S"))
    return fb, bbb, out

fbsearch, bbbsearch, outfile = formatTerms()
print()


