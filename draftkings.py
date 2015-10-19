me
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is me trying to create a CSV file output.

The next module is actually a lot more helpful
"""
import nflgame

games = nflgame.games(2015, week=3)
players = nflgame.combine_game_stats(games)
positions = ['CB']
stats = {}
for p in players:
    if p.guess_position in positions:
        print p.stats, p.defense_int_tds

nflgame.combine_game_stats(nflgame.games(2015, week = 6)).csv("week6.csv")
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
Prints out all scores
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

