#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def getData(scoreboardURLs):
    gamePlayerDataOdd =[]
    gamePlayerDataEven =[]
    for link in scoreboardURLs:
        r = requests.get(link)

        soup = BeautifulSoup(r.content, "html.parser")

        playerDataOdd = soup.find_all("tr", {"class": "odd"})
        playerDataEven = soup.find_all("tr", {"class": "even"})
        for player in playerDataOdd:
            gamePlayerDataOdd.append(player.text)
        for player in playerDataEven:
            gamePlayerDataEven.append(player.text)
    return gamePlayerDataOdd, gamePlayerDataEven
    



def getLinks(scoreboardURLs):
    playerNames = []
    for link in scoreboardURLs:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")

        playerData = soup.find_all("a")
        for link in playerData:
            playerNames.append(link.get("href"))

    return playerNames

def getNameLinks(hreflinks):
    keyword = u'/playerfile/'
    playerlinks = []
    for link in hreflinks:
        try:
            if keyword in link:
                playerlinks.append(link)
        except:
            pass
    return playerlinks

def getNames(links):
    names = []
    for link in links:
        link = link.replace('/playerfile/', '')
        link = link.replace('/index.html', '')
        link = link.replace('_', ' ')
        names.append(link)
    return names
        

  



