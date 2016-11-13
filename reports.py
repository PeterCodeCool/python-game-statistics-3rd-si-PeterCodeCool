# Report functions

import datetime

fn = []
fn = str('game_stat.txt')

actual_date = []
today = datetime.date.today()
actual_date.append(today)

def count_games(file_name):
    gamelist = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    return int(len(gamelist))

def decide(file_name, year):
    gamelist = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        if str(year) == i[2]:
            return True
        else:
            result = False
    return result

def get_latest(file_name):
    gamelist = []
    years = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        years.append(i[2])
    latest = years.index(max(years))
    return gamelist[latest][0]

def count_by_genre(file_name, genre):
    gamelist = []
    counter = 0
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        if genre == i[3]:
            counter += 1
    return counter

def get_line_number_by_title(file_name, title):
    gamelist = []
    years = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        if title == i[0]:
            return (gamelist.index(i)) + 1
    return 'value error'

def sort_abc(file_name):
    gamelist = []
    titles = []
    result = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        titles.append(i[0])
    for game in gamelist:
        result.append(min(titles))
        titles.remove(min(titles))
    return result

def get_genres(file_name):
    gamelist = []
    genres = []
    result = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        genres.append(i[3])
    genres = sorted(set(genres), key = str.lower)
    return genres

def when_was_top_sold_fps(file_name):
    gamelist = []
    shooterGames = []
    shooterSold = []
    with open(file_name, newline = '\n') as inputfile:
        for line in inputfile:
            gamelist.append(line.strip().split('\t'))
    for i in gamelist:
        if i[3] == "First-person shooter":
            shooterGames.append(i)
            shooterSold.append(float(i[1]))
    top_sold = shooterSold.index(max(shooterSold))
    return int(shooterGames[top_sold][2])

