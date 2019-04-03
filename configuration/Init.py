# Class: Init
# Initializes the necessary information that the app needs

# IMPORTS
import os
import asyncio
import browser_cookie3

from utilities import utils
from configuration import config

class Init():

	def __init__(self, account_name, league, cookie_jar):
		self.account_name = account_name
		self.league 	  = league
		self.cookie_jar	  = cookie_jar
		self.path 		  = os.getcwd()
		self.num_tabs 	  = 0
		self.chars 		  = list()
		self.is_setup 	  = False

	# Method: setup
	# The setup method to start the setup
	async def setup(self):
		await self.check_setup('logfile.log')
		if self.is_setup:
			return
		await asyncio.gather(
			self.set_config(config),
			self.create_req_folders(config.REQUIRE_FOLDERS),
			self.get_leagues(config.POE + config.LEAGUES, self.cookie_jar),
			self.get_characters(config.POE + config.CHARACTERS, self.cookie_jar),
			self.get_mtx_stash(config.POE + config.MTXSTASH, self.cookie_jar),
			self.get_stash(config.POE + config.STASH, self.cookie_jar),
			self.get_stash_tabs(config.POE + config.STASHTAB, self.cookie_jar),
			self.get_chars_items(config.POE + config.ITEMS, self.cookie_jar),
			self.get_chars_passives(config.POE + config.PASSIVES, self.cookie_jar)
		)

	# Method: update_all
	# Updates all data		
	async def update_all(self):
		await asyncio.gather(
				self.get_leagues(config.POE + config.LEAGUES, self.cookie_jar),
				self.get_characters(config.POE + config.CHARACTERS, self.cookie_jar),
				self.get_mtx_stash(config.POE + config.MTXSTASH, self.cookie_jar),
				self.get_stash(config.POE + config.STASH, self.cookie_jar),
				self.get_stash_tabs(config.POE + config.STASHTAB, self.cookie_jar),
				self.get_chars_items(config.POE + config.ITEMS, self.cookie_jar),
				self.get_chars_passives(config.POE + config.PASSIVES, self.cookie_jar)
			)


	# Method: update_leagues
	# Updates the PoE leagues
	async def update_leagues(self):
		await self.set_config(config)
		await self.get_leagues(config.POE + config.LEAGUES, self.cookie_jar)

	# Method: update_characters
	# Updates all characters
	async def update_characters(self):
		await self.set_config(config)
		await self.get_characters(config.POE + config.CHARACTERS, self.cookie_jar)

	# Method: update_mtxstash
	# Updates the mtxstash
	async def update_mtxstash(self):
		await self.set_config(config)
		await self.get_mtx_stash(config.POE + config.MTXSTASH, self.cookie_jar)

	# Method: update_stash
	# Updates the stash
	async def update_stash(self):
		await self.set_config(config)
		await self.get_stash(config.POE + config.STASH, self.cookie_jar)

	# Method: update_stashtab
	# Updates a specific stashtab
	async def update_stashtab(self, tab):
		await self.set_config(config)
		await self.get_stash_tab(config.POE + config.STASHTAB, tab, self.cookie_jar)

	# Method: update_stashtabs
	# Updates all stashtabs
	async def update_stashtabs(self):
		await self.set_config(config)
		await self.get_stash_tabs(config.POE + config.STASHTAB, self.cookie_jar)

	# Method: update_char_items
	# Updates all items from a character
	#	Parameters:
	#		char: the character name
	#			type: str
	async def update_char_items(self, char):
		await self.set_config(config)
		await self.get_char_items(config.POE + config.ITEMS, char, self.cookie_jar)

	# Method: update_all_chars_items
	# Updates all items from all characters
	async def update_all_chars_items(self):
		await self.set_config(config)
		await self.get_chars_items(config.POE + config.ITEMS, self.cookie_jar)

	# Method: update_char_passives
	# Updates all passives from a character
	#	Parameters:
	#		char: the character name
	#			type: str
	async def update_all_chars_passives(self, char):
		await self.set_config(config)
		await self.get_char_passives(config.POE + config.PASSIVES, char, self.cookie_jar)

	# Method: update_all_chars_passives
	# Updates all passives from all characters	
	async def update_all_chars_passives(self):
		await self.set_config(config)
		await self.get_chars_passives(config.POE + config.PASSIVES, self.cookie_jar)
		

	# Method: check_setup
	# Checked if a setup was already taken
	#	Parameters:
	#		logfile: the logfile to check / create
	#			type: str
	#		is_setup: the answer if a setup has been done
	#			type: bool
	#	Return:
	#		is_setup
	async def check_setup(self, logfile):
		if not os.path.isfile(self.path +'/'+ logfile):
			with open(logfile, 'w') as log:
				log.write('###################################################################\n')
			return 
		else: 
			self.is_setup = True
			return self.is_setup
		#if not os.stat(path +'/'+ logfile).st_size is 0:

	# Method: set_config
	# Sets the information in the config
	#	Parameters:
	#		conf: the configuration file
	#			type: module 
	async def set_config(self, conf):
		conf.ROOTPATH = self.path
		conf.ACCOUNTNAME = self.account_name
		conf.LEAGUE = self.league

	# Method: create_req_folders
	# Creates the required folders given from the config
	#	Parameters:
	#		req_folders: the requiered folders
	#			type: list
	async def create_req_folders(self, req_folders):
		for req_folder in req_folders:
			if not os.path.exists(os.getcwd() +'/'+ req_folder):
				os.mkdir(self.path +'/'+ req_folder)

	# Method: get_leagues
	# Get all leages from PoE
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_leagues(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		response = utils.start_request(conf_url, cookie_jar)
		utils.save_dump('leagues.json', response, conf_url)

	# Method: get_characters
	# Get all the characters from account
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_characters(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		response = utils.start_request(conf_url, cookie_jar)
		for char in response: self.chars.append(char)
		utils.save_dump('characters.json', response, conf_url)

	# Method: get_stash
	# Get all the stash from account
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_stash(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		conf_url = utils.replace_placeholder(conf_url, self.account_name, self.league)
		response = utils.start_request(conf_url, cookie_jar)
		self.num_tabs = response['numTabs']
		utils.save_dump('stash.json', response, conf_url)

	# Method: get_stash_tab
	# Get one specific stashtab from the stash
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_stash_tab(self, conf_url, tab, cookie_jar):
		conf_url = utils.replace_placeholder(conf_url, self.account_name, self.league)
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
	async def get_stash_tabs(self, conf_url, cookie_jar):
		conf_url = utils.replace_placeholder(conf_url, self.account_name, self.league)
		for tab in range(self.num_tabs):
			os.chdir(self.path +'/ressources/stashTabs')
			response = utils.start_request(conf_url + str(tab), cookie_jar)
			utils.save_dump('stashtab'+str(tab)+'.json', response, conf_url + str(tab))

	# Method: get_mtx_stash
	# Get the mtx stash from account
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_mtx_stash(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		response = utils.start_request(conf_url, cookie_jar)
		utils.save_dump('mtxstash.json', response, conf_url)

	# Method: get_char_items
	# Get all the items from a character
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_char_items(self, conf_url, char, cookie_jar):
		os.chdir(self.path +'/ressources/characters/')
		if not os.path.exists(os.getcwd() +'/'+ char):
			os.mkdir(char)
		os.chdir(self.path +'/ressources/characters/'+ char)
		response = utils.start_request(conf_url + char, cookie_jar)
		utils.save_dump('items.json', response, conf_url + char)

	# Method: get_chars_items
	# Get all the items from all characters
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_chars_items(self, conf_url, cookie_jar):
		for char in self.chars:
			os.chdir(self.path +'/ressources/characters/')
			if not os.path.exists(os.getcwd() +'/'+ char['name']):
				os.mkdir(char['name'])
			os.chdir(self.path +'/ressources/characters/'+ char['name'])
			response = utils.start_request(conf_url + char['name'], cookie_jar)
			utils.save_dump('items.json', response, conf_url + char['name'])

	# Method: get_char_passives
	# Get all the passives from a character
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_char_passives(self, conf_url, char, cookie_jar):
		os.chdir(self.path +'/ressources/characters/')
		if not os.path.exists(os.getcwd() +'/'+ char):
			os.mkdir(char)
		os.chdir(self.path +'/ressources/characters/'+ char)
		response = utils.start_request(conf_url + char, cookie_jar)
		utils.save_dump('pasives.json', response, conf_url + char)

	# Method: get_chars_passives
	# Get all the passives from all characters
	#	Parameters:
	#		conf_url: the given url 
	#			type: str
	#		cookie_jar: the saved session cookie
	#			type: cookie_jar
	async def get_chars_passives(self, conf_url, cookie_jar):
		for char in self.chars:
			os.chdir(self.path +'/ressources/characters/')
			if not os.path.exists(os.getcwd() +'/'+ char['name']):
				os.mkdir(char['name'])
			os.chdir(self.path +'/ressources/characters/'+ char['name'])
			response = utils.start_request(conf_url + char['name'], cookie_jar)
			utils.save_dump('pasives.json', response, conf_url + char['name'])
