me
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nflgame

games = nflgame.games(2015, week=5)
players = nflgame.combine_game_stats(games)
positions = ['QB','WR','TE','RB']
stats = {}
for p in players:
    if p.guess_position in positions:
        print p.name, p.guess_position, p.passing_tds, p.passing_cmp, p.passing_att, p.passing_yds, p.passing_ints,\
            p.rushing_att, p.rushing_yds, p.rushing_tds, \
            p.receiving_yds, p.receiving_rec, p.receiving_tds, \
            p.fumbles_lost,\
            p.twoptm, p.twopta,\
            p.puntret_tds, p.kickret_tds

nflgame.combine_game_stats(nflgame.games(2015, week = 5)).csv("week5.csv")
nflgame.combine_game_stats(nflgame.games(2015, week = 4)).csv("week4.csv")
nflgame.combine_game_stats(nflgame.games(2015, week = 3)).csv("week3.csv")
nflgame.combine_game_stats(nflgame.games(2015, week = 2)).csv("week2.csv")
nflgame.combine_game_stats(nflgame.games(2015, week = 1)).csv("week1.csv")

week1 = nflgame.combine_game_stats(nflgame.games(2015, week = 1))
positions = ['QB','WR','TE','RB']
for p in week1:
    if p.guess_position in positions:
        print p

nflgame.combine_game_stats(nflgame.games(2015)).csv("2015.csv")

########################################################################################################################
"""
Quick way to download all player stats in a given season
"""
for x in range(1,18):
    players = nflgame.combine_game_stats(nflgame.games(2014, week = x))
    for player in players:
        if player not in players.defense():
            player.
##############################
import csv

fields, rows = set([]), []
players = list(self)
for p in players:
    for field, stat in p.stats.iteritems():
        fields.add(field)
if allfields:
    for statId, info in statmap.idmap.iteritems():
        for field in info['fields']:
            fields.add(field)
fields = sorted(list(fields))

for p in players:
    d = {
        'name': p.name,
        'id': p.playerid,
        'home': p.home and 'yes' or 'no',
        'team': p.team,
        'pos': 'N/A',
    }
    if p.player is not None:
        d['pos'] = p.player.position

    for field in fields:
        if field in p.__dict__:
            d[field] = p.__dict__[field]
        else:
            d[field] = ""
    rows.append(d)

fieldNames = ["name", "id", "home", "team", "pos"] + fields
rows = [dict((f, f) for f in fieldNames)] + rows
csv.DictWriter(open(fileName, 'w+'), fieldNames).writerows(rows)


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

nflgame.combine_game_stats(nflgame.games(2015, week = 5))

year, current_week = nflgame.live.current_year_and_week()
weeks = [x for x in range(1, current_week+1)]

games = nflgame.games(year, weeks)
players = nflgame.combine(games, plays=True)

for p in players.sort('receiving_tar').limit(50):
    print p, p.receiving_tar

#######################################################################################################################

import nflgame

games = nflgame.games(2015)
teams = nflgame.combine_game_stats(games)
for team in teams.offense()
