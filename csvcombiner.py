__author__ = 'LV-JYOO'

"""
Creates a Stat Map
"""

import pandas as pd
import os

os.getcwd()

allStats = pd.read_csv("2015stats.csv")

allStats[['DK-passing_td']] = allStats[['passing_tds']] * 6
allStats[['DK-passing_yd']] = allStats[['passing_tds']] * 6
allStats[['DK-passing_int']] = allStats[['passing_tds']] * 6
allStats[['DK-passing_300']] = if allStats[['passing_tds']] > 300):3 ## Needs a fix
allStats[['DK-rushing_td']] = allStats[['rushing_tds']] * 6
allStats[['DK-rushing_yd']] = allStats[['rushing_yds']] * 0.1
allStats[['DK-rushing_100']] = allStats[['rushing_yds']] * 0.1 ## Needs a fix
allStats[['DK-receiving_rec']] = allStats[['receiving_rec']] * 1
allStats[['DK-receiving_td']] = allStats[['receiving_tds']] * 6
allStats[['DK-receiving_yd']] = allStats[['receiving_yds']] * 0.1
allStats[['DK-receiving_100']] = allStats[['receiving_yds']] * 6 ## Needs a fix

allStats[['DK-puntret_td']] = allStats[['puntret_tds']] * 6
allStats[['DK-kickret_td']] = allStats[['kickret_tds']] * 6
allStats[['DK-fumbles_tot']] = allStats[['fumbles_tot']] * -1

allStats[['DK-passing_twoptm']] = allStats[['passing_twoptm']] * 2
allStats[['DK-rushing_twoptm']] = allStats[['rushing_twoptm']] * 2
allStats[['DK-receiving_twoptm']] = allStats[['receiving_twoptm']] * 2