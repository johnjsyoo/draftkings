me
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nflgame

games = nflgame.games(2015, week=5)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(20):
    print p, p.guess_position, p.rushing_att, p.rushing_yds, p.rushing_tds

