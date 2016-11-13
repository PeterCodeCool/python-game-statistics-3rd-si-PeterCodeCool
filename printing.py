# Printing functions

import reports
from reports import fn

print (reports.count_games(fn))
print (reports.decide(fn, 2000))
print (reports.count_by_genre(fn, 'Simulation'))
print (reports.get_line_number_by_title(fn, 'blavl'))
print (reports.sort_abc(fn))
print (reports.get_genres(fn))
print (reports.when_was_top_sold_fps(fn))