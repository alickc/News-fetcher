# news-fetcher
Scrapping news from various websites to txt files with keyword and website selection on selenium driver.



supportedSites = ["independent", "guardian", "sputnik", "pravdareport", "dailysabah","turkiyenewspaper", "hurriyetdailynews"]

Scrapping scripts for each supported site is under the "news" package. While html-schemas of websites can change in time, code changes may be needed. Therefore, each website's script is created seperately for easy-to-understand.

In case of selector change, please edit necessary script with new class name.

**Usage example:**
```
python newsFetcher.py -l theguardian.com dailysabah.com -p myPath -d ../chromedriver_win32_2/chromedriver.exe -da 2020-09-25 -k Armenia-Azerbaijan Karabakh 
```


** For sputnik.com:

If your list includes sputnik, selenium will be work on normal mode instead of headless. You will be directed to sputnik search page and make your search own with advanced search options. Click on "get more" button until you reach the point you wanted to fetch and **open new tab bar on chrome driver to start the process.** The reason for manual search is the getting the advantage of advanced search of sputnik <3. 
