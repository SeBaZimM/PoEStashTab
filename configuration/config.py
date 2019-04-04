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
	'ressources\\characters',
	'ressources\\images',
	'ressources\\images\\inventory',
]
REQUIRE_IMG = [
	'/image/inventory/MainInventory.png?1553142576000',
	'/image/inventory/WeaponSwap1.png?1553142576000',
	'/image/inventory/WeaponSwap2.png?1553142576000',
	'/image/inventory/Stash.png?1553142576000',
	'/image/inventory/StashPanelCurrency.png?1553142576000',
	'/image/inventory/EssenceStashPanelGrid.png?1553142576000',
	'/image/inventory/StashPanelDivinationCardBackground.png?1553142576000',
	'/image/inventory/StashPanelMap.png?1553142576000',
	'/image/inventory/StashPanelFragment.png?1553142576000',
	'/image/inventory/MTXStash.png?1553142576000',
	'/image/inventory/MTXListHeaderBackground.png?1553142576000',
	'/image/inventory/tabs-control/ExpandButton.png?1553142576000',
	'/image/layout/synthesis-bg.jpg?1553142582000',
]
