# config.py
# Contains the configuration for the app

ROOTPATH	= ''
ACCOUNTNAME = '[ACCOUNTNAME]'
LEAGUE 		= '[LEAGUE]'
POE 		= 'https://pathofexile.com'
LEAGUES 	= '/api/trade/data/leagues'
CHARACTERS  = '/character-window/get-characters'
STASH 		= '/character-window/get-stash-items?league=[LEAGUE]&accountName=[ACCOUNTNAME]&tabs=1'
STASHTAB 	= '/character-window/get-stash-items?league=[LEAGUE]&accountName=[ACCOUNTNAME]&tabs=0&tabIndex='
MTXSTASH 	= '/character-window/get-mtx-stash-items'
ITEMS 		= '/character-window/get-items?character='
PASSIVES 	= '/character-window/get-passive-skills?character='
REQUIRE_FOLDERS = [
	'ressources', 
	'ressources\\stashTabs',
	'ressources\\characters'
]
