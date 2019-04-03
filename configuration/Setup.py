# Class: Setup
# Initializes the necessary information that the app needs

# IMPORTS
import os
import asyncio
import browser_cookie3

from utilities import utils
from configuration import config

class Setup():

	def __init__(self, account_name, league, cookie_jar):
		self.account_name = account_name
		self.league 	  = league
		self.cookie_jar	  = cookie_jar
		self.path 		  = os.getcwd()
		self.num_tabs 	  = 0
		self.chars 		  = list()
		self.is_setup 	  = False


	# Method: setup
	# The main Method to start the setup
	async def setup(self):
		await self.check_setup('logfile.log', self.is_setup)
		await self.set_config(config)
		await self.create_req_folders(config.REQUIRE_FOLDERS)
		await self.get_leagues(config.POE + config.LEAGUES, self.cookie_jar)
		await self.get_characters(config.POE + config.CHARACTERS, self.cookie_jar)
		await self.get_mtx_stash(config.POE + config.MTXSTASH, self.cookie_jar)
		await self.get_stash(config.POE + config.STASH, self.cookie_jar)
		await self.get_stash_tabs(config.POE + config.STASHTAB, self.cookie_jar)
		await self.get_char_items(config.POE + config.ITEMS, self.cookie_jar)
		await self.get_char_passives(config.POE + config.PASSIVES, self.cookie_jar)
		

	# Method: check_setup
	# Checked if a setup was already taken
	#	Parameters:
	#		logfile  --- type: str  --- the logfile to check / create
	#		is_setup --- type: bool --- the answer if a setup has been done
	#	Return:
	#		is_setup
	async def check_setup(self, logfile, is_setup):
		if not os.path.isfile(self.path +'/'+ logfile):
			with open(logfile, 'w') as log:
				log.write('###################################################################\n')
			return is_setup
		else: 
			is_setup = True
			return is_setup
		#if not os.stat(path +'/'+ logfile).st_size is 0:


	# Method: set_config
	# Sets the information in the config
	#	Parameters:
	#		conf --- type: module --- the configuration file
	async def set_config(self, conf):
		conf.ROOTPATH = self.path
		conf.ACCOUNTNAME = self.account_name
		conf.LEAGUE = self.league


	# Method: create_req_folders
	# Creates the required folders given from the config
	#	Parameters:
	#		req_folders --- type: list --- the requiered folders
	async def create_req_folders(self, req_folders):
		for req_folder in req_folders:
			if not os.path.exists(os.getcwd() +'/'+ req_folder):
				os.mkdir(self.path +'/'+ req_folder)


	# Method: get_leagues
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_leagues(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		response = utils.start_request(conf_url, cookie_jar)
		utils.save_dump('leagues.json', response, conf_url)


	# Method: get_characters
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_characters(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		response = utils.start_request(conf_url, cookie_jar)
		for char in response: self.chars.append(char)
		utils.save_dump('characters.json', response, conf_url)


	# Method: get_stash
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_stash(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		conf_url = utils.replace_placeholder(conf_url, self.account_name, self.league)
		response = utils.start_request(conf_url, cookie_jar)
		self.num_tabs = response['numTabs']
		utils.save_dump('stash.json', response, conf_url)


	# Method: get_stash_tabs
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_stash_tabs(self, conf_url, cookie_jar):
		conf_url = utils.replace_placeholder(conf_url, self.account_name, self.league)
		for tab in range(self.num_tabs):
			os.chdir(self.path +'/ressources/stashTabs')
			response = utils.start_request(conf_url + str(tab), cookie_jar)
			utils.save_dump('stashtab'+str(tab)+'.json', response, conf_url)


	# Method: get_mtx_stash
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_mtx_stash(self, conf_url, cookie_jar):
		os.chdir(self.path +'/ressources')
		response = utils.start_request(conf_url, cookie_jar)
		utils.save_dump('mtxstash.json', response, conf_url)


	# Method: get_char_items
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_char_items(self, conf_url, cookie_jar):
		for char in self.chars:
			os.chdir(self.path +'/ressources/characters/')
			if not os.path.exists(os.getcwd() +'/'+ char['name']):
				os.mkdir(char['name'])
			os.chdir(self.path +'/ressources/characters/'+ char['name'])
			response = utils.start_request(conf_url + char['name'], cookie_jar)
			utils.save_dump('items.json', response, conf_url)


	# Method: get_char_passives
	# Get the information from the url
	#	Parameters:
	#		conf_url   --- type: str 		--- the given url
	#		cookie_jar --- type: cookie_jar --- the saved session cookie
	async def get_char_passives(self, conf_url, cookie_jar):
		for char in self.chars:
			os.chdir(self.path +'/ressources/characters/')
			if not os.path.exists(os.getcwd() +'/'+ char['name']):
				os.mkdir(char['name'])
			os.chdir(self.path +'/ressources/characters/'+ char['name'])
			response = utils.start_request(conf_url + char['name'], cookie_jar)
			utils.save_dump('pasives.json', response, conf_url)
