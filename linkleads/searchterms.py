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
# searchday applies to the facebook search term and changes the name of the outputfile
# searchday = dt.datetime.today()
# searchday = dt.datetime.today() - dt.timedelta(days=1)

# datetime is (yyyy, m, d, h, min, sec) Time is optional.
searchday = dt.datetime(2021, 2, 9)
# searchday = dt.datetime(2021, 1, 1, 9, 30, 0)


# timebbt  applies to bbb searches only currently and sets the engine time to previous day, or week or a custom time (for bing)
# timewix  applies to wix searches only currently and sets the engine time to previous day, or week or a custom time (for bing)
# available values are ["d", "w", "m", "y", 'c']
# c is for custom, If you you choose custom, then then custom dates needs to be filled in
# Implementing day week and month only because noting else is supported by all three 
# Note that Yahoo has d, w, m only anything else disables it for yahoo searches

timebbb = ''
timewix = 'm'

bingcustomdate = (dt.datetime(2020, 11, 1), dt.datetime(2021, 2, 5))


############################# Search Terms #######################################
# Enable these terms on the command line. 
# For example
# LeadLinks -st
# To include quotes, use a combination of single quotes and double quote.

# runsearches may be one of 'all', 'bbb', 'fb', 'wix' or an array like ['fb', 'bbb']
# runsearches = 'bbb'
runsearches = 'all'

fb_q = '"Page created - {month} {day}, {year}"'
# bbb_q = '"Accredited Since:{day}/{month}/{year}"'
# bbb_q = '"Accredited Since:" {year}'
# bbb_q = "Accredited"
bbb_q = ""
wix_q =  'Proudly created with Wix.com'

############################# Save to file ###########################################
# They can be set to the same or different outfs. {} will place a date
outf = 'outfile_{}.csv'

# If True, overwrite the file, if False, preserve the data (checks that it begins with prescribed header)
# Note that using the today() method above will cause every run to create a new file using a new time in the name
forceoverwrite = False

############################# misc ############################
# Introduce time between new searches so as not to tax the server and or get 429'd. 
randomsleep = (5, 10)
# randomsleep = None

# Limit the number of links harvested per search term
# LIMIT = 1440
LIMIT = 22


########### Do not alter below line ##################################################
def getBingCustomDates(beg, end):
    '''
    This gets the strange format for Bings custom date which looks something like: &filters=ex1:"ez5_18423_18659"
    18628 = Jan 1 2021,
    18629 = Jan 2 2021,
    '''
    a = dt.datetime(2021, 1, 1)
    JAN2021 =  18628
    begn = (beg - a).days + JAN2021
    endn = (end - a).days + JAN2021
    return f'ex1:"ez5_{begn}_{endn}"'

def getBingTimeParam(tt):
    if not tt:
        return ''
    assert tt in ['d', 'w', 'm', 'y', 'c']
    if tt in ['y', 'c']:
        if tt == 'y':
            bt = getBingCustomDates(dt.datetime.today()- dt.timedelta(days=365), dt.datetime.today(), )
        else:
            bt = getBingCustomDates(*bingcustomdate)
    else:
        bt = {'d': 'ex1:"ez1"', 'w': 'ex1:"ez2"', 'm': 'ex1:"ez3"'}[tt]
    return bt

def formatTerms(dadate=None):
    global fb_q
    global bbb_q
    global outf
    global searchday 
    global timebbb
    if dadate is None:
        dadate = searchday

    fb = fb_q.format(month=dadate.strftime("%B"), day=dadate.day, year=dadate.year)
    bbb = bbb_q.format(day=dadate.day, month=dadate.month, year=dadate.year) if bbb_q else ''
    out = outf.format(dadate.strftime("%Y%m%d_%H-%M-%S"))
    bbt =  getBingTimeParam(timebbb)
    ybt = timebbb if timebbb in ['d', 'w', 'm'] else ''
    bwt = getBingTimeParam(timewix)
    ywt = timewix if timewix in ['d', 'w', 'm'] else ''

    return fb, bbb, out, bbt, ybt, bwt, ywt

fbsearch, bbbsearch, outfile, bingbbbtime, yahoobbbtime, bingwixtime, yahoowixtime = formatTerms()
print()


