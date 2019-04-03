# utils.py
# A bunch of utility functions

import requests
import json
import os

from configuration import config


# Function: start_request
# Request the data from the given account /league and the ressources
#	Parameters:
#		url 	--- type: str 		 --- the given url to start a request
#		cookie  --- type: cookie_jar --- the saved session cookie from PoE
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
#		filename 	--- type: str  --- the filename to save
#		res_json 	--- type: json --- the response json object
#		ressources 	--- type: str  --- the url thet was requested
def save_dump(filename, res_json, ressource):
	with open(filename, 'w') as json_file:
		json.dump(res_json, json_file, indent=2)
		write_logfile('logfile.log', os.getcwd(), filename, ressource)


# Function: write_logfile
# Saved the league and characters ressources 
# whithout given account/league informations
#	Parameters:
#		logfile 	--- type: str --- the logfile to write
#		dest_path 	--- type: str --- the information where the file was saved
#		file 		--- type: str --- the filename that was saved
#		ressources 	--- type: str --- the url from where the information is
def write_logfile(logfile, dest_path, file, ressource):
	os.chdir(config.ROOTPATH)
	with open(logfile, 'a+') as log:
		output = '[PATH]{}\n[FILE]{}\n[RESSOURCE]{}\n'.format(
			dest_path, file, ressource)
		log.write(output + '###################################################################\n')


# Function: replace_placeholder
# Replace the standart ACCOUNTNAME / LEAGUE in the url
#	Parameters:
#		url 	 --- type: str --- the given url to replace
#		acc_name --- type: str --- the given Accountname
#		league 	 --- type: str --- the given league
def replace_placeholder(url, acc_name, league):
	ph_accountname  = '[ACCOUNTNAME]'
	ph_league		= '[LEAGUE]'
	if ph_accountname in url: url =  url.replace(ph_accountname, acc_name)
	if ph_league in url: 	  url =  url.replace(ph_league, league)
	return url
	