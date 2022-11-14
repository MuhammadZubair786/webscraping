from requests_html import AsyncHTMLSession
from collections import defaultdict
import pandas as pd 


url = 'https://www.flashscore.com/football/england/premier-league-2018-2019/results/'

asession = AsyncHTMLSession()

async def get_scores():
    r = await asession.get(url)
    await r.html.arender()
    return r

results = asession.run(get_scores)
results = results[0]

times = results.html.find("div.event__time")
home_teams = results.html.find("div.event__participant.event__participant--home") 
scores = results.html.find("div.event__scores.fontBold")
away_teams = results.html.find("div.event__participant.event__participant--away")
event_part = results.html.find("div.event__part")


dict_res = defaultdict(list)

for ind in range(len(times)):
    dict_res['times'].append(times[ind].text)
    dict_res['home_teams'].append(home_teams[ind].text)
    dict_res['scores'].append(scores[ind].text)
    dict_res['away_teams'].append(away_teams[ind].text)
    dict_res['event_part'].append(event_part[ind].text)

df_res = pd.DataFrame(dict_res)
