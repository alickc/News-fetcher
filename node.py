import requests

import googlesearch_script
import constants
from news import sputnik, dailysabah, theguardian, hurriyetdailynews, pravdareport, independent, turkiyenewspaper
import os


def fetchHistory(site, blinks=True, btitles=False):
    for cat in constants.supportedSites:
        if cat in site:
            rcat = cat
    print("history for " + rcat + " fetched")
    files = os.listdir(constants.path + rcat)
    links = []
    titles = []
    for file in files:
        with open(constants.path + rcat + "/" + file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            titles.append(lines[1][:-2])
            links.append(lines[0][5:-1])
    if (blinks == True) and (btitles == False):
        return links
    elif (blinks == True) and (btitles == True):
        return links, titles
    elif (blinks == False) and (btitles == True):
        return titles


def initializeFolders():
    for folder in constants.supportedSites:
        if not os.path.exists(path=constants.path + folder):
            os.mkdir(constants.path + folder)

def checkSite(sites):
    temp = [site for site in sites if any(x in site for x in constants.supportedSites)]
    if(len(temp)==0):
        print("Input websites are non-supported or invalid.\n+Be sure that your web-site is one of them:\n" +
              str(constants.supportedSites))
    results = []
    for s in temp:
        try:
            s = s.replace("http://","").replace("http:/","")
            s = "http://" + s
            response = requests.get(s)
            print("URL is valid and exists on the internet: " + s)
            results.append(s)
        except requests.ConnectionError as exception:
            print("URL does not exist on Internet " + s)
    if len(results)>0:
        print("Supported and valid results: " + str(results))
        return results
    else:
        exit(0)


def start(sites, keywords):
    sites = checkSite(sites)
    initializeFolders()
    for site in sites:
        if ("sputnik" in site):
            hlinks = fetchHistory(site, blinks=True, btitles=False)
            c = len(os.listdir(constants.path + "sputnik"))
            print(c)
            sputnik.getNews("https://sputniknews.com/search", hlinks)
        else:
            for keyword in keywords:
                hlinks = fetchHistory(site, blinks=True, btitles=False)
                print(hlinks)
                results = (
                    googlesearch_script.search(keyword + " site:" + site + " after:" + constants.date_after,
                                               num_results=constants.num_results))
                print(len(results))
                # results = ["https://sputniknews.com"]
                for link in results:
                    if link not in hlinks:
                        print(link)
                        if "independent" in site:
                            c = len(os.listdir(constants.path + "independent"))
                            print(c)
                            independent.getNews(link, c)
                        elif "guardian" in site:
                            c = len(os.listdir(constants.path + "guardian"))
                            print(c)
                            theguardian.getNews(link, c)
                        elif "pravdareport" in site:
                            c = len(os.listdir(constants.path + "pravdareport"))
                            print(c)
                            pravdareport.getNews(link, c)
                        elif "dailysabah" in site:
                            c = len(os.listdir(constants.path + "dailysabah"))
                            print(c)
                            dailysabah.getNews(link, c)
                        elif "turkiyenewspaper" in site:
                            c = len(os.listdir(constants.path + "turkiyenewspaper"))
                            print(c)
                            turkiyenewspaper.getNews(link, c)
                        elif "hurriyetdailynews" in site:
                            c = len(os.listdir(constants.path + "hurriyetdailynews"))
                            print(c)
                            hurriyetdailynews.getNews(link, c)
                    else:
                        print(link + " already fetched before.")
    for i in constants.supportedSites:
        saveAsTableTxt(i)


def saveAsTableTxt(site):
    files = os.listdir(constants.path + site)
    links = []
    titles = []
    for file in files:
        with open(constants.path + site + "/" + file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            titles.append(lines[1][:-2])
            links.append(lines[0][5:-1])
    writer = "PATH\tTITLE\tLINK\n"
    for i in range(len(files)):
        writer += files[i] + "\t" + titles[i] + "\t" + links[i] + "\n"
    with open(constants.path + site + "Table.txt", "a+",
              encoding="utf-8") as f:
        f.write(writer)
