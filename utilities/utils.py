# utils.py
# A bunch of utility functions

# IMPORTS
import os
import json
import requests


# Function: start_request
# Start a request from a given url
#	Parameters:
#		url: the given url to start a request
#		cookie: the saved session cookie from PoE
#	Return:
#		res_json: an json object including the information
def start_request(url, cookie):
	try:
		response = requests.get(url, cookies=cookie)
		if response.status_code == 200:
			if not response is None:
				if not cookie is None:
					res_json = json.loads(response.text)
					return res_json
				return response
		else:
			raise Exception(response)
	except Exception as ex:
		print('ERROR: {}, {}'.format(ex, url))


# Function: save_dump
# Saved the given information as an json object
#	Parameters:
#		filename: the filename to save
#		res_json: the response json object
#		ressources: the url thet was requested
def save_dump(filename, res_json, ressource):
	if res_json is None:
		return
	with open(filename, 'w') as json_file:
		json.dump(res_json, json_file, indent=2)
		write_logfile('logfile.log', filename, ressource)


# Function: save_img
# Saved the given information as an json object
#	Parameters:
#		filename: the filename to save
#		res_json: the response json object
#		ressources: the url thet was requested
def save_img(filename, response, ressource):
	with open(os.getcwd() +'/ressources/images/inventory/' + filename, 'wb') as img:
		img.write(response.content)
		write_logfile('logfile.log', filename, ressource)


# Function: write_logfile
# Write the given parameters into the logfile
#	Parameters:
#		logfile: the logfile to write 	 
#		filename: the filename that was saved 	 
#		ressources: the url from where the information is 	 
def write_logfile(logfile, filename, ressource):
	with open(logfile, 'a+') as log:
		output = '[FILE]{}\n[RESSOURCE]{}\n'.format(
			filename, ressource)
		log.write(output + '###################################################################\n')


# Function: replace_placeholder
# Replace the default ACCOUNTNAME / LEAGUE in the url
#	Parameters:
#		url: the given url to replace 	  
#		acc_name: the given Accountname  
#		league: the given league 	  
def replace_placeholder(url, acc_name, league):
	ph_accountname  = '[ACCOUNTNAME]'
	ph_league		= '[LEAGUE]'
	if ph_accountname in url:
		url = url.replace(ph_accountname, acc_name)
	if ph_league in url:
		url = url.replace(ph_league, league)
	return url
