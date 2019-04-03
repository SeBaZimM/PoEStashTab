# utils.py
# A bunch of utility functions

import os
import json
import requests

from configuration import config


# Function: start_request
# Request the data from the given account /league and the ressources
#	Parameters:
#		url: the given url to start a request
#			type: str
#		cookie: the saved session cookie from PoE
#			type: cookie_jar
def start_request(url, cookie):
	try:
		response = requests.get(url, cookies=cookie)
		if response.status_code == 200:
			if not response is None:
				res_json = json.loads(response.text)
				return res_json
		else:
			raise Exception(response)
	except Exception as ex:
		print('ERROR: {}'.format(ex))

# Function: save_dump
# Saved the league and characters ressources 
# whithout given account/league informations
#	Parameters:
#		filename: the filename to save
#			type: str
#		res_json: the response json object
#			type: json
#		ressources: the url thet was requested
#			type: str 
def save_dump(filename, res_json, ressource):
	with open(filename, 'w') as json_file:
		json.dump(res_json, json_file, indent=2)
		write_logfile('logfile.log', os.getcwd(), filename, ressource)

# Function: write_logfile
# Saved the league and characters ressources 
# whithout given account/league informations
#	Parameters:
#		logfile: the logfile to write 	 
#			type: str
#		dest_path: the information where the file was saved 	 
#			type: str
#		filename: the filename that was saved 	 
#			type: str
#		ressources: the url from where the information is 	 
#			type: str
def write_logfile(logfile, dest_path, filename, ressource):
	os.chdir(config.ROOTPATH)
	with open(logfile, 'a+') as log:
		output = '[PATH]{}\n[FILE]{}\n[RESSOURCE]{}\n'.format(
			dest_path, filename, ressource)
		log.write(output + '###################################################################\n')

# Function: replace_placeholder
# Replace the standart ACCOUNTNAME / LEAGUE in the url
#	Parameters:
#		url: the given url to replace 	  
#			type: str
#		acc_name: the given Accountname  
#			type: str
#		league: the given league 	  
#			type: str
def replace_placeholder(url, acc_name, league):
	ph_accountname  = '[ACCOUNTNAME]'
	ph_league		= '[LEAGUE]'
	if ph_accountname in url:
		url = url.replace(ph_accountname, acc_name)
	if ph_league in url:
		url = url.replace(ph_league, league)
	return url
