# Class: Client
# The necessary client information that the app needs

# IMPORTS
import browser_cookie3
import configuration.config as config

class Client:
	def __init__(self, account_name, league):
		self.account_name = account_name
		self.league 	  = league
		self.cookie_jar	  = browser_cookie3.load(config.POE[8:])


	def change_account_name(self, account_name):
		self.account_name = account_name


	def change_league(self, league):
		self.league = league
