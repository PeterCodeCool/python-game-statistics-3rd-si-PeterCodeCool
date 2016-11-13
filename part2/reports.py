# Report functions

from operator import itemgetter
import datetime

fn = []
fn = str('game_stat.txt')

actual_date = []
today = datetime.date.today()
actual_date.append(today)


def get_most_played(file_name):
    gamelist = []
    sells = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        sells.append(float(game[1]))
    mostplayed = sells.index(max(sells))
    return gamelist[sells.index(max(sells))][0]

def sum_sold(file_name):
    gamelist = []
    all_sells = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        all_sells.append(float(game[1]))
    return sum(all_sells)

def get_selling_avg(file_name):
    gamelist = []
    sells = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        sells.append(float(game[1]))
    return sum(sells) / len(sells)

def count_longest_title(file_name):
    gamelist = []
    titles_len = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        titles_len.append(len(game[0]))
    return max(titles_len)

def get_date_avg(file_name):
    gamelist = []
    years = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        years.append(int(game[2]))
    return round(sum(years) / len(years))

def get_game(file_name, title):
    gamelist = []
    titles = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        game[1] = float(game[1])
        game[2] = int(game[2])
        titles.append(game[0])
    return gamelist[titles.index(title)]

def count_grouped_by_genre(file_name):
    gamelist = []
    genres = {}
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for game in gamelist:
        if game[3] in genres:
            genres[game[3]] += 1
        else:
            genres[game[3]] = 1
    return genres

def get_date_ordered(file_name):
    gamelist = []
    result = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    gamelist = sorted(gamelist, key = itemgetter(0))
    gamelist = sorted(gamelist, key = itemgetter(2), reverse = True)
    for item in gamelist:
        result.append(item[0])
    return result