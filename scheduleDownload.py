__author__ = 'LV-JYOO'

#! \usr\bin\python

"""
Downloading a CSV of the entire 2015 NFL Schedule
"""
import nflgame
import nflgame.sched
import csv

schedule_games = nflgame.sched.games

def writeScheduletoCSV(year):
    with open(str(year)+'_Schedule.csv', 'wb') as csvfile:
        schedulewriter = csv.writer(csvfile, delimiter=',')
        schedulewriter.writerow(['Home', 'Away', 'Week', 'Year', 'Month', 'Day'])
        for item, info in schedule_games.iteritems():
            ## Maybe I need to change the year to be a string variable
            if info['year'] == year and info['season_type']=='REG':
                row = info['home'], info['away'], info['week'], info['year'], info['wday'], info['month'], info['day']
                schedulewriter.writerow(row)

if __name__ == "__main__":
    writeScheduletoCSV(raw_input("What year would you like to download?"))