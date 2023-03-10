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