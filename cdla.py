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

  print(type(reigningTid))
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


def team0():
  players = []

  for player in cdla['players']:
    if player['tid'] == 0:
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


def team1():
  players = []

  for player in cdla['players']:
    if player['tid'] == 1:
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


def team2():
  players = []

  for player in cdla['players']:
    if player['tid'] == 2:
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


def team3():
  players = []

  for player in cdla['players']:
    if player['tid'] == 3:
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


def team4():
  players = []

  for player in cdla['players']:
    if player['tid'] == 4:
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


def team5():
  players = []

  for player in cdla['players']:
    if player['tid'] == 5:
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


def team6():
  players = []

  for player in cdla['players']:
    if player['tid'] == 6:
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


def team7():
  players = []

  for player in cdla['players']:
    if player['tid'] == 7:
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


def team8():
  players = []

  for player in cdla['players']:
    if player['tid'] == 8:
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


def team9():
  players = []

  for player in cdla['players']:
    if player['tid'] == 9:
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


def team10():
  players = []

  for player in cdla['players']:
    if player['tid'] == 10:
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


def team11():
  players = []

  for player in cdla['players']:
    if player['tid'] == 11:
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


def team12():
  players = []

  for player in cdla['players']:
    if player['tid'] == 12:
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


def team13():
  players = []

  for player in cdla['players']:
    if player['tid'] == 13:
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


def team14():
  players = []

  for player in cdla['players']:
    if player['tid'] == 14:
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


def team15():
  players = []

  for player in cdla['players']:
    if player['tid'] == 15:
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


def team16():
  players = []

  for player in cdla['players']:
    if player['tid'] == 16:
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


def team17():
  players = []

  for player in cdla['players']:
    if player['tid'] == 17:
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


def team18():
  players = []

  for player in cdla['players']:
    if player['tid'] == 18:
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


def team19():
  players = []

  for player in cdla['players']:
    if player['tid'] == 19:
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
