me
# -*- coding: utf-8 -*-
"""
Creating a real CSV output
"""
import csv
from nflgame import statmap

"""
Function that reads to CSV from nflgame object
"""
def csvIterator(gameFile, week, fileName, allfields=True):

    """
    Grabs a list of fields
    """
    fields, rows = set([]), []
    players = list(gameFile)
    for p in players:
        for field, stat in p.stats.iteritems():
            fields.add(field)
    if allfields:
        for statId, info in statmap.idmap.iteritems():
            for field in info['fields']:
                fields.add(field)
    fields = sorted(list(fields))

    """
    Grabs a list of Players
    """
    for p in players:
        d = {
            'name': p.name,
            'id': p.playerid,
            'home': p.home and 'yes' or 'no',
            'team': p.team,
            'pos': 'N/A',
            'week': week
        }
        if p.player is not None:
            d['pos'] = p.player.position

        """
        Adds the stat to each field
        """
        for field in fields:
            if field in p.__dict__:
                d[field] = p.__dict__[field]
            else:
                d[field] = ""
        rows.append(d)

    fieldNames = ["name", "id", "home", "team", "pos", "week"] + fields
    rows = [dict((f, f) for f in fieldNames)] + rows
    csv.DictWriter(open(fileName, 'w+'), fieldNames).writerows(rows)

"""
This section does the actual tasks of writing to CSV
"""
for weekNum in range(1,7):
    gameFile = nflgame.combine_game_stats(nflgame.games(2015, week = weekNum))
    createCSV(gameFile,weekNum,"2015week"+str(weekNum)+".csv")

"""
Function that combines all CSVs into one baby
"""
import glob
import os

os.getcwd()
os.chdir("week2015\\")

interesting_files = glob.glob("*.csv")

header_saved = False
with open('2015stats.csv','wb') as fout:
    for filename in interesting_files:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)

########################################################################################################################

"""
Downloading a CSV of the entire 2015 NFL Schedule
"""
import nflgame
import nflgame.sched
import csv

schedule_games = nflgame.sched.games

def writeScheduletoCSV(year):
    with open('Schedule_'+str(year)+'.csv', 'wb') as csvfile:
        schedulewriter = csv.writer(csvfile, delimiter=',')
        schedulewriter.writerow(['Week', 'Home', 'Away', 'Year', 'Weekday', 'Month', 'Day'])
        for item, info in schedule_games.iteritems():
            if info['year'] == year and info['season_type']=='REG':
                row = info['week'], info['home'], info['away'], info['year'], info['wday'], info['month'], info['day']
                schedulewriter.writerow(row)
#######################################################################################################################
"""
Listing top Receivers Targeted
"""
import nflgame

year, current_week = nflgame.live.current_year_and_week()
weeks = [x for x in range(1, current_week+1)]

games = nflgame.games(year, weeks)
players = nflgame.combine(games, plays=True)

for p in players.sort('receiving_tar').limit(50):
    print p, p.receiving_tar, p.team

#######################################################################################################################
"""
Exports all scores
"""
import nflgame
import csv

def writeScoresToCSV(year):
    games = nflgame.games_gen(year)
    with open('Scores_'+str(year)+'.csv', 'wb') as csvfile:
        scorewriter = csv.writer(csvfile, delimiter=',')
        scorewriter.writerow(['Week', 'Home', 'Home_Score', 'Away', 'Away_Score'])
        for game in games:
            row = game.schedule['week'], game.home, game.score_home, game.away, game.score_away
            scorewriter.writerow(row)

