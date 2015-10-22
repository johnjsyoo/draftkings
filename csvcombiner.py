__author__ = 'LV-JYOO'

"""
Creates a Stat Map
"""

import pandas as pd
import os

os.getcwd()

allStats = pd.read_csv("./week2015/2015stats.csv")

allStats[['DK-passing_td']] = allStats[['passing_tds']] * 4
allStats[['DK-passing_yd']] = allStats[['passing_yds']] * .04
allStats[['DK-passing_int']] = allStats[['passing_ints']] * -1
allStats[['DK-passing_300']] = allStats[['passing_yds']].applymap(lambda x: x if pd.isnull(x) else (3 if x >=300 else 0))

allStats[['DK-rushing_td']] = allStats[['rushing_tds']] * 6
allStats[['DK-rushing_yd']] = allStats[['rushing_yds']] * 0.1
allStats[['DK-rushing_100']] = allStats[['rushing_yds']].applymap(lambda x: x if pd.isnull(x) else (3 if x >=100 else 0))

allStats[['DK-receiving_rec']] = allStats[['receiving_rec']] * 1
allStats[['DK-receiving_td']] = allStats[['receiving_tds']] * 6
allStats[['DK-receiving_yd']] = allStats[['receiving_yds']] * 0.1
allStats[['DK-receiving_100']] = allStats[['receiving_yds']].applymap(lambda x: x if pd.isnull(x) else (3 if x >=100 else 0))

allStats[['DK-puntret_td']] = allStats[['puntret_tds']] * 6
allStats[['DK-kickret_td']] = allStats[['kickret_tds']] * 6
allStats[['DK-fumbles_lost']] = allStats[['fumbles_lost']] * -1

allStats[['DK-passing_twoptm']] = allStats[['passing_twoptm']] * 2
allStats[['DK-rushing_twoptm']] = allStats[['rushing_twoptm']] * 2
allStats[['DK-receiving_twoptm']] = allStats[['receiving_twoptm']] * 2

allStats[['DK-total']] = allStats.loc[:,'DK-passing_td':'DK-receiving_twoptm']

allStats.to_csv("allStats.csv", index=False)