#!/usr/bin/python3
##
# @package	script
# @file		configuration.py
# @brief	Load the configuration file for the script into a shared dictionary

# Path to the configuration file
__CONFIGURATION_FILE = "../configuration.json"

# Configuration
__CONFIGURATION = {}

# Try to import required modules to read configuration file
# Then read the configuration file
try:
	import json
	with open(__CONFIGURATION_FILE) as file:
		__CONFIGURATION = json.load(file)
except:
	print("Failed to load configuration file for script: " + __CONFIGURATION_FILE)
	exit(-1)