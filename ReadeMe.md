## Gig for Dennis Thompson Mike Petersen mike@zerosubstance.org
Completed first version 2/10/21
* 2/12/21

### Reccomend install of a program editor
* Atom will make editing the files easier
* And has a Command Prompt (a package install) to make running the program easier
#### [Atom code editor](https://atom.io/)
* After installation, Install the package to run command prompt
    *  Click Packages
        * Settings View
            * Install Packages/Themes
                * In the search box type 
                ```plateformio-ide-terminal``` click install
* When it is done installing type ```Alt-shift-T``` to open a terminal
    * You can also find it in the packages menu *when* you forget the shortcut
![Atom](images/atom.png)
## Commandline program [linkedlead.py](linkedlead.py)
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
* I managed to piss of Bing last night. So I placed an addition sleep time between pagination 
* Configure ```randomsleep(1.5, 15)```
    * This would cause it to sleep beteen 1 1/2-15 seconds between each page
    * Ran yahoo this in wee hours (with LIMIT set to ~500 hits per search) and results are in the included file
    * the searchday set to today()

### Using the CSV file
* Excel needs to open the files with the comma as the seperator value
* If you open it and the entire row is in the fisrt cell, close it and open it by browsing to the file
    * From in excel, browse to the file and enable open any type of file (*.*)
    * click on file and set the delimiter to comma
* Format the links as links