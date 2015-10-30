import requests
from bs4 import BeautifulSoup

#scrapes matchups for the day based on schedule url given. Returns the home and away team names. (Chicago Bulls returns CHI)
def getInitialData(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    homeTeamName = soup.find_all("h5", {"class": "nbaModTopTeamName hometeam"})
    awayTeamName = soup.find_all("h5", {"class": "nbaModTopTeamName awayteam"})
    return homeTeamName, awayTeamName

#modifies data to make it into 2 separate lists that only contain text and not the individual urls
def getTeams(homeTeamName, awayTeamName):
    homeTeams = []
    awayTeams = []
    for team in homeTeamName:
        homeTeams.append(team.text)
    for team in awayTeamName:
        awayTeams.append(team.text)
    return homeTeams, awayTeams

#removes duplicate teams from list without rearranging order
def removeTeamDuplicates(teams):
    output = []
    seen = set()
    for team in teams:
        if team not in seen:
            output.append(team)
            seen.add(team)
    return output

#converts from unicode to string just to test
def cleanTeams(teams):
    output = []
    newTeam = "" 
    for team in teams:
        newTeam = team.encode('ascii', 'ignore')
        output.append(newTeam)
    return output

#combines separate team lists to create matchups for the day. (CHI and MIL combine to CHIMIL)
def createSchedule(awayTeam, homeTeam):
    output = []
    for index in range(len(awayTeam)):
        matchup = awayTeam[index] + homeTeam[index]
        output.append(matchup)
    return output        

#concatenates base nba.com game url with date and matchups to create URLs for each game that occurred
def getScoreboard(date, schedule):
    output = []
    for index in range(len(schedule)):
        gameURL = "http://www.nba.com/games/" + str(date) + "/" + schedule[index] + "/gameinfo.html?ls=iref:nba:scoreboard"
        output.append(gameURL)
    return output




