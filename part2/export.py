# Export functions

import sys
import reports
import datetime
from reports import fn
from reports import actual_date

sys.stdout = open('stat_export.txt', 'w')

print ('Reports:')

print ('Latest report: ', actual_date[0])
print ('____________________________________________________________________ \n')

print ('What is the title of the most played game: %s. \n' %reports.get_most_played(fn))
print ('How many copies have been sold total: %i million copies \n' %reports.sum_sold(fn))
print ('What is the average selling: %.2f million. \n' %round(reports.get_selling_avg(fn), 2))
print ('How many characters long is the longest title:  %i characters long.\n' %reports.count_longest_title(fn))
print ('What is the average of the release dates: %i. \n' %reports.get_date_avg(fn))

print ('The properies of The Sims:')

game = reports.get_game(fn, 'The Sims')

print ('%s:    %s,    %s,    %s,    %s. \n' %
    (game[0], str(game[2]), str(game[1]), game[3], game[4]))

print ('How many games are there grouped by genre: \n')

genres = reports.count_grouped_by_genre(fn)

for x in genres:
    print (' ' * (20 - len(x)), x, ': ', genres[x])
print ('')
print ('What is the date ordered list of the games: \n')

for item in reports.get_date_ordered(fn):
    print (item)