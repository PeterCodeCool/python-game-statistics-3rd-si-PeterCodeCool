# Printing functions

import reports

import reports
from reports import fn

print ('mostplayed')
print (reports.get_most_played(fn))

print ('sumsold')
print (reports.sum_sold(fn))

print ('avgselling')
print (reports.get_selling_avg(fn))

print ('longestitle')
print (reports.count_longest_title(fn))

print ('avgdate')
print (reports.get_date_avg(fn))

print ('thesims')
print (reports.get_game(fn, 'The Sims'))

print ('genres:')
print (reports.count_grouped_by_genre(fn))

print ('sorted:')
print (reports.get_date_ordered(fn))