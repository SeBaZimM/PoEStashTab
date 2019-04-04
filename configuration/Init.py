# Class: Init
# Initializes the necessary information that the app needs

# IMPORTS
import os
import json

from utilities import utils
from configuration import config


class Init():

	def __init__(self, client):
		self.client		  		= client
		self.path 		  		= os.getcwd()
		self.num_tabs_synth 	= 0
		self.num_tabs_hc_synth	= 0
		self.num_tabs_stand		= 0
		self.num_tabs_hc	  	= 0
		self.chars 		  		= list()
		self.is_setup 	  		= False
		self.check_setup('logfile.log')


	# Method: setup
	# The setup method to start the setup
	def setup(self):
		if self.is_setup:
			return
		self.set_config(config),
		self.create_req_folders(config.REQUIRE_FOLDERS)
		self.get_req_img(config.POE, config.REQUIRE_IMG)
		self.get_leagues(config.POE + config.LEAGUES, self.client.cookie_jar)
		self.get_characters(config.POE + config.CHARACTERS, self.client.cookie_jar)
		self.get_mtx_stash(config.POE + config.MTXSTASH, self.client.cookie_jar)
		self.get_stash(config.POE + config.STASH, self.client.cookie_jar)
		self.get_stash_tabs(config.POE + config.STASHTAB, self.client.cookie_jar)
		self.get_chars_items(config.POE + config.ITEMS, self.client.cookie_jar)
		self.get_chars_passives(config.POE + config.PASSIVES, self.client.cookie_jar)


	# Method: update_all
	# Updates all data		
	def update_all(self):
		self.set_config(config)
		self.get_leagues(config.POE + config.LEAGUES, self.client.cookie_jar)
		self.get_characters(config.POE + config.CHARACTERS, self.client.cookie_jar)
		self.get_mtx_stash(config.POE + config.MTXSTASH, self.client.cookie_jar)
		self.get_stash(config.POE + config.STASH, self.client.cookie_jar)
		self.get_stash_tabs(config.POE + config.STASHTAB, self.client.cookie_jar)
		self.get_chars_items(config.POE + config.ITEMS, self.client.cookie_jar)
		self.get_chars_passives(config.POE + config.PASSIVES, self.client.cookie_jar)


	# Method: update_leagues
	# Updates the PoE leagues
	def update_leagues(self):
		self.set_config(config)
		self.get_leagues(config.POE + config.LEAGUES, self.client.cookie_jar)

	# Method: update_characters
	# Updates all characters
	def update_characters(self):
		self.set_config(config)
		self.get_characters(config.POE + config.CHARACTERS, self.client.cookie_jar)

	# Method: update_mtxstash
	# Updates the mtxstash
	def update_mtxstash(self):
		self.set_config(config)
		self.get_mtx_stash(config.POE + config.MTXSTASH, self.client.cookie_jar)

	# Method: update_stash
	# Updates the stash
	def update_stash(self):
		self.set_config(config)
		self.get_stash(config.POE + config.STASH, self.client.cookie_jar)

	# Method: update_stashtab
	# Updates a specific stashtab
	def update_stashtab(self, tab):
		self.set_config(config)
		self.get_stash_tab(config.POE + config.STASHTAB, tab, self.client.cookie_jar)

	# Method: update_stashtabs
	# Updates all stashtabs
	def update_stashtabs(self):
		self.set_config(config)
		self.get_stash_tabs(config.POE + config.STASHTAB, self.client.cookie_jar)

	# Method: update_char_items
	# Updates all items from a character
	#	Parameters:
	#		char: the character name
	#			type: str
	def update_char_items(self, char, league):
		self.set_config(config)
		self.get_char_items(config.POE + config.ITEMS, char, self.client.cookie_jar)

	# Method: update_all_chars_items
	# Updates all items from all characters
	def update_all_chars_items(self):
		self.set_config(config)
		self.get_chars_items(config.POE + config.ITEMS, self.client.cookie_jar)

	# Method: update_char_passives
	# Updates all passives from a character
	#	Parameters:
	#		char: the character name
	#			type: str
	def update_all_chars_passives(self, char, league):
		self.set_config(config)
		self.get_char_passives(config.POE + config.PASSIVES, char, self.client.cookie_jar)

	# Method: update_all_chars_passives
	# Updates all passives from all characters	
	def update_all_chars_passives(self):
		self.set_config(config)
		self.get_chars_passives(config.POE + config.PASSIVES, self.client.cookie_jar)
		

	# Method: check_setup
	# Checking if a setup was already taken
	#	Parameters:
	#		logfile: the logfile to check / create
	#			type: str
	#		is_setup: the answer if a setup has been done
	#			type: bool
	#	Return:
	#		is_setup
	def check_setup(self, logfile):
		if not os.path.isfile(self.path +'/'+ logfile):
			with open(logfile, 'w') as log:
				log.write('###################################################################\n')
			return 
		else: 
			self.is_setup = True
			return self.is_setup


	# Method: set_config
	# Sets the information in the config
	#	Parameters:
	#		conf: the configuration file
	#			type: module 
	def set_config(self, conf):
		conf.ROOTPATH = self.path
		conf.ACCOUNTNAME = self.client.account_name
		conf.LEAGUE = self.client.league


	# Method: create_req_folders
	# Creates the required folders given from the config
	#	Parameters:
	#		req_folders: the requiered folders
	#			type: list
	def create_req_folders(self, req_folders):
		for req_folder in req_folders:
			if not os.path.exists(self.path +'/'+ req_folder):
				os.mkdir(self.path +'/'+ req_folder)


	# Method: get_req_img
	# Downloads the required images given from the config
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		img_urls: the requiered images
	#			type: list
	def get_req_img(self, conf_url, img_urls):
		for img_url in img_urls:
			if 'synthesis' in img_url:
				filename_pos_start = img_url.find('/image/layout/') + len('/image/layout/')
			elif 'tabs-control' in img_url:
				filename_pos_start = img_url.find('/image/inventory/tabs-control/') + len('/image/inventory/tabs-control/')
			else:
				filename_pos_start = img_url.find('/image/inventory/') + len('/image/inventory/')
			filename_pos_end = img_url.find('?')
			filename = img_url[ filename_pos_start : filename_pos_end]
			if os.path.exists(self.path +'/ressources/images/inventory/'+ filename):
				continue
			response = utils.start_request(conf_url + img_url, None)
			utils.save_img(filename, response, conf_url)


	# Method: get_leagues
	# Get all leagues from PoE
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_leagues(self, conf_url, cookie_jar):
		response = utils.start_request(conf_url, cookie_jar)
		utils.save_dump(self.path +'/ressources/leagues.json', response, conf_url)


	# Method: get_characters
	# Get all the characters from account
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_characters(self, conf_url, cookie_jar):
		response = utils.start_request(conf_url, cookie_jar)
		for char in response: self.chars.append(char)
		utils.save_dump(self.path +'/ressources/characters/characters.json', response, conf_url)

	
	# Method: get_stash
	# Get all the stash from account
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_stash(self, conf_url, cookie_jar):
		with open(self.path +'/ressources/leagues.json','r') as leagues:
			j_leagues = json.load(leagues)
			for league in j_leagues['result']:
				url_tmp = conf_url
				conf_url = utils.replace_placeholder(conf_url, self.client.account_name, league['id'])
				response = utils.start_request(conf_url, cookie_jar)
				if league['id'] == 'Synthesis':
					self.num_tabs_synth = response['numTabs']
					if not os.path.exists(self.path +'/ressources/stashTabs/'+ league['id']):
						os.mkdir(self.path +'/ressources/stashTabs/'+ league['id'])
				elif league['id'] == 'Hardcore Synthesis':
					self.num_tabs_hc_synth = response['numTabs']
					if not os.path.exists(self.path +'/ressources/stashTabs/'+ league['id']):
						os.mkdir(self.path +'/ressources/stashTabs/'+ league['id'])
				elif league['id'] == 'Standard':
					self.num_tabs_stand = response['numTabs']
					if not os.path.exists(self.path +'/ressources/stashTabs/'+ league['id']):
						os.mkdir(self.path +'/ressources/stashTabs/'+ league['id'])
				elif league['id'] == 'Hardcore':
					self.num_tabs_hc = response['numTabs']
					if not os.path.exists(self.path +'/ressources/stashTabs/'+ league['id']):
						os.mkdir(self.path +'/ressources/stashTabs/'+ league['id'])
				utils.save_dump(self.path +'/ressources/stashTabs/stash_'+ league['id'] +'.json', response, conf_url)
				conf_url = url_tmp


	# TODO --------------------------------------
	# Method: get_stash_tab
	# Get one specific stashtab from the stash
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		tab: the specific stashtab
	#			type: str / int
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_stash_tab(self, conf_url, tab, cookie_jar):
		conf_url = utils.replace_placeholder(conf_url, self.client.account_name, self.client.league)
		os.chdir(self.path +'/ressources/stashTabs')
		response = utils.start_request(conf_url + str(tab), cookie_jar)
		utils.save_dump('stashtab'+str(tab)+'.json', response, conf_url + str(tab))


	# Method: get_stash_tabs
	# Get all the stashtabs from the stash
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_stash_tabs(self, conf_url, cookie_jar):
		with open(self.path +'/ressources/leagues.json','r') as leagues:
			j_leagues = json.load(leagues)
			for league in j_leagues['result']:
				url_tmp = conf_url
				conf_url = utils.replace_placeholder(conf_url, self.client.account_name, league['id'])
				if league['id']   == 'Synthesis': 		   numTabs = self.num_tabs_synth
				elif league['id'] == 'Hardcore Synthesis': numTabs = self.num_tabs_hc_synth
				elif league['id'] == 'Standard': 		   numTabs = self.num_tabs_stand 
				elif league['id'] == 'Hardcore': 		   numTabs = self.num_tabs_hc 
				for tab in range(numTabs):
					response = utils.start_request(conf_url + str(tab), cookie_jar)
					utils.save_dump(self.path +'/ressources/stashTabs/' + league['id'] +'/stashtab'+str(tab)+'.json', response, conf_url + str(tab))
				conf_url = url_tmp


	# Method: get_mtx_stash
	# Get the mtx stash from account
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_mtx_stash(self, conf_url, cookie_jar):
		response = utils.start_request(conf_url, cookie_jar)
		utils.save_dump(self.path +'/ressources/stashTabs/mtxstash.json', response, conf_url)


	# TODO --------------------------------------
	# Method: get_char_items
	# Get all the items from a character
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		char: the charactername
	#			type: str
	#		league: the league
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_char_items(self, conf_url, char, league, cookie_jar):
		os.chdir(self.path +'/ressources/characters/')
		if not os.path.exists(os.getcwd() +'/'+ league +'/'+ char):
			os.mkdir(char)
		os.chdir(self.path +'/ressources/characters/'+ league +'/'+  char)
		response = utils.start_request(conf_url + char, cookie_jar)
		utils.save_dump('items.json', response, conf_url + char)


	# Method: get_chars_items
	# Get all the items from all characters
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_chars_items(self, conf_url, cookie_jar):
		for char in self.chars:
			if not os.path.exists(self.path +'/ressources/characters/'+ char['league']):
				os.mkdir(self.path +'/ressources/characters/'+ char['league'])
			if not os.path.exists(self.path +'/ressources/characters/'+ char['league'] +'/'+ char['name']):
				os.mkdir(self.path +'/ressources/characters/'+ char['league'] +'/'+ char['name'])
			response = utils.start_request(conf_url + char['name'], cookie_jar)
			utils.save_dump(self.path +'/ressources/characters/'+ char['league'] +'/items.json', response, conf_url + char['name'])


	# Method: get_char_passives
	# Get all the passives from a character
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		char: the charactername
	#			type: str
	#		league: the league
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_char_passives(self, conf_url, char, league, cookie_jar):
		if not os.path.exists(self.path +'/ressources/characters/'+ league +'/'+ char):
			os.mkdir(self.path +'/ressources/characters/'+ league +'/'+ char)
		response = utils.start_request(conf_url + char, cookie_jar)
		utils.save_dump(self.path +'/ressources/characters/'+ league +'/'+ char +'/pasives.json', response, conf_url + char)


	# Method: get_chars_passives
	# Get all the passives from all characters
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	def get_chars_passives(self, conf_url, cookie_jar):
		for char in self.chars:
			if not os.path.exists(self.path +'/ressources/characters/'+ char['league']):
				os.mkdir(self.path +'/ressources/characters/'+ char['league'])
			if not os.path.exists(self.path +'/ressources/characters/'+ char['league'] +'/'+ char['name']):
				os.mkdir(self.path +'/ressources/characters/'+ char['league'] +'/'+ char['name'])
			response = utils.start_request(conf_url + char['name'], cookie_jar)
			utils.save_dump(self.path +'/ressources/characters/'+ char['league'] +'/'+ char['name'] +'/pasives.json', response, conf_url + char['name'])
