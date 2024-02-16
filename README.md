## Command line program to automate finding new Home Improvement contractor leads from Facebook and WIX using Google, Bing and Yahoo

Commandline program [linkedlead.py](linkedlead.py)
Ways to run the program
```
python linkedlead.py --help
python linkedlead.py --all
python linkedlead.py --bing
python linkedlead.py --yahoo
python linkedlead.py --google
python linklead.py -b -y -g
```

## Configue these 12 variables in [searchterms.py](linkleads/searchterms.py)
### Time stuff
```python
searchday = dt.datetime(2021, 2, 9)
timebbb = 'w'
timewix = 'c'
customdate = (dt.datetime(2020, 11, 1), dt.datetime(2021, 2, 5))
```
### Operational stuff
```python
runsearches = 'all' 
outf = 'outfile_{}.csv'
forceoverwrite = False
LIMIT = 22
randomsleep = (15, 30)
```
### Search terms
```
fb_q = '"Page created - {month} {day}, {year}"'
bbb_q = "Accredited"
wix_q = 'Proudly created with Wix.com'
```

## Edit terms in [terms.py](linkleads/terms.py)
The terms that usuall go in the title search can also be edited

### Getting blocked
* Keep the list of agents updated
* Configure the sleep time ```randomsleep(1.5, 15)```
    * This would cause it to sleep beteen 1 1/2-15 seconds between each page

### Leads are collected in a csv file
