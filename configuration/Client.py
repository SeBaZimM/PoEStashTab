# Class: Client
# The necessary client information that the app needs

# IMPORTS
import browser_cookie3

class Client():
	
	def __init__(self, account_name, league):
		self.account_name = account_name
		self.league 	  = league
		self.cookie_jar	  = browser_cookie3.load(config.POE[8:])
