import urllib.request, json

with urllib.request.urlopen(
    "https://raw.githubusercontent.com/buntaga/archivist-league-files/main/cdla-webpage.json"
) as url:
  cdla = json.load(url)


def reigning_champ():
  champions_list = []
  for team in cdla['teams']:
    for season in team['seasons']:
      if season['playoffRoundsWon'] == 4:
        string = str(
          season['season']) + " " + season['region'] + " " + season['name']
        champions_list.append(string)
        champions_list.sort()
  return champions_list[-1]


def champions_list():
  champions_list = []
  for team in cdla['teams']:
    for season in team['seasons']:
      if season['playoffRoundsWon'] == 4:
        string = str(
          season['season']) + " " + season['region'] + " " + season['name']
        champions_list.append(string)
  champions_list.sort()
  return champions_list


def team_list():
  team_list = []
  for team in cdla['teams']:
    team_name = team['region'] + " " + team['name']
    team_list.append({'name': team_name, 'tid': team['tid']})
  team_list = sorted(team_list, key=lambda d: d['name'])
  return team_list


def reigning_champ_players():
  champions_list = []

  for team in cdla['teams']:
    for season in team['seasons']:
      if season['playoffRoundsWon'] == 4:
        string = str(season['season']) + " " + str(team['tid'])
        champions_list.append(string)

  champions_list.sort()

  reigning = champions_list[-1]

  reigningTid = int(reigning[len(reigning) - 1])

  print(reigningTid)
  print(len(cdla['players']))

  playerChamps = []
  awardsCount = 0

  for player in cdla['players']:
    if player['stats']:
      for stat in player['stats']:
        if stat['season'] == cdla['gameAttributes'][0]['season'] and stat[
            'tid'] == reigningTid and stat['playoffs']:
          awardsCount += 1
          pos = player['ratings'][len(player['ratings']) - 1]['pos']
          ovr = player['ratings'][len(player['ratings']) - 1]['ovr']
          playerChamps.append({
            'name':
            player['firstName'] + " " + player['lastName'],
            'age':
            stat['season'] - player['born']['year'],
            'pos':
            pos,
            'ovr':
            ovr
          })

  if awardsCount == 0:
    for player in cdla['players']:
      if player['stats']:
        for stat in player['stats']:
          if stat['season'] == cdla['gameAttributes'][0]['season'] - 1 and stat[
              'tid'] == reigningTid and stat['playoffs']:
            pos = player['ratings'][len(player['ratings']) - 1]['pos']
            ovr = player['ratings'][len(player['ratings']) - 1]['ovr']
            playerChamps.append({
              'name':
              player['firstName'] + " " + player['lastName'],
              'age':
              stat['season'] - player['born']['year'],
              'pos':
              pos,
              'ovr':
              ovr
            })

  playerChamps = sorted(playerChamps, key=lambda d: d['ovr'], reverse=True)
  return (playerChamps)


def team0(num):
  players = []

  for player in cdla['players']:
    if player['tid'] == num:
      pos = player['ratings'][len(player['ratings']) - 1]['pos']
      ovr = player['ratings'][len(player['ratings']) - 1]['ovr']
      players.append({
        'name':
        player['firstName'] + " " + player['lastName'],
        'age':
        cdla['gameAttributes'][0]['season'] - player['born']['year'],
        'pos':
        pos,
        'ovr':
        ovr
      })
  players = sorted(players, key=lambda d: d['ovr'], reverse=True)
  return (players)


def mvp():
  awards = []
  for player in cdla['players']:
    for award in player['awards']:
      if award['type'] == 'Most Valuable Player':
        pos = 'n/a'
        for rating in player['ratings']:
          if rating['season'] == award['season']:
            pos = rating['pos']
        tid = 0
        for stat in player['stats']:
          if award['season'] == stat['season']:
            tid = stat['tid']
        for team in cdla['teams']:
          for season in team['seasons']:
            if season['season'] == award['season']:
              if player['firstName'] == 'Joel' and player['lastName'] == 'Lee':
                teamAbbrev = 'ATL'
              elif tid == season['tid']:
                teamAbbrev = season['abbrev']
        awards.append({
          'name': player['firstName'] + " " + player['lastName'],
          'age': award['season'] - player['born']['year'],
          'pos': pos,
          'season': award['season'],
          'award': award['type'],
          'abbrev': teamAbbrev
        })
  awards = sorted(awards, key=lambda d: d['season'])
  return awards


def dpoy():
  awards = []
  for player in cdla['players']:
    for award in player['awards']:
      if award['type'] == 'Defensive Player of the Year':
        pos = 'n/a'
        for rating in player['ratings']:
          if rating['season'] == award['season']:
            pos = rating['pos']
        tid = 0
        for stat in player['stats']:
          if award['season'] == stat['season']:
            tid = stat['tid']
        for team in cdla['teams']:
          for season in team['seasons']:
            if season['season'] == award['season']:
              if player['firstName'] == 'Joel' and player['lastName'] == 'Lee':
                teamAbbrev = 'ATL'
              elif tid == season['tid']:
                teamAbbrev = season['abbrev']
        awards.append({
          'name': player['firstName'] + " " + player['lastName'],
          'age': award['season'] - player['born']['year'],
          'pos': pos,
          'season': award['season'],
          'award': award['type'],
          'abbrev': teamAbbrev
        })
  awards = sorted(awards, key=lambda d: d['season'])
  return awards


def smoty():
  awards = []
  for player in cdla['players']:
    for award in player['awards']:
      if award['type'] == 'Sixth Man of the Year':
        pos = 'n/a'
        for rating in player['ratings']:
          if rating['season'] == award['season']:
            pos = rating['pos']
        tid = 0
        for stat in player['stats']:
          if award['season'] == stat['season']:
            tid = stat['tid']
        for team in cdla['teams']:
          for season in team['seasons']:
            if season['season'] == award['season']:
              if player['firstName'] == 'Joel' and player['lastName'] == 'Lee':
                teamAbbrev = 'ATL'
              elif tid == season['tid']:
                teamAbbrev = season['abbrev']
        awards.append({
          'name': player['firstName'] + " " + player['lastName'],
          'age': award['season'] - player['born']['year'],
          'pos': pos,
          'season': award['season'],
          'award': award['type'],
          'abbrev': teamAbbrev
        })
  awards = sorted(awards, key=lambda d: d['season'])
  return awards


def mip():
  awards = []
  for player in cdla['players']:
    for award in player['awards']:
      if award['type'] == 'Most Improved Player':
        pos = 'n/a'
        for rating in player['ratings']:
          if rating['season'] == award['season']:
            pos = rating['pos']
        tid = 0
        for stat in player['stats']:
          if award['season'] == stat['season']:
            tid = stat['tid']
        for team in cdla['teams']:
          for season in team['seasons']:
            if season['season'] == award['season']:
              if player['firstName'] == 'Joel' and player['lastName'] == 'Lee':
                teamAbbrev = 'ATL'
              elif tid == season['tid']:
                teamAbbrev = season['abbrev']
        awards.append({
          'name': player['firstName'] + " " + player['lastName'],
          'age': award['season'] - player['born']['year'],
          'pos': pos,
          'season': award['season'],
          'award': award['type'],
          'abbrev': teamAbbrev
        })
  awards = sorted(awards, key=lambda d: d['season'])
  return awards


def roy():
  awards = []
  for player in cdla['players']:
    for award in player['awards']:
      if award['type'] == 'Rookie of the Year':
        pos = 'n/a'
        for rating in player['ratings']:
          if rating['season'] == award['season']:
            pos = rating['pos']
        tid = 0
        for stat in player['stats']:
          if award['season'] == stat['season']:
            tid = stat['tid']
        for team in cdla['teams']:
          for season in team['seasons']:
            if season['season'] == award['season']:
              if player['firstName'] == 'Joel' and player['lastName'] == 'Lee':
                teamAbbrev = 'ATL'
              elif tid == season['tid']:
                teamAbbrev = season['abbrev']
        awards.append({
          'name': player['firstName'] + " " + player['lastName'],
          'age': award['season'] - player['born']['year'],
          'pos': pos,
          'season': award['season'],
          'award': award['type'],
          'abbrev': teamAbbrev
        })
  awards = sorted(awards, key=lambda d: d['season'])
  return awards


def team_history(num):
  titles = 0
  wins = 0
  losses = 0
  playoffs = 0
  team_history = {'retired': [], 'stats': []}
  for team in cdla['teams']:
    if num == team['tid']:
      for retired in team['retiredJerseyNumbers']:
        for player in cdla['players']:
          if retired['pid'] == player['pid']:
            name = player['firstName'] + " " + player['lastName']
            jersey = retired['number']
            team_history['retired'].append({'name': name, 'jersey': jersey})
      for stat in team['stats']:
        if stat['playoffs'] is True:
          playoffs += 1
      for season in team['seasons']:
        wins += season['won']
        losses += season['lost']
        if season['playoffRoundsWon'] == 4:
          titles += 1
      team_history['stats'].append({
        'titles': titles,
        'wins': wins,
        'losses': losses,
        'playoffs': playoffs
      })
  return team_history