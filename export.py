# Export functions

import sys
import reports
import datetime
from reports import fn
from reports import actual_date

sys.stdout = open('stat_export.txt', 'w')

print ('Reports:')

print ('Latest report: ', actual_date[0])
print ('____________________________________________________________________')
print (' ')



print ('Games:')
print ('Short by ABC')
print (' ')

for title in reports.sort_abc (fn):
    print(title)
print ('____________________________________________________________________')
print (' ')



print ('Genres of games:')
print (' ')

for genre in reports.get_genres(fn):
    print (genre)
print ('____________________________________________________________________')
print (' ')



print (' ')
print ('Statistics:')
print (' ')


print ('How many games are in the file: %i pcs' %(reports.count_games(fn)))

print ('How many games do we have by genre:')

for genre in reports.get_genres(fn):
    print ('                                 ', genre, ': %i pcs' %reports.count_by_genre(fn, genre))

print ('Which was the latest game: %s' %reports.get_latest(fn))

print ('What is the line number of the latest game:  %ith' %reports.get_line_number_by_title(fn, reports.get_latest(fn)))

if reports.decide(fn, 2004):
    print ('Is there a game from a given year: Yes, We have game from year, ', title)

else:
    print ('Is there a game from a given year: No, We have not from year, ')

print ('What is the release date of the top sold First-person shooters game: This game from %i.' %reports.when_was_top_sold_fps(fn))