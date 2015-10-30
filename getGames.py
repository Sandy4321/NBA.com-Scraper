import requests
from bs4 import BeautifulSoup


def getInitialData(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    homeTeamName = soup.find_all("h5", {"class": "nbaModTopTeamName hometeam"})
    awayTeamName = soup.find_all("h5", {"class": "nbaModTopTeamName awayteam"})
    return homeTeamName, awayTeamName


def getTeams(homeTeamName, awayTeamName):
    homeTeams = []
    awayTeams = []
    for team in homeTeamName:
        homeTeams.append(team.text)
    for team in awayTeamName:
        awayTeams.append(team.text)
    return homeTeams, awayTeams

def removeTeamDuplicates(teams):
    output = []
    seen = set()
    for team in teams:
        if team not in seen:
            output.append(team)
            seen.add(team)
    return output

def cleanTeams(teams):
    output = []
    newTeam = "" 
    for team in teams:
        newTeam = team.encode('ascii', 'ignore')
        output.append(newTeam)
    return output

def createSchedule(awayTeam, homeTeam):
    output = []
    for index in range(len(awayTeam)):
        matchup = awayTeam[index] + homeTeam[index]
        output.append(matchup)
    return output        

def getScoreboard(date, schedule):
    output = []
    for index in range(len(schedule)):
        gameURL = "http://www.nba.com/games/" + str(date) + "/" + schedule[index] + "/gameinfo.html?ls=iref:nba:scoreboard"
        output.append(gameURL)
    return output




