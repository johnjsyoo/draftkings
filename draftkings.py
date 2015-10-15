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

for x in range(1,18):
    nflgame.combine_game_stats(nflgame.games(2014, week = x)).csv("2014week%s.csv" % x)



#######################################################################################################################
"""
Downloading a CSV of the entire 2015 NFL Schedule
"""
import nflgame
import nflgame.sched
import csv

schedule_games = nflgame.sched.games

with open('2015_Schedule.csv', 'wb') as csvfile:
    schedulewriter = csv.writer(csvfile, delimiter=',')
    schedulewriter.writerow(['Home', 'Away', 'Week', 'Year'])
    for (y, t, w, h, a), info in schedule_games:
        if y == 2015 and t=='REG':
            schedulewriter.writerow([h, a, w, y])
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
    print p, p.receiving_tar

#######################################################################################################################

nflgame.combine_game_stats(nflgame.games(2015, week = 5))

year, current_week = nflgame.live.current_year_and_week()
weeks = [x for x in range(1, current_week+1)]

games = nflgame.games(year, weeks)
players = nflgame.combine(games, plays=True)

for p in players.sort('receiving_tar').limit(50):
    print p, p.receiving_tar





year = 2015
games = nflgame.games(year, home="NE", away="NE")
bigben = nflgame.find('Tom Brady')[0]
# bigben -> Ben Roethlisberger (QB, PIT)
# bigben.gsis_name -> B.Roethlisberger

for i, game in enumerate(games):
    if game.players.name(bigben.gsis_name):
        stats = game.players.name(bigben.gsis_name).passing_yds
        print 'Game {:2}, Week {:2} - {:4}'.format(
            i+1, game.schedule['week'], stats)

print '-'*25
players = nflgame.combine(games)
print '{:9} Season - {:4}'.format(
    year, players.name(bigben.gsis_name).passing_yds)


for  in schedule_games.iteritems():
        if y == 2015 and t=='REG':
            print y

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print key, 'corresponds to', d[key]