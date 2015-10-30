#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

#uses created URLs from getGames.py to start scraping individual player data. NBA.com has specific tags called "even" and "odd"
#for each player. Thus they are split into different lists for clarity. 
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
    


#gets the href links for each player which contains the first and last name of the player.
def getLinks(scoreboardURLs):
    playerNames = []
    for link in scoreboardURLs:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")

        playerData = soup.find_all("a")
        for link in playerData:
            playerNames.append(link.get("href"))

    return playerNames

#gathers only links that have "/playerfile/" in them to make sure that only player name links are being added 
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

#cleans up the links to remove certain parts and leave the player first and last name, capitalized appropriately
def getNames(links):
    names = []
    for link in links:
        link = link.replace('/playerfile/', '')
        link = link.replace('/index.html', '')
        link = link.replace('_', ' ')
        link = link.title()
        names.append(link)
    return names
        

  



