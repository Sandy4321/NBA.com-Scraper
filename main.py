import requests
from bs4 import BeautifulSoup
import scrape
import getGames

date = input('Enter the game(s) date you want to pull in YYYYMMDD format, after 20151027: ')

url = "http://www.nba.com/gameline/" + str(date) + "/"

homeTeams, awayTeams = getGames.getInitialData(url)
homeTeams, awayTeams = getGames.getTeams(homeTeams, awayTeams)
homeTeams = getGames.removeTeamDuplicates(homeTeams)
awayTeams= getGames.removeTeamDuplicates(awayTeams)
homeTeams = getGames.cleanTeams(homeTeams)
awayTeams = getGames.cleanTeams(awayTeams)

schedule = getGames.createSchedule(awayTeams, homeTeams)
scoreboardURLs = getGames.getScoreboard(date, schedule)

print(scoreboardURLs)

gamePlayerDataOdd, gamePlayerDataEven = scrape.getData(scoreboardURLs)

#print(gamePlayerDataOdd)
names = scrape.getLinks(scoreboardURLs)
names = scrape.getNameLinks(names)
names = getGames.removeTeamDuplicates(names)
names = scrape.getNames(names)
print(names)


print('You have reached the end and the "raw_input()" function is keeping the window open') 
raw_input()

